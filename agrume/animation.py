"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

animation.py: Animation manager for entities

"""

from pygame.math import Vector2
from pygame.surface import Surface
import pygame

class Animation:
    def __init__(self, image_path: str, speed: float = 1.0, spritesheet_size: Vector2 = None):
        self.surface: Surface = pygame.image.load(image_path).convert_alpha()
        if not spritesheet_size:
            spritesheet_size = Vector2(self.surface.get_rect().w, self.surface.get_rect().h)

        self.spritesheet_size = spritesheet_size
        self.speed = speed
        self.is_play: bool = True
        self.current_frame = 0

    def update(self) -> None:
        pass

    def draw(self, target: Surface) -> None:
        pass

    def play(self) -> None:
        self.current_frame = 0
        self.is_play = True

    def stop(self) -> None:
        self.is_play = False
        self.current_frame = 0

    def pause(self) -> None:
        self.is_play = False

    def resume(self) -> None:
        self.is_play = True
