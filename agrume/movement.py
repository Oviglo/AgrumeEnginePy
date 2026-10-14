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
        self.__direction: Vector2 = Vector2(0, 0)
        self.velocity: Vector2 = Vector2(0, 0)

        # Collision
        self.collide_entities: list[Entity] = []

        # Callbacks
        self.__on_direction_change: function|None = None

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

    @property
    def direction(self) -> Vector2:
        return self.__direction

    @direction.setter
    def direction(self, direction: Vector2) -> None:
        self.__direction = direction
        if self.__on_direction_change:
            self.__on_direction_change(self.direction)

    def set_direction_x(self, x: int) -> None:
        if int(self.direction.x) == x:
            return
        
        self.direction = Vector2(x, self.direction.y)

    def set_direction_y(self, y: int) -> None:
        if int(self.direction.y) == y:
            return
        
        self.direction = Vector2(self.direction.x, y)

    @property
    def on_direction_change(self) -> function|None:
        return self.__on_direction_change

    @on_direction_change.setter
    def on_direction_change(self, callback: function) -> None:
        self.__on_direction_change = callback
