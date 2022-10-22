from argparse import Action
import platform
import os

class Computer:
    def __init__(self):
        from src.log import Log
        from src.actions import Actions
        self.log = Log()
        self.actions = Actions()

    def reboot(self):
        if platform.system() == "Windows":
            self.log.console('Rebooting Windows',
                         services=True, emoji='📄')
            self.actions.sleep(5, 5, forceTime=True)
            os.system("shutdown.exe -r -t 0")
        else:
            self.log.console('Rebooting Linux',
                         services=True, emoji='📄')
            self.actions.sleep(5, 5, forceTime=True)
            os.system("reboot")


