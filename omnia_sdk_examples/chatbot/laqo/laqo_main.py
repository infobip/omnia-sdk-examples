import logging

from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.chatbot.chatbot_state import Message
from omnia_sdk.workflow.chatbot.constants import CONFIGURABLE
from omnia_sdk.workflow.logging.logging import omnia_logger

from omnia_sdk_examples.chatbot.laqo.laqo_graph import Pavle
from omnia_sdk_examples.chatbot.laqo.localization import translation_table

omnia_logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    chatbot_configuration = ChatbotConfiguration(default_language="en")
    config = {
            CONFIGURABLE: {
                "thread_id": "123",
                "channel": "WHATSAPP",
                "business_number": "Test_Business_Number",
                "end_user_number":  "Test_User_Number"
            }
        }
    pavle = Pavle(configuration=chatbot_configuration, translation_table=translation_table)

    # ----- Chatbot -----
    message = Message(role="user", content={"type": "text", "payload": "What can you help me with?"})
    pavle.run(message=message, config=config)

    # ----- Travel insurance-----
    message = Message(role="user", content={"type": "text", "payload": "Give me travel insurance"})
    pavle.run(message=message, config=config)

    message = Message(role="user", content={"type": "text", "payload": "Single"})
    pavle.run(message=message, config=config)

    message = Message(role="user", content={"type": "text", "payload": "7"})
    pavle.run(message=message, config=config)

    message = Message(role="user", content={"type": "text", "payload": "Would like to go to Spain"})
    pavle.run(message=message, config=config)