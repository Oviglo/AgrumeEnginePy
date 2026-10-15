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
from agrume.eight_directions_movement import EightDirectionsMovement
from agrume.tilemap import Tilemap, TileCollisionType
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, CONTROLLER_BUTTON_DPAD_UP, CONTROLLER_BUTTON_DPAD_DOWN, CONTROLLER_BUTTON_DPAD_LEFT, CONTROLLER_BUTTON_DPAD_RIGHT
from pygame.image import load

game = Agrume("Exemple 2: 8  Directions Movement")
scene = Scene("main")
game.set_current_scene(scene)

# Create tilemap
tilemap = Tilemap(load(Path("tileset.png")))
tilemap.tile_size = 64
for x in range(0, 20):
    for y in range(0, 12):
        if x == 0 or x == 19 or y == 0 or y == 11:
            tilemap.set_tile_by_id(Vector2(x, y), 1, TileCollisionType.SOLID)
        elif x == 10 and y == 8:
            tilemap.set_tile_by_id(Vector2(x, y), 1, TileCollisionType.SOLID)
        else:
            tilemap.set_tile_by_id(Vector2(x, y), 0)

scene.add_entity(tilemap)

# Define inputs
game.input.add_input(EightDirectionsMovement.UP, [K_UP, CONTROLLER_BUTTON_DPAD_UP])
game.input.add_input(EightDirectionsMovement.DOWN, [K_DOWN, CONTROLLER_BUTTON_DPAD_DOWN])
game.input.add_input(EightDirectionsMovement.LEFT, [K_LEFT, CONTROLLER_BUTTON_DPAD_LEFT])
game.input.add_input(EightDirectionsMovement.RIGHT, [K_RIGHT, CONTROLLER_BUTTON_DPAD_RIGHT])

# Create wall
wall = Entity(Vector2(300, 100), None, Vector2(80, 300))
wall.image.fill("mediumorchid4")
scene.add_entity(wall)

# Create player
player = Entity(Vector2(100, 100), None, Vector2(42, 50))
player.movement = EightDirectionsMovement()
player.movement.max_speed = 50
scene.add_entity(player)

# Create animations
player_down_sps = Spritesheet(Path("player_down.png"), Vector2(3, 1))
player_down_animation = Animation(player_down_sps.frames)
player_down_animation.frame_duration = 8.0
player.add_animation("walk_down", player_down_animation)
player.set_current_animation("walk_down")

player_up_sps = Spritesheet(Path("player_up.png"), Vector2(3, 1))
player_up_animation = Animation(player_up_sps.frames)
player_up_animation.frame_duration = 8.0
player.add_animation("walk_up", player_up_animation)
player.set_current_animation("walk_up")

player_left_sps = Spritesheet(Path("player_left.png"), Vector2(3, 1))
player_left_animation = Animation(player_left_sps.frames)
player_left_animation.frame_duration = 8.0
player.add_animation("walk_left", player_left_animation)
player.set_current_animation("walk_left")

player_right_sps = Spritesheet(Path("player_right.png"), Vector2(3, 1))
player_right_animation = Animation(player_right_sps.frames)
player_right_animation.frame_duration = 8.0
player.add_animation("walk_right", player_right_animation)
player.set_current_animation("walk_right")

def on_player_change_direction(direction: Vector2) -> None:
    if direction.x > 0:
        player.set_current_animation("walk_right")
    if direction.x < 0:
        player.set_current_animation("walk_left")
    if direction.y > 0:
        player.set_current_animation("walk_down")
    if direction.y < 0:
        player.set_current_animation("walk_up")

player.movement.on_direction_change = on_player_change_direction

player.movement.collide_entities = [wall, tilemap]

def update(delta: float):
    pass

game.run(update)