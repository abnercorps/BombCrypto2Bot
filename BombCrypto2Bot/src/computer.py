import platform
class Computer:
    def reboot(self):
        if platform.system() == "Windows": 
            os.system("shutdown.exe -r -t 0")
        else:
            os.system("reboot")


