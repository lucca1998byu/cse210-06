from asyncio import constants
import time
import pygame
import math
from game.scale import ScaleImg
from game.utils import blit_rotate_center, blit_text_center
pygame.font.init()

GRASS = ScaleImg.scale_image(pygame.image.load("image/grass.jpg"), 2.5)
TRACK = ScaleImg.scale_image(pygame.image.load("image/track.png"), 0.9)
TRACK_BORDER = ScaleImg.scale_image(pygame.image.load("image/track-border.png"), 0.9)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
FINISH = pygame.image.load("image/finish.png")
FINISH_MASK = pygame.mask.from_surface(FINISH)
FINISH_POSITION = (130, 250)
RED_CAR = ScaleImg.scale_image(pygame.image.load("image/red-car.png"), 0.55)
GREEN_CAR = ScaleImg.scale_image(pygame.image.load("image/green-car.png"), 0.55)
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")
MAIN_FONT = pygame.font.SysFont("comicsans", 44)
FPS = 60
PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]