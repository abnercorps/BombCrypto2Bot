
from colorama import init, Fore, Style

from src.application import Application
from src.log import Log
from src.multi_account import MultiAccount

from src.services.telegram import Telegram

import sys

init()

banner = """
*******************************************************************************
** BOMBCRYPTO2 - BOT
**
** Please consider to buy me a coffee :)
** MATIC:       0x9d9fa1ce36f3d21d81e14a0a9ea22a069f0e77f1
** BITCOIN BSC: 0x9d9fa1ce36f3d21d81e14a0a9ea22a069f0e77f1 
** PIX:         9fe608c8-1594-469a-ae58-124a9de40a97
*******************************************************************************
** Press CTRL + C to kill the bot.
** Some configs can be found in the https://github.com/pbiajoni/BombCrypto2Bot
*******************************************************************************"""

print(Fore.GREEN + banner + Style.RESET_ALL)

application = Application()
log = Log()
multi_account = MultiAccount()
telegram = Telegram()


def main():
    application.start()
    telegram.start()
    multi_account.start()


def onlyMap():
    application.start()
    telegram.start()
    multi_account.startOnlyMapAction()


if __name__ == '__main__':
    try:
        if 'only-map' in sys.argv:
            onlyMap()
        else:
            main()
    except KeyboardInterrupt:
        log.console('Shutting down the bot',
                    services=True, emoji='😓', color='red')
        telegram.stop()
        exit()
