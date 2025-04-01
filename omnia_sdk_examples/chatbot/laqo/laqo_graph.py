from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.constants import END
from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.langgraph.chatbot.chatbot_graph import (
    ChatbotFlow,
    State,
    )
from omnia_sdk.workflow.tools.ai.rag.assistant import assistant_response
from omnia_sdk.workflow.tools.contact_center.agent_tools import (
    time_aware_agent_transfer,
    )

from omnia_sdk_examples.chatbot.laqo import entity_extraction, travel_insurance
from omnia_sdk_examples.chatbot.laqo.intent import detect_laqo_intent
from omnia_sdk_examples.chatbot.laqo.localization import (
    MULTIPLE_OFFER,
    OUTRO,
    SINGLE_OFFER,
    TRAVEL_DURATION,
    TRAVEL_INTRO,
    TRAVEL_LOCATION,
    TRAVEL_TYPE,
    )

AGENT_INTENTS = {"agent", "unknown", "sales"}
LOCATION = "location"
NUM_TRIPS = "num_trips"
LOCALIZED_NUM_TRIPS = "localized_num_trips"
LOCALIZED_LOCATION = "localized_location"

LAQO_ASSISTANT_ID = "8817a65a-c312-4da4-8f9a-7ff6d7eafb05"


class Pavle(ChatbotFlow):
    def __init__(self, checkpointer: BaseCheckpointSaver = None, configuration: ChatbotConfiguration = None, translation_table=None):
        super().__init__(checkpointer=checkpointer, configuration=configuration, translation_table=translation_table)

    def start(self, state: State, config: dict):
        text = self.get_user_message_text(state=state)
        intent = detect_laqo_intent(message=text, config=config)
        ChatbotFlow.save_intent(state=state, intent=intent)

    def agent_transfer(self, state: State, config: dict):
        time_aware_agent_transfer(country_code="HR")

    def chatbot(self, state: State, config: dict):
        text = self.get_user_message_text(state=state)
        reply = assistant_response(message=text, assistant_id=LAQO_ASSISTANT_ID, config=config, language=self.get_language(state))
        ChatbotFlow.send_text_response(text=reply, state=state, config=config)

    def travel_intro(self, state: State, config: dict):
        self.send_predefined_response(key=TRAVEL_INTRO, state=state, config=config)
        self.send_predefined_response(key=TRAVEL_TYPE, state=state, config=config)

    def travel_type(self, state: State, config: dict):
        # single or multiple trips
        num_trips = ChatbotFlow.wait_user_input(state=state, config=config, variable_name=NUM_TRIPS)
        # localization.py will have lowercased keys for num trips which will be aligned with postback result
        self.save_variable(name=LOCALIZED_NUM_TRIPS, value=self.get_localized_constant(num_trips, state), state=state)

    def travel_duration(self, state: State, config: dict):
        ChatbotFlow.wait_user_input(state=state, config=config, variable_name=TRAVEL_DURATION, extractor=int)
        self.send_predefined_response(key=TRAVEL_LOCATION, state=state, config=config)

    def travel_location(self, state: State, config: dict):
        # this is postback data from button or user text message
        location_message = ChatbotFlow.wait_user_input(state=state, config=config)
        # extracted location is always in english language
        location = entity_extraction.extract_location(message=location_message)
        # we save extracted location for further insurance calculation
        self.save_variable(name=LOCATION, value=location, state=state)
        # we save localized location to generate reply to user
        self.save_variable(name=LOCALIZED_LOCATION, value=self.get_localized_constant(location, state), state=state)
        self._estimate_cost(config=config, state=state)
        self.send_predefined_response(key=OUTRO, state=state, config=config)

    def _estimate_cost(self, config: dict, state: State):
        num_trips = ChatbotFlow.get_variable(state=state, name=NUM_TRIPS)
        if num_trips == "single":
            cost = travel_insurance.calculate_single_trip(**self.get_variables(state))
            self.send_predefined_response(key=SINGLE_OFFER, state=state, config=config, cost=cost)
        else:
            cost = travel_insurance.calculate_multiple_trip(**self.get_variables(state))
            self.send_predefined_response(key=MULTIPLE_OFFER, state=state, config=config, cost=cost)

    def intent_transition(self, state: State, config: dict) -> str:
        intent = self.get_intent(state=state)
        if intent in AGENT_INTENTS:
            return "agent_transfer"
        return intent

    def route_travel_type(self, state: State, config: dict) -> str:
        num_trips = self.get_variable(state=state, name=NUM_TRIPS)
        if num_trips == "single":
            self.send_predefined_response(key=TRAVEL_DURATION, state=state, config=config)
            return "travel_duration"
        self.send_predefined_response(key=TRAVEL_LOCATION, state=state, config=config)
        return "travel_location"

    def _transitions(self) -> None:
        self.add_conditional_edge("start", self.intent_transition)
        self.add_edge("agent_transfer", END)
        self.add_edge("chatbot", END)
        self.add_edge("travel", "travel_type")
        self.add_conditional_edge("travel_type", self.route_travel_type)
        self.add_edge("travel_duration", "travel_location")
        self.add_edge("travel_location", END)

    def _nodes(self) -> None:
        self.add_node("start", self.start)
        self.add_node("agent_transfer", self.agent_transfer)
        self.add_node("chatbot", self.chatbot)
        self.add_node("travel", self.travel_intro)
        self.add_node("travel_type", self.travel_type)
        self.add_node("travel_duration", self.travel_duration)
        self.add_node("travel_location", self.travel_location)
        self.create_entry_point(start_node="start")
