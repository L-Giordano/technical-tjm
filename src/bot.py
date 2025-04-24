from botcity.core import DesktopBot
import pyautogui as pg
import pyperclip as pc
import requests

from config import Settings
from src.bot_utils.os_utils import OSUtils


class Bot(DesktopBot):

    def __init__(self, utils: OSUtils):
        super().__init__()
        self.utils = utils

    def action(self, execution=None):
        for i in range(Settings.POST_AMOUNT):
            post_name = Settings.DOCUMENT_NAME + str(i+1)
            self.utils.create_new_document()
            post = self.__get_post_from_api(i+1)
            self.__write_post(post)
            self.utils.save_document(post_name)

    def __get_post_from_api(self, post_id: int):
        url = Settings.API_URL + str(post_id)
        response = requests.get(url)
        return response.json()

    def __write_post(bot, post):
        title = f"Title: {post['title']}\n\n"
        body = f"{post['body']}\n"
        pc.copy(title + body)
        pg.hotkey("command", "v", interval=Settings.INTERVAL)
