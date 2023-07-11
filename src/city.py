import pygame
import numpy as np

from src.colors import MAXIMUM_GREEN
from src.settings import FL_N, FL_S, FL_E, FL_W


class City:
    def __init__(self, window: pygame.surface.Surface, name: str, population: int, lat: str, long: str) -> None:
        self.name = name
        self.population = population
        self.lat = float(lat)
        self.long = float(long)
        self.x = None
        self.y = None
        self.window = window
    
    def distance_from(self, other: 'City') -> float:
        return np.sqrt((abs(self.lat - other.lat) ** 2) + (abs(self.long - other.long) ** 2))
    
    def calculate_XY(self, image_start_x, image_start_y, image_height, image_width):
        self.x = (image_start_x + image_width)  - int((self.long  - FL_E) *  image_width / (FL_W - FL_E))
        self.y = (image_start_y + image_height) - int((self.lat - FL_S) * image_height / (FL_N - FL_S))
    
    def __repr__(self):
        return self.name + ": (" + str(self.lat) + ", " + str(self.long) + ")"
    
    def draw(self):
        pygame.draw.circle(self.window, MAXIMUM_GREEN, (self.x, self.y), 3)