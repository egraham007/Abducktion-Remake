import os
from colorama import Fore, Style
import random

class Duck:
    myduck = ' '
    def __init__(self):
        self.ducklist = ["B", "Y", "P", "W"]
        random.shuffle(self.ducklist)
        self.myduck = self.ducklist[0]


    def __str__(self):
        if self.myduck == "B":
            return f"{Fore.BLUE}"+self.myduck+ f"{Style.RESET_ALL}"
        if self.myduck == "Y":
            return f"{Fore.LIGHTYELLOW_EX}"+self.myduck+ f"{Style.RESET_ALL}"
        if self.myduck == "P":
            return f"{Fore.LIGHTMAGENTA_EX}" + self.myduck + f"{Style.RESET_ALL}"
        return self.myduck

    def __repr__(self):
        return self.__str__()

    def getColor(self):
        return self.myduck