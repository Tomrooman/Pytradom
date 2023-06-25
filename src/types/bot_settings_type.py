from typing import TypedDict


class Mt5Settings(TypedDict):
    path: str
    login: int
    password: str
    server: str
    timeout: int
    portable: bool


class BotSettings(TypedDict):
    mt5: Mt5Settings
