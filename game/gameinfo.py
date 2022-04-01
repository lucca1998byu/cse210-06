from asyncio import constants
import time
import pygame
import math
import game.constants
from game.scale import ScaleImg
from game.utils import blit_rotate_center, blit_text_center
pygame.font.init()
from game.playercar import PlayerCar
from game.computercar import ComputerCar
from game.abstractcar import AbstractCar


#this class sets the velocity, time and level information in the window
class GameInfo():
    LEVELS = 10
    

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = time.time()

    def get_level_time(self):
        if not self.started:
            return 0
        return round(time.time() - self.level_start_time)
