from omnia_sdk_examples.chatbot.laqo.entity_extraction import WORLD, EUROPE


def calculate_multiple_trip(location: str, **kwargs):
    return round(61.27 * 0.95, 2) if location == WORLD else round(53.28 * 0.95, 2)


def calculate_single_trip(location: str, travel_duration: int, **kwargs) -> float:
    coefficients = {WORLD: [3.13, 2.67, 2.14, 1.78, 1.69], EUROPE: [2.72, 2.32, 1.86, 1.55, 1.47]}

    if 1 <= travel_duration <= 3:
        cijena = coefficients[location][0] * travel_duration * 0.95
    elif 4 <= travel_duration <= 6:
        cijena = coefficients[location][1] * travel_duration * 0.95
    elif 7 <= travel_duration <= 15:
        cijena = coefficients[location][2] * travel_duration * 0.95
    elif 16 <= travel_duration <= 22:
        cijena = coefficients[location][3] * travel_duration * 0.95
    else:
        cijena = coefficients[location][4] * travel_duration * 0.95

    return round(cijena, 2)
