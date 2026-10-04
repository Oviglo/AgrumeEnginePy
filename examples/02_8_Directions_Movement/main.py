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
from agrume.eight_directions_movement import EightDirectionsMovement
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, CONTROLLER_BUTTON_DPAD_UP, CONTROLLER_BUTTON_DPAD_DOWN, CONTROLLER_BUTTON_DPAD_LEFT, CONTROLLER_BUTTON_DPAD_RIGHT

game = Agrume("Exemple 2: 8  Directions Movement")
scene = Scene("main")
game.set_current_scene(scene)

# Define inputs
game.input.add_input(EightDirectionsMovement.UP, [K_UP, CONTROLLER_BUTTON_DPAD_UP])
game.input.add_input(EightDirectionsMovement.DOWN, [K_DOWN, CONTROLLER_BUTTON_DPAD_DOWN])
game.input.add_input(EightDirectionsMovement.LEFT, [K_LEFT, CONTROLLER_BUTTON_DPAD_LEFT])
game.input.add_input(EightDirectionsMovement.RIGHT, [K_RIGHT, CONTROLLER_BUTTON_DPAD_RIGHT])

# Create player
player = Entity(Vector2(0, 0), Path("player_down.png"))
player.movement = EightDirectionsMovement()
player.movement.max_speed = 50
player.hitbox_rect = player.hitbox_rect.inflate(-24, -10)
scene.add_entity(player)

# Create wall
wall = Entity(Vector2(300, 100), None, Vector2(80, 300))
wall.image.fill("mediumorchid4")
scene.add_entity(wall)

def update(delta: float):
    if wall in scene.get_collide_entities(player):
        player.movement.collide_entities = [wall]

game.run(update)