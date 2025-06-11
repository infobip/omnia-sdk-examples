import logging as log

import yaml
from omnia_sdk.workflow.chatbot.chatbot_configuration import ChatbotConfiguration
from omnia_sdk.workflow.chatbot.chatbot_state import Message
from omnia_sdk.workflow.chatbot.constants import CONFIGURABLE, TEXT, TYPE, USER
from omnia_sdk.workflow.tools.answers._context import get_workflow_state

from answers_hybrid_bot.graph import AnswersHybridFlow

if __name__ == "__main__":
    log.getLogger("root").setLevel(log.INFO)
    chatbot_configuration = ChatbotConfiguration.from_yaml(
        "answers_hybrid_bot/chatbot_configuration.yaml"
    )
    build_configuration_dict = yaml.safe_load(
        open("answers_hybrid_bot/build.yaml", "rb").read()
    )

    config = {
        CONFIGURABLE: {
            "thread_id": "123",
            "channel": "CONSOLE",
        }
    }

    flow = AnswersHybridFlow(configuration=chatbot_configuration)

    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "hi"})
    flow.run(message=message, config=config)

    message = Message(role=USER, content={TYPE: TEXT.upper(), TEXT: "John Smith"})
    flow.run(message=message, config=config)

    message = Message(
        role=USER, content={TYPE: TEXT.upper(), TEXT: "john.smith@mail.com"}
    )
    flow.run(message=message, config=config)

    state = get_workflow_state()
    print(f"Final state: {state}")
