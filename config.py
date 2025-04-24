import os
import sys


class Settings:
    RESOURCE_FORLDER = os.path.dirname(os.path.abspath(sys.argv[0])) + "/resource"
    SEARCH_BTN = RESOURCE_FORLDER + "/search.png"
    FOLDER_BTN = RESOURCE_FORLDER + "/tjm.png"
    SAVE = RESOURCE_FORLDER + "/save_btn.png"
    TIME_SLEEP = 0.5
    INTERVAL = 0.1
    POST_AMOUNT = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    DOCUMENT_NAME = "post_"
    API_URL = "https://jsonplaceholder.typicode.com/posts/"
    SCREEN_CROP_FACTOR = 0.5
