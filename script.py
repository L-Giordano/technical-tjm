import platform
import sys

from src.bot import Bot
from src.bot_utils.linux_utils import LinuxOsUtils
from src.bot_utils.macos_utils import MacOsUtils
from src.bot_utils.windows_utils import WindowsOsUtils

OS = {
    "Darwin": MacOsUtils,
    "Linux": LinuxOsUtils,
    "Windows": WindowsOsUtils,
}

if __name__ == '__main__':
    os_name = platform.system()
    try:
        utils = OS[os_name]() if os_name in OS.keys() else sys.exit("Error: OS not supported")
        bot = Bot(utils)
        bot.action()
    except Exception as e:
        sys.exit(e.args[0])
