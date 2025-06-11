import logging as log

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.constants import END
from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.langgraph.chatbot.chatbot_graph import (
    ChatbotFlow,
    State,
)


class AnswersHybridFlow(ChatbotFlow):
    def __init__(
        self,
        checkpointer: BaseCheckpointSaver = None,
        configuration: ChatbotConfiguration = None,
        translation_table=None,
    ):
        super().__init__(checkpointer=checkpointer, configuration=configuration)

    def start(self, state: State, config: dict):
        log.info("Starting AnswersHybridFlow")
        metadata = ChatbotFlow.get_metadata(config)
        log.info(f"Metadata: {metadata}")
        if self._transfer_to_agent(state):
            return
        self.send_text_response(
            text="Hi, what is your name?", state=state, config=config
        )

    def collect_user_name(self, state: State, config: dict):
        log.info("Collecting user name")
        ChatbotFlow.wait_user_input(
            state=state, config=config, variable_name="user_name"
        )
        if self._transfer_to_agent(state):
            return
        user_name = self.get_variable(state=state, name="user_name")
        self.send_text_response(
            text=f"Hello, nice to meet you {user_name}! What is your email",
            state=state,
            config=config,
        )

    def collect_user_email(self, state: State, config: dict):
        log.info("Collecting user email")
        ChatbotFlow.wait_user_input(
            state=state, config=config, variable_name="user_email"
        )
        if self._transfer_to_agent(state):
            return
        self.send_text_response(text="Thank you", state=state, config=config)
        answers_state = {
            "user_name": self.get_variable(state=state, name="user_name"),
            "user_email": self.get_variable(state=state, name="user_email"),
        }
        ChatbotFlow.return_to_answers(state=answers_state)
        log.info("Workflow completed successfully")

    def _transfer_to_agent(self, state: State) -> bool:
        message = ChatbotFlow.get_last_message(state=state)
        if "agent" in message.get_text().lower():
            log.info("Transferring to agent")
            answers_state = {
                "agent": True,
            }
            ChatbotFlow.return_to_answers(state=answers_state)
            return True
        return False

    def _transitions(self) -> None:
        self.add_edge("start", "collect_user_name")
        self.add_edge("collect_user_name", "collect_user_email")
        self.add_edge("collect_user_email", END)

    def _nodes(self) -> None:
        self.add_node("start", self.start)
        self.add_node("collect_user_name", self.collect_user_name)
        self.add_node("collect_user_email", self.collect_user_email)
        self.create_entry_point(start_node="start")
