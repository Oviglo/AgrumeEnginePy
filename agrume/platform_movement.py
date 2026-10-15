"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

platform_movement.py: Plateforme movement

"""

from .movement import Movement
from pygame.math import lerp

class PlatformMovement(Movement):
    LEFT = "left"
    RIGHT = "right"
    JUMP = "jump"
    
    def __init__(self):
        super().__init__()
        self.max_speed: float = 100.0
        self.input_map = {"left": self.LEFT, "right": self.RIGHT, "jump": self.JUMP}
        self.acceleration: float = 1
        self.deceleration: float = 0.1

        self.gravity_force: float = 10

    def update(self, delta: float) -> None:
        if not self.entity:
            return

        scene = self.entity.scene
        if not scene:
            return

        self.direction.x = 0
        input = self.entity.scene.agrume.input
        if input.is_active(self.input_map["left"]):
            self.set_direction_x(-1)
        if input.is_active(self.input_map['right']):
            self.set_direction_x(1)
        if input.is_active(self.input_map['jump']):
            self.jump()

        self.velocity.y = max(-self.gravity_force, min(self.gravity_force, (self.velocity.y + 0.1) * scene.gravity.y))
        speed: float = self.max_speed / 10
        target_velocity = self.direction.x * speed
        acceleration_factor = self.acceleration if self.direction.x != 0 else self.deceleration
        self.velocity.x = lerp(self.velocity.x, target_velocity, acceleration_factor * delta)

        # Update position and test collision
        self.entity.hitbox_rect.x += self.velocity.x
        self.handle_collision("x")
        self.entity.hitbox_rect.y += self.velocity.y
        self.handle_collision("y")
        
        self.entity.rect.center = self.entity.hitbox_rect.center

    def handle_collision(self, direction: str) -> None:
        for entity in self.collide_entities:
            collide_rects = entity.get_collide_rects(self.entity.hitbox_rect)

            for collide_rect in collide_rects:
                if collide_rect:
                    if direction == "x":
                        if self.velocity.x > 0: 
                            self.entity.hitbox_rect.right = collide_rect.left
                        if self.velocity.x < 0:
                            self.entity.hitbox_rect.left = collide_rect.right

                        self.velocity.x = 0
                    else:
                        if self.velocity.y < 0: 
                            self.entity.hitbox_rect.top = collide_rect.bottom
                        if self.velocity.y > 0:
                            self.entity.hitbox_rect.bottom = collide_rect.top

                        self.velocity.y = 0

    def is_move(self) -> bool:
        return abs(self.velocity.x) > 1 or abs(self.velocity.y) > 1

    def jump(self) -> None:
        self.velocity.y = -4
