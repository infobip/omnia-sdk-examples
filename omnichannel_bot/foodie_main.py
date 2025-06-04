import logging as log

from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.chatbot.chatbot_state import Message
from omnia_sdk.workflow.chatbot.constants import (
    CONFIGURABLE,
    PAYLOAD,
    TEXT,
    TYPE,
    USER,
    BUTTON_REPLY,
)
from omnia_sdk.workflow.tools.channels.omni_channels import CONSOLE

from omnichannel_bot.graph import Foodie

if __name__ == "__main__":
    log.getLogger("root").setLevel(log.INFO)
    chatbot_configuration = ChatbotConfiguration.from_yaml("chatbot_configuration.yaml")
    config = {CONFIGURABLE: {"thread_id": "1234", "channel": CONSOLE}}
    foodie = Foodie(configuration=chatbot_configuration)

    # welcome message sent by the user
    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "Hi"})
    foodie.run(message=message, config=config)
    # here we simulate button press event from the user with OmniChannel API
    message = Message(role=USER, content={TYPE: BUTTON_REPLY, TEXT: "Sushi", PAYLOAD: "sushi"})
    foodie.run(message=message, config=config)
