def get_capital_city(country: str) -> str:
    """Returns the capital city of the given country."""
    capitals = {
        "france": "Paris",
        "japan": "Tokyo",
        "canada": "Ottawa",
        "germany": "Berlin",
        "india": "New Delhi",
    }
    return capitals.get(country.lower(), f"Sorry, I don't know the capital of {country}.")
