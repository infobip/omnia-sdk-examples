from omnia_sdk.workflow.tools.ai.prompts.chat import chat_completions

WORLD = "world"
EUROPE = "europe"

travel_location_system_message = f"""
- Help me extract the location from user's message.
- Location can be {EUROPE} or {WORLD}.
- User message will be delimited with **.
- location should be extracted in following format:
-- location: <{EUROPE}>
-- If there is no location in user's message, return location: <none>
- Examples:
-- I am planning to travel to Greece -> location: <{EUROPE}>
-- I am planning to travel to Paris -> location: <{EUROPE}>
-- I am planning to travel to USA -> location: <{WORLD}>
-- Želim sutra putovati u Španjolsku -> location: <{EUROPE}>
"""


def extract_location(message: str) -> str:
    completion = chat_completions(
        messages=[
            {"role": "system", "content": travel_location_system_message},
            {"role": "user", "content": f" User question: **{message}**"},
        ],
        extract_params=True,
    )
    return completion.model_extra["parsed_params"]["p1"]
