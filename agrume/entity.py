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
    from .animation import Animation

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
        self.hitbox_rect = self.rect.inflate(0, 0)
        self.__scene: Scene = None
        self.__movement: Movement = None
        self.animations: dict[str, Animation] = {}
        self.current_animation: Animation|None = None
           

    def update(self, delta: float) -> None:
        if self.movement:
            self.movement.update(delta)
        if self.current_animation:
            self.current_animation.update(delta)
            self.image = self.current_animation.get_current_frame()

    @property
    def scene(self) -> Scene:
        return self.__scene

    @scene.setter
    def scene(self, scene: Scene) -> None:
        self.__scene = scene

    @property
    def movement(self) -> Movement | None:
        return self.__movement

    @movement.setter
    def movement(self, movement: Movement) -> None:
        movement.entity = self
        self.__movement = movement

    def add_animation(self, name: str, animation: Animation) -> None:
        self.animations[name] = animation

    def get_animation(self, name: str) -> Animation | None:
        if name in self.animations:
            return self.animations[name]

        return None

    def remove_animation(self, name: str) -> None:
        if name in self.animations:
            del self.animations[name]

    def set_current_animation(self, name: str) -> None:
        if name in self.animations:
            self.current_animation = self.animations[name]
