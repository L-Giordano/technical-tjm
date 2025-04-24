import os
import time

import pyautogui as pg
from pyautogui import ImageNotFoundException
import pyperclip as pc

from config import Settings
from src.bot_utils.os_utils import OSUtils
from src.error_handler.error_handler import retry_on_error


class MacOsUtils(OSUtils):

    def create_new_document(self) -> None:
        os.system("open -a TextEdit")
        pg.hotkey("command", "n", interval=Settings.INTERVAL)

    def save_document(self, document_name: str) -> None:
        pg.hotkey("command", "s", interval=Settings.INTERVAL)
        pc.copy(document_name)
        pg.hotkey("command", "v", interval=Settings.INTERVAL)

        self.__select_folder()
        time.sleep(Settings.TIME_SLEEP)

        self.__find_and_click(Settings.SAVE, clicks=1)

        pg.hotkey("command", "w", interval=Settings.INTERVAL)

    @retry_on_error(max_retries=3, delay=1, exceptions=ImageNotFoundException,)
    def __find_and_click(self, img_path: str, clicks: int) -> None:
        x, y = pg.locateCenterOnScreen(img_path, confidence=0.7)
        x = x * Settings.SCREEN_CROP_FACTOR
        y = y * Settings.SCREEN_CROP_FACTOR
        pg.click(clicks=clicks, x=x, y=y, interval=Settings.INTERVAL)

    def __select_folder(self) -> None:
        self.__find_and_click(img_path=Settings.SEARCH_BTN, clicks=1)
        pc.copy("tjm-proj")
        pg.hotkey("command", "v", interval=Settings.INTERVAL)
        time.sleep(Settings.TIME_SLEEP)
        self.__find_and_click(img_path=Settings.FOLDER_BTN, clicks=1)
        pg.press("enter")
