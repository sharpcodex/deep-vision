from deep_vision import config


def log(msg: str):
    if config.SHOW_LOGS:
        print(msg)
