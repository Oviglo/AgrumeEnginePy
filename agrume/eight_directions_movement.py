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
from pygame.math import Vector2
from pygame import Rect

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .entity import Entity

class EightDirectionsMovement(Movement):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

    def __init__(self):
        super().__init__()
        self.max_speed: float = 100.0
        self.input_map = {"up": self.UP, "down": self.DOWN, "left": self.LEFT, "right": self.RIGHT}
        self.acceleration: float = 1
        self.deceleration: float = 0.15

    def update(self, delta: float) -> None:
        if not self.entity:
            return
        
        self.direction.x = 0
        self.direction.y = 0
        
        input = self.entity.scene.agrume.input
        if input.is_active(self.input_map["up"]):
            self.set_direction_y(-1)
        if input.is_active(self.input_map['down']):
            self.set_direction_y(1)
        if input.is_active(self.input_map["left"]):
            self.set_direction_x(-1)
        if input.is_active(self.input_map['right']):
            self.set_direction_x(1)

        normalized_direction: Vector2 = self.direction.normalize() if self.direction != Vector2(0, 0) else self.direction
        speed:float = self.max_speed / 10
        lerp_value: float = self.deceleration if normalized_direction == Vector2(0, 0) else self.acceleration
        self.velocity = self.velocity.lerp(normalized_direction * speed * delta, lerp_value)

        # Update position and test collision
        self.entity.hitbox_rect.x += self.velocity.x
        self.handle_collision("x")
        self.entity.hitbox_rect.y += self.velocity.y
        self.handle_collision("y")

        self.entity.rect.center = self.entity.hitbox_rect.center

        # Animation
        if self.entity.current_animation:
            animation = self.entity.current_animation
            if not self.is_move() and animation.is_play:
                animation.stop()
            elif self.is_move() and not animation.is_play:
                animation.play()

    def handle_collision(self, direction: str) -> None:
        for entity in self.collide_entities:
            collide_rects = entity.get_collide_rects(self.entity.hitbox_rect)

            for collide_rect in collide_rects:
                if collide_rect:
                    if direction == "x":
                        self.velocity.x = 0
                        if self.direction.x > 0: 
                            self.entity.hitbox_rect.right = collide_rect.left
                        if self.direction.x < 0:
                            self.entity.hitbox_rect.left = collide_rect.right
                    else:
                        self.velocity.y = 0
                        if self.direction.y < 0: 
                            self.entity.hitbox_rect.top = collide_rect.bottom
                        if self.direction.y > 0:
                            self.entity.hitbox_rect.bottom = collide_rect.top

    def is_move(self) -> bool:
        return abs(self.velocity.x) > 1 or abs(self.velocity.y) > 1
