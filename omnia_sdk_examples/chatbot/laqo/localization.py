HR = "hr"
EN = "en"
TRAVEL_INTRO = "travel_intro"
TRAVEL_TYPE = "travel_type"
TRAVEL_DURATION = "travel_duration"
TRAVEL_LOCATION = "travel_location"
SINGLE_OFFER = "single_offer"
MULTIPLE_OFFER = "multiple_offer"
TRAVEL_TYPE_ONE = "travel_type_one"
OUTRO = "outro"
EUROPE = "europe"
WORLD = "world"
BUTTONS = "buttons"
MESSAGE = "message"

translation_table = {
    TRAVEL_INTRO: {
        HR: "Baš mi je drago da putuješ! Za izračun ponude putnog osiguranja treba mi nekoliko informacija o putovanju.",
        EN: "I'm so glad you're traveling! To calculate a travel insurance quote, I need some information about the trip.",
    },
    TRAVEL_TYPE: {
        HR: {MESSAGE: "Želiš osiguranje za samo jedno putovanje ili planiraš više putovanja u godini dana?", BUTTONS: ["Jedno", "Više"]},
        EN: {
            MESSAGE: "Do you want insurance for just one trip or are you planning several trips in a year?",
            BUTTONS: ["Single", "Multiple"],
        },
    },
    TRAVEL_DURATION: {
        HR: "Hvala ti! Koliko dana traje tvoje putovanje? Upiši broj od 1 do 30.",
        EN: "Thank you! How many days does your trip last? Enter a number from 1 to 30.",
    },
    TRAVEL_LOCATION: {
        HR: {MESSAGE: "Super! Gdje putuješ? Putovanje je u Europi ili ideš negdje drugdje u svijetu?", BUTTONS: ["Europa", "Svijet"]},
        EN: {
            MESSAGE: "Great! Where are you traveling? Is the trip in Europe or are you going somewhere else in the world?",
            BUTTONS: ["Europe", "World"],
        },
    },
    SINGLE_OFFER: {
        HR: """Odlično! Imam sve potrebne informacije za izračun osnovne cijene putnog osiguranja za 1 osobu:
            Tip putovanja: {travel_type}
            Trajanje putovanja u danima: {travel_duration}
            Mjesto putovanja: {travel_location}

            Informativan izračun: *{cost}*
            """,
        EN: """Great! I have all the necessary information to calculate the basic price of travel insurance for 1 person:
            Type of travel: {travel_type}
            Duration of the trip in days: {travel_duration}
            Travel location: {travel_location}

            Informative calculation: *{cost}*
            """,
    },
    MULTIPLE_OFFER: {
        HR: """Odlično! Imam sve potrebne informacije za izračun osnovne cijene putnog osiguranja za 1 osobu:
            Tip putovanja: {travel_type}
            Mjesto putovanja: {travel_location}

            Informativan izračun: *{cost}*
            """,
        EN: """Great! I have all the necessary information to calculate the basic price of travel insurance for 1 person:
            Type of travel: {travel_type}
            Travel location: {travel_location}

            Informative calculation: *{cost}*
            """,
    },
    OUTRO: {
        HR: "Putovanja su uzbudljiva, ali ne čekaj s odlukom o kupnji osiguranja. Provjeri dodatna pokrića i trenutnu promociju.\n https://kupi.laqo.hr/putno/putovanje",
        EN: "Travel is exciting, but don't wait to buy insurance. Check out additional coverage and the current promotion.\n https://kupi.laqo.hr/putno/put",
    },
    TRAVEL_TYPE_ONE: {HR: "Jedno", EN: "Single"},
    EUROPE: {HR: "Europa", EN: "Europe"},
    WORLD: {HR: "Svijet", EN: "World"},
}
