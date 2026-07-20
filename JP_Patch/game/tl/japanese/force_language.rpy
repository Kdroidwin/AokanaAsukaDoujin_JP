# Make the Japanese translation active as soon as the game starts.
init -1000 python:
    preferences.language = "japanese"
    if "custom_layer" not in config.layers:
        config.layers.append("custom_layer")
