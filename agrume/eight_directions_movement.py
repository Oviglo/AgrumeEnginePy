"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

eight_directions_movement.py: 8 directions movement

"""
from .movement import Movement

class EightDirectionsMovement(Movement):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def __init__(self):
        self.max_speed: float = 100.0

    def update(self, delta: float) -> None:
        super().update(delta)

        if self.entity:
            input = self.entity.scene.agrume.input
            