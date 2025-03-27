from omnia_sdk.workflow.tools.ai.llm_models import IntentInstruction
from omnia_sdk.workflow.tools.ai.prompts.chat import detect_intent

intents = ["agent", "chatbot", "sales", "travel"]

intent_prompt = """
- Question: ##{message}##
- Help me classify question in one of the categories.
"""

intent_system_message = f"""
LAQO is digital insurance that offers compulsory vehicle insurance, comprehensive insurance, travel insurance and pet insurance.
- Help me classify user questions for LAQO insurance into one of the categories: {intents}.
- Examples:

-- agent category:
* [the user wants to contact an agent or wants the agent to contact him,  the user is complaining about the quality of 
the response, the application is not working for the user].

-- sales category:
* [the user has a question about prices / offer of comprehensive or compulsory insurance, how much does insurance cost]

-- travel category:
* [the user wants to know the price of travel insurance, inquiry about the travel insurance]

-- chatbot category:
* [user greeting: hi, hey, hey, hello, greeting, regards, good day, hello, ..., product information, 
which insurance you offer, what is Laqo]

- The user question you need to classify will be separated with: ##.
- Your answer must be in a valid JSON format, with the key: category, and the value is one of the categories defined above.
"""


def detect_laqo_intent(config: dict, message: str) -> str:
    intent_instruction = IntentInstruction(
        prompt=intent_prompt.format(message=message), intents=intents, user_message=message, system_message=intent_system_message
    )
    return detect_intent(config=config, intent_instruction=intent_instruction)
