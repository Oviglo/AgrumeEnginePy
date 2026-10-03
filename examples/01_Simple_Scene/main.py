"""
"""

import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agrume import Agrume
from agrume.scene import Scene
from agrume.entity import Entity
from pygame.math import Vector2

game = Agrume("Exemple 1: Simple Scene")
scene = Scene("main")
game.set_current_scene(scene)

# Settings object
entity = Entity((300, 150), None, (100, 100))
entity.image.fill("lightpink2")
scene.add_entity(entity)
scene.bg_color = "snow2"
direction: Vector2 = Vector2(1, 1)
speed = 4


def update(delta: float) -> None:
    entity.rect.center += (direction * speed)
    if entity.rect.top <= 0 or entity.rect.bottom >= scene.rect.bottom:
        direction.y *= -1

    if entity.rect.left <= 0 or entity.rect.right >= scene.rect.right:
        direction.x *= -1

game.run(update)
