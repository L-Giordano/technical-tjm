import os
import sys


class Settings:
    RESOURCE_FORLDER = os.path.dirname(os.path.abspath(sys.argv[0])) + "/resource"
    SEARCH_BTN = RESOURCE_FORLDER + "/lupa.png"
    FOLDER_BTN = RESOURCE_FORLDER + "/folder.png"
    ICON_BTN = RESOURCE_FORLDER + "/icons.png"
    LIST_BTN = RESOURCE_FORLDER + "/list.png"
    COLUMN_BTN = RESOURCE_FORLDER + "/columns.png"
    BTNS = [COLUMN_BTN, ICON_BTN, LIST_BTN]
    ICON_OPTION = RESOURCE_FORLDER + "/colums.png"
    SAVE = RESOURCE_FORLDER + "/save.png"
    TIME_SLEEP = 0.2
    INTERVAL = 0.1
    POST_AMOUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    DOCUMENT_NAME = "post_"
    API_URL = "https://jsonplaceholder.typicode.com/posts/"
