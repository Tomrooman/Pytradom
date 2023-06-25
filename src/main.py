import json
import os
import mt5_lib
from types.bot_settings_type import BotSettings
# import time


def get_settings(file_name: str) -> BotSettings:
    if (os.path.exists(path=os.path.join(os.path.dirname(p=__file__), file_name)) == False):
        raise ImportError('No {file_name} file found')

    with open(file=os.path.join(os.path.dirname(p=__file__), file_name)) as f:
        settings: BotSettings = json.load(fp=f)
        return settings


def main() -> None:
    settings: BotSettings = get_settings(file_name='bot.settings.json')
    print("Main function")
    mt5_lib.initialize_mt5(settings=settings)
    mt5_lib.connect_to_mt5(settings=settings)
    print("End of main function")


if __name__ == "__main__":
    main()
