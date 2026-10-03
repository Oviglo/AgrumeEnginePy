"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

scene.py: game scene

"""
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.sprite import Group
from pygame.color import Color
from .entity import Entity

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .agrume import Agrume

class Scene:
    def __init__(self, name: str, size: Vector2 = (1280, 768)):
        self.size = size
        self.name = name
        self.surface: Surface = Surface(self.size)
        self.rect = self.surface.get_frect()
        self.bg_color: Color = Color("gray24")
        self.layers = []
        self.__agrume: Agrume = None

        # Environnement
        self.gravity: Vector2 = (0, 0)

    @property
    def agrume(self) -> Agrume:
        return self.__agrume

    @agrume.setter
    def agrume(self, agrume: Agrume) -> None:
        self.__agrume = agrume

    def draw(self, target: Surface) -> None:
        self.surface.fill(self.bg_color)

        # Draw all layers (groups of sprites)
        for layer in self.layers:
            layer.draw(self.surface)


        target.blit(self.surface)

    def update(self, delta: float) -> None:
        # Update all layers (groups of sprites)
        for layer in self.layers:
            layer.update(delta)

    def add_entity(self, entity: Entity, layer: int = 0) -> None:
        """ Add Entity object into the scene
            layer: layer number, if doesn't exist it will create
        """
        if not layer in self.layers:
            self.layers.append(Group())

        entity.scene = self
        entity.add(self.layers[0])
