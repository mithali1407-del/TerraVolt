import random


def sensor_data():

    solar = round(
        random.uniform(20, 50),
        2
    )

    battery = round(
        random.uniform(40, 100),
        2
    )

    load = round(
        random.uniform(10, 40),
        2
    )

    weather = random.choice(
        [
            "Sunny",
            "Cloudy",
            "Rainy"
        ]
    )

    temperature = round(
        random.uniform(20, 40),
        1
    )

    return (
        solar,
        battery,
        load,
        weather,
        temperature
    )