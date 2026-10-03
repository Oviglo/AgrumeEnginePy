"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

entity.py: game graphical object

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .scene import Scene
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.math import Vector2
import pygame

class Entity(Sprite):
    def __init__(self, position: Vector2 = Vector2(0, 0), image_path: str = None, size: Vector2 = Vector2(16, 16)):
        super().__init__()
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            self.image = Surface(size)

        self.rect = self.image.get_frect()
        self.rect.topleft = position
        self.scene: Scene = None

    def draw(self, target: Surface) -> None:
        pass

    def update(self, delta: float) -> None:
        pass

    def set_scene(self, scene: Scene) -> None:
        self.scene = scene