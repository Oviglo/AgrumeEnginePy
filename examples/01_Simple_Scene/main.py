"""
"""

import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agrume import Agrume
from agrume.scene import Scene
from agrume.entity import Entity
from agrume.physics_entity import PhysicEntity

game = Agrume("Exemple 1: Simple Scene")
scene = Scene("main")
entity = PhysicEntity((300, 150), None, (100, 100))
entity.velocity.x = 5
scene.add_entity(entity)
game.set_current_scene(scene)

def update(delta: float) -> None:
    if entity.rect.bottom >= game.viewport_size.y:
        entity.bounce_y()
    if entity.rect.left < 0 or entity.rect.right > game.viewport_size.x:
        entity.bounce_x()

game.run(update)
