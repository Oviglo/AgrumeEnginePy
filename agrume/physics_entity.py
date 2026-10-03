"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

physic_entity.py: entity subjected to scene gravity

"""

from .entity import Entity
from pygame.math import Vector2
from pygame import FRect

class PhysicEntity(Entity):
    def __init__(self, position: Vector2 = Vector2(0, 0), image_path: str = None, size: Vector2 = Vector2(16, 16)):
            super().__init__(position, image_path, size)
            self.velocity: Vector2 = Vector2(0.0, 0.0)
            self.collision_box: FRect = FRect(self.rect)

    def update(self, delta: float) -> None:
        if not self.scene:
            return
        
        # Add scene gravity
        gravity: Vector2 = self.scene.gravity
        self.velocity += gravity
        self.rect.center += self.velocity

    def stop(self) -> None:
        self.velocity *= 0

    def bounce_y(self) -> None:
        self.velocity.y *= -1

    def bounce_x(self) -> None:
        self.velocity.x *= -1