"""
"""

import sys
from pathlib import Path

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agrume import Agrume
from agrume.scene import Scene
from agrume.entity import Entity
from agrume.spritesheet import Spritesheet
from agrume.animation import Animation
from pygame.math import Vector2
from agrume.platform_movement import PlatformMovement
from agrume.tilemap import Tilemap, TileCollisionType
from pygame import K_SPACE, K_LEFT, K_RIGHT, CONTROLLER_BUTTON_DPAD_UP, CONTROLLER_BUTTON_DPAD_DOWN, CONTROLLER_BUTTON_DPAD_LEFT, CONTROLLER_BUTTON_DPAD_RIGHT
from pygame.image import load

game = Agrume("Exemple 3: Plateform", Vector2(1280, 768), Vector2(320, 192))
scene = Scene("main")
scene.gravity = Vector2(0, 1)
game.set_current_scene(scene)

# Define inputs
game.input.add_input(PlatformMovement.LEFT, [K_LEFT])
game.input.add_input(PlatformMovement.RIGHT, [K_RIGHT])
game.input.add_input(PlatformMovement.JUMP, [K_SPACE])

# Tilemap
tilemap = Tilemap(load(Path("tileset.png")))
tilemap.tile_size = 18
for x in range(0, 18):
    tilemap.set_tile_by_id(Vector2(x, 9), 0, TileCollisionType.SOLID)
            

scene.add_entity(tilemap)

# Player
player = Entity(Vector2(50, 50), Path("player.png"))
player.movement = PlatformMovement()
scene.add_entity(player)
player.movement.collide_entities = [tilemap]
player.movement.max_speed = 20

def update(delta: float):
    pass

game.run(update)