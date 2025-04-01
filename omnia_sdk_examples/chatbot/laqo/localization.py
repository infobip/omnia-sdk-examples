HR = "hr"
EN = "en"
TRAVEL_INTRO = "travel_intro"
TRAVEL_TYPE = "travel_type"
TRAVEL_DURATION = "travel_duration"
TRAVEL_LOCATION = "travel_location"
SINGLE_OFFER = "single_offer"
MULTIPLE_OFFER = "multiple_offer"
OUTRO = "outro"
EUROPE = "europe"
WORLD = "world"
BUTTONS = "buttons"
MESSAGE = "message"
SINGLE = "single"
MULTIPLE = "multiple"

translation_table_cpaas = {
    TRAVEL_INTRO: {
        HR: {
            "body": {
                "text": "Baš mi je drago da putuješ! Za izračun ponude putnog osiguranja treba mi nekoliko informacija o putovanju.",
                "type": "TEXT",
                }
            },
        EN: {
            "body": {
                "text": "I'm so glad you're traveling! To calculate a travel insurance quote, I need some information about the trip.",
                "type": "TEXT",
                }
            },
        },
    TRAVEL_TYPE: {
        HR: {
            "body": {
                "text": "Želiš osiguranje za samo jedno putovanje ili planiraš više putovanja u godini dana?",
                "type": "TEXT",
                },
            "buttons": [
                {"type": "REPLY", "text": "Jedno", "postbackData": "single"},
                {"type": "REPLY", "text": "Više", "postbackData": "multiple"},
                ],
            },
        EN: {
            "body": {
                "text": "Do you want insurance for just one trip or are you planning several trips in a year?",
                "type": "TEXT",
                },
            "buttons": [
                {"type": "REPLY", "text": "Single", "postbackData": "single"},
                {"type": "REPLY", "text": "Multiple", "postbackData": "multiple"},
                ],
            },
        },
    TRAVEL_DURATION: {
        HR: {
            "body": {
                "text": "Hvala ti! Koliko dana traje tvoje putovanje? Upiši broj od 1 do 30.",
                "type": "TEXT",
                }
            },
        EN: {
            "body": {
                "text": "Thank you! How many days does your trip last? Enter a number from 1 to 30.",
                "type": "TEXT",
                }
            },
        },
    TRAVEL_LOCATION: {
        HR: {
            "body": {
                "text": "Super! Gdje putuješ? Putovanje je u Europi ili ideš negdje drugdje u svijetu?",
                "type": "TEXT",
                },
            "buttons": [
                {"type": "REPLY", "text": "Europa", "postbackData": "europe"},
                {"type": "REPLY", "text": "Svijet", "postbackData": "world"},
                ],
            },
        EN: {
            "body": {
                "text": "Great! Where are you traveling? Is the trip in Europe or are you going somewhere else in the world?",
                "type": "TEXT",
                },
            "buttons": [
                {"type": "REPLY", "text": "Europe", "postbackData": "europe"},
                {"type": "REPLY", "text": "World", "postbackData": "world"},
                ],
            },
        },
    SINGLE_OFFER: {
        HR: {
            "body": {
                "text": """Odlično! Imam sve potrebne informacije za izračun osnovne cijene putnog osiguranja za 1 osobu:
Tip putovanja: {localized_num_trips}
Trajanje putovanja u danima: {travel_duration}
Mjesto putovanja: {localized_location}
Informativan izračun: *{cost}*""",
                "type": "TEXT",
                }
            },
        EN: {
            "body": {
                "text": """Great! I have all the necessary information to calculate the basic price of travel insurance for 1 person:
Type of travel: {localized_num_trips}
Duration of the trip in days: {travel_duration}
Travel location: {localized_location}
Informative calculation: *{cost}*""",
                "type": "TEXT",
                }
            },
        },
    MULTIPLE_OFFER: {
        HR: {
            "body": {
                "text": """Odlično! Imam sve potrebne informacije za izračun osnovne cijene putnog osiguranja za 1 osobu:
Tip putovanja: {localized_num_trips}
Mjesto putovanja: {localized_location}
Informativan izračun: *{cost}*""",
                "type": "TEXT",
                }
            },
        EN: {
            "body": {
                "text": """Great! I have all the necessary information to calculate the basic price of travel insurance for 1 person:
Type of travel: {localized_num_trips}
Travel location: {localized_location}
Informative calculation: *{cost}*""",
                "type": "TEXT",
                }
            },
        },
    OUTRO: {
        HR: {
            "body": {
                "text": "Putovanja su uzbudljiva, ali ne čekaj s odlukom o kupnji osiguranja. Provjeri dodatna pokrića i trenutnu promociju.\n https://kupi.laqo.hr/putno/putovanje",
                "type": "TEXT",
                }
            },
        EN: {
            "body": {
                "text": "Travel is exciting, but don't wait to buy insurance. Check out additional coverage and the current promotion.\n https://kupi.laqo.hr/putno/put",
                "type": "TEXT",
                }
            },
        },
    }

translation_table_constants = {
    EUROPE: {
        HR: "Europa",
        EN: "Europe",
        },
    WORLD: {
        HR: "Svijet",
        EN: "World",
        },
    SINGLE: {
        HR: "Jedno",
        EN: "Single",
        },
    MULTIPLE: {
        HR: "Više",
        EN: "Multiple",
        },
    }
