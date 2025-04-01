from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.chatbot.chatbot_state import Message
from omnia_sdk.workflow.chatbot.constants import CONFIGURABLE, PAYLOAD, TEXT, TYPE, USER
from omnia_sdk.workflow.tools.channels.omni_channels import BUTTON_REPLY
from omnia_sdk.workflow.tools.localization.cpaas_translation_table import (
    CPaaSTranslationTable,
    )

from omnia_sdk_examples.chatbot.laqo.laqo_graph import Pavle
from omnia_sdk_examples.chatbot.laqo.localization import (
    translation_table_constants,
    translation_table_cpaas,
    )

if __name__ == "__main__":
    chatbot_configuration = ChatbotConfiguration(default_language="en")
    config = {
        CONFIGURABLE: {
            "thread_id": "123",
            "channel": "CONSOLE",
            }
        }
    translation_table = CPaaSTranslationTable(translation_table_cpaas=translation_table_cpaas,
                                              translation_table_constants=translation_table_constants)
    pavle = Pavle(configuration=chatbot_configuration, translation_table=translation_table)

    # ----- Chatbot -----
    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "What insurances you offer"})
    pavle.run(message=message, config=config)

    # ----- Travel insurance-----
    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "Can you give me an offer for travel insurance"})
    pavle.run(message=message, config=config)

    message = Message(role=USER, content={TYPE: BUTTON_REPLY, TEXT: "Single", PAYLOAD: "single"})
    pavle.run(message=message, config=config)

    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "8"})
    pavle.run(message=message, config=config)

    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "I want to travel to Turkey"})
    pavle.run(message=message, config=config)
