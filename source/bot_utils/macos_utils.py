import os
import time

import pyautogui as pg
from pyautogui import ImageNotFoundException
import pyperclip as pc

from config import Settings
from source.bot_utils.os_utils import OSUtils


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

    def __find_and_click(self, img_path: str, clicks: int) -> None:
        x, y = pg.locateCenterOnScreen(img_path, confidence=0.7)
        pg.click(clicks=clicks, x=x/2, y=y/2, interval=Settings.INTERVAL)

    def __select_folder(self) -> None:
        self.__find_and_click(img_path=Settings.SEARCH_BTN, clicks=1)
        pc.copy("tjm-proj")
        pg.hotkey("command", "v", interval=Settings.INTERVAL)
        time.sleep(Settings.TIME_SLEEP)

        self.__find_and_click_format_btn()
        self.__find_and_click(img_path=Settings.ICON_OPTION, clicks=1)
        self.__find_and_click(img_path=Settings.FOLDER_BTN, clicks=2)

    def __find_and_click_format_btn(self) -> None:
        for btn in Settings.BTNS:
            try:
                self.__find_and_click(img_path=btn, clicks=1)
                return
            except ImageNotFoundException:
                continue
        raise Exception
