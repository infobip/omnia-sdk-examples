import logging as log
from langgraph.constants import END

from omnia_sdk.workflow.langgraph.chatbot.chatbot_graph import ChatbotFlow, State
from omnia_sdk.workflow.tools.channels.omni_channels import ButtonDefinition



class Foodie(ChatbotFlow):

    def start(self, state: State, config: dict):
        log.info(f"User message: {self.get_user_message(state=state).get_text()}")
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
