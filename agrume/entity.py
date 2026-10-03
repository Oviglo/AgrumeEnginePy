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
    from .movement import Movement

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
            self.image = Surface(size, pygame.HWSURFACE)

        self.rect = self.image.get_frect()
        self.rect.topleft = position
        self.__scene: Scene = None
        self.__movement: Movement = None

    def draw(self, target: Surface) -> None:
        pass

    def update(self, delta: float) -> None:
        if self.movement:
            self.movement.update(delta)

    @property
    def scene(self) -> Scene:
        return self.__scene

    @scene.setter
    def scene(self, scene: Scene) -> None:
        self.__scene = scene

    @property
    def movement(self) -> Movement:
        return self.__movement

    @movement.setter
    def movement(self, movement: Movement) -> None:
        movement.entity = self
        self.__movement = movement