import MetaTrader5 as mt5
from types.bot_settings_type import BotSettings

# pyright: reportGeneralTypeIssues=true


def initialize_mt5(settings: BotSettings) -> None:
    if not mt5.initialize(  # type: ignore
        path=settings["mt5"]["path"],
        login=settings["mt5"]["login"],
        password=settings["mt5"]["password"],
        server=settings["mt5"]["server"],
        timeout=settings["mt5"]["timeout"],
        portable=settings["mt5"]["portable"]
    ):
        print("failed to initialize metatrader account, probably bad credentials, error code =",
              mt5.last_error())  # type: ignore
        mt5.shutdown()  # type: ignore
        quit()


def connect_to_mt5(settings: BotSettings) -> None:
    if not mt5.login(  # type: ignore
        login=settings["mt5"]["login"],
        password=settings["mt5"]["password"],
        server=settings["mt5"]["server"],
        timeout=settings["mt5"]["timeout"],
        portable=settings["mt5"]["portable"]
    ):
        print("failed to connect to metatrader account, error code =",
              mt5.last_error())  # type: ignore
        mt5.shutdown()  # type: ignore
        quit()
