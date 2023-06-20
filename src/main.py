import json
import os
import MetaTrader5 as mt5
# import time


def get_settings(file_name: str):
    if (os.path.exists(os.path.join(os.path.dirname(__file__), file_name)) == False):
        raise ImportError('No {file_name} file found')

    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        settings = json.load(f)
        return settings


def initialize_mt5(settings):
    if not mt5.initialize(
        path=settings["mt5"]["path"],
            login=settings["mt5"]["login"],
            password=settings["mt5"]["password"],
            server=settings["mt5"]["server"],
            timeout=settings["mt5"]["timeout"],
            portable=settings["mt5"]["portable"]):
        print("initialize() failed, probably bad credentials, error code =",
              mt5.last_error())
        mt5.shutdown()
        quit()


def connect_to_mt5(settings):
    authorized = mt5.login(
        login=settings["mt5"]["login"],
        password=settings["mt5"]["password"],
        server=settings["mt5"]["server"],
        timeout=settings["mt5"]["timeout"],
        portable=settings["mt5"]["portable"]
    )
    if not authorized:
        print("failed to connect to metatrader account, error code =",
              mt5.last_error())
        mt5.shutdown()
        quit()


def main():
    settings = get_settings('bot.settings.json')
    print("Main function")
    initialize_mt5(settings)
    connect_to_mt5(settings)
    print("End of main function")


if __name__ == "__main__":
    main()
