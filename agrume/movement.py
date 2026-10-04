"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

movement.py: Movement base class

"""

from .input import Input
from pygame.math import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .entity import Entity

class Movement():
    def __init__(self):
        self.__input: Input = None
        self.__entity: Entity = None
        self.direction: Vector2 = Vector2(0, 0)
        self.velocity: Vector2 = Vector2(0, 0)

        # Collision
        self.collide_entities: list[Entity] = []

    def update(self, delta: float) -> None:
        pass

    @property
    def entity(self) -> Entity:
        return self.__entity

    @entity.setter
    def entity(self, entity: Entity) -> None:
        self.__entity = entity

    def stop(self):
        self.velocity = Vector2(0, 0)
