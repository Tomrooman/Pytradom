# pyright: reportMissingImports=false

import json
import os
import MetaTrader5 as mt5  # type: ignore


def get_settings():
    if (os.path.exists(os.path.join(os.path.dirname(__file__), 'bot.settings.json')) == False):
        raise ImportError('No bot.settings.json file found')

    with open(os.path.join(os.path.dirname(__file__), 'bot.settings.json')) as f:
        settings = json.load(f)
        return settings


def main():
    settings = get_settings()
    print("Main function")
    print(settings["bot"]["name"])


if __name__ == "__main__":
    main()
