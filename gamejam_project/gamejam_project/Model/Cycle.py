import pygame
import random


class Cycle:

    def __init__(self, day, night):
        self.day = day
        self.night = night

    def cycleChange(self):
        if self.day:
            self.day = False
            self.night = True
        else:
            self.day = True
            self.night = False

    def getCycle(self) ->str:
        if self.day:
            return "day"
        else:
            return "night"

    def isCycle(self, cycle) ->bool:
        return cycle == "day" and self.day or cycle == "night" and self.night
