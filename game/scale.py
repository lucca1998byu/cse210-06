#from msilib.schema import Class
import pygame


class ScaleImg:
    def scale_image(img, factor):
        size = round(img.get_width() * factor), round(img.get_height() * factor)
        return pygame.transform.scale(img, size)

