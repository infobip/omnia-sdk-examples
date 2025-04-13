from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.constants import END
from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.langgraph.chatbot.chatbot_graph import (
    ChatbotFlow,
    State,
    )
from omnia_sdk.workflow.omnia_logging.omnia_logging import omnia_logger
from omnia_sdk.workflow.tools.channels.omni_channels import (
    ButtonDefinition,
    )
from omnia_sdk.workflow.tools.localization.translation_table import TranslationTable


class Foodie(ChatbotFlow):
    def __init__(self, checkpointer: BaseCheckpointSaver = None, configuration: ChatbotConfiguration = None,
                 translation_table: TranslationTable = None):
        super().__init__(checkpointer=checkpointer, configuration=configuration, translation_table=translation_table)

    def start(self, state: State, config: dict):
        omnia_logger.info(f"User message: {self.get_user_message_text(state=state)}")
        self.send_text_response(text="Hello, I am Foodie, your food assistant. I can help you with food recommendations", state=state,
                                config=config)
        self.send_buttons_response("Choose your favorite food",
                                   buttons=[ButtonDefinition(type="REPLY", text="Pizza", postback_data="pizza"),
                                            ButtonDefinition(type="REPLY", text="Sushi", postback_data="sushi"),
                                            ButtonDefinition(type="REPLY", text="Burger", postback_data="Burger")],
                                   state=state,
                                   config=config)

    def button_feedback(self, state: State, config: dict):
        postback = self.wait_user_input(state=state, config=config)
        self.send_text_response(text=f"Great choice! You chose {postback}", state=state, config=config)

    def _nodes(self):
        self.add_node("start", self.start)
        self.add_node("button_feedback", self.button_feedback)
        self.create_entry_point(start_node="start")

    def _transitions(self):
        self.add_edge("start", "button_feedback")
        self.add_edge("button_feedback", END)
