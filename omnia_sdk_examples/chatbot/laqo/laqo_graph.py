from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.constants import END
from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.langgraph.chatbot.chatbot_graph import ChatbotFlow, State, CHATBOT_STATE
from omnia_sdk.workflow.tools.ai.rag.assistant import assistant_response
from omnia_sdk.workflow.tools.channels.localize import is_value_in_table
from omnia_sdk.workflow.tools.contact_center.agent_tools import time_aware_agent_transfer

from omnia_sdk_examples.chatbot.laqo import entity_extraction, travel_insurance
from omnia_sdk_examples.chatbot.laqo.intent import detect_laqo_intent
from omnia_sdk_examples.chatbot.laqo.localization import TRAVEL_INTRO, TRAVEL_TYPE, TRAVEL_DURATION, TRAVEL_LOCATION, \
    OUTRO, TRAVEL_TYPE_ONE, SINGLE_OFFER, MULTIPLE_OFFER

AGENT_INTENTS = {"agent", "unknown", "sales"}
LOCATION = "location"

LAQO_ASSISTANT_ID = "8817a65a-c312-4da4-8f9a-7ff6d7eafb05"

class Pavle(ChatbotFlow):

    def __init__(self, checkpointer: BaseCheckpointSaver = None, configuration: ChatbotConfiguration = None, translation_table=None):
        super().__init__(checkpointer=checkpointer, configuration=configuration, translation_table=translation_table)

    def start(self, state: State, config: dict):
        user_message = self.get_user_message(state=state)
        intent = detect_laqo_intent(message=user_message, config=config)
        ChatbotFlow.save_intent(state=state, intent=intent)

    def agent_transfer(self, state: State, config: dict):
        time_aware_agent_transfer(country_code="HR")

    def chatbot(self, state: State, config: dict):
        user_message = ChatbotFlow.get_user_message(state=state)
        reply = assistant_response(message=user_message, assistant_id=LAQO_ASSISTANT_ID, config=config)
        ChatbotFlow.send_response(message=reply, state=state, config=config)

    def travel_intro(self, state: State, config: dict):
        self.send_predefined_response(key=TRAVEL_INTRO, state=state, config=config)
        self.send_buttons_response(key=TRAVEL_TYPE, state=state, config=config)

    def travel_type(self, state: State, config: dict):
        ChatbotFlow.wait_user_input(state=state, config=config, variable_name=TRAVEL_TYPE)

    def travel_duration(self, state: State, config: dict):
        ChatbotFlow.wait_user_input(state=state, config=config, variable_name=TRAVEL_DURATION, extractor=int)
        self.send_buttons_response(key=TRAVEL_LOCATION, state=state, config=config)

    def travel_location(self, state: State, config: dict):
        ChatbotFlow.wait_user_input(state=state, config=config)
        message = ChatbotFlow.get_user_message(state=state)
        location = entity_extraction.extract_location(message=message)
        self.save_variable(name=LOCATION, value=location, state=state)
        travel_location = self.get_localized_value(key=location, state=state)
        self.save_variable(name=TRAVEL_LOCATION, value=travel_location, state=state)
        travel_type = ChatbotFlow.get_variable(state=state, name=TRAVEL_TYPE)
        self._estimate_cost(config, state, travel_type)
        self.send_predefined_response(key=OUTRO, state=state, config=config)

    def _estimate_cost(self, config: dict, state: State, travel_type: str):
        if is_value_in_table(key=TRAVEL_TYPE_ONE, value=travel_type, translation_table=self.translation_table):
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
        travel_type = self.get_variable(state=state, name=TRAVEL_TYPE)
        travel_type_single = self.get_localized_value(key=TRAVEL_TYPE_ONE, state=state)
        if travel_type == travel_type_single:
            self.send_predefined_response(key=TRAVEL_DURATION, state=state, config=config)
            return "travel_duration"
        self.send_buttons_response(key=TRAVEL_LOCATION, state=state, config=config)
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