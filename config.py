import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7606030800:AAGo6Ulo-9MlL3b1sqLjm-R5o82xSIIr9r8")

    APP_ID = int(os.environ.get("APP_ID", 20043878))

    API_HASH = os.environ.get("API_HASH", "763983cd61ad87ad673a9f83756e3d74")
