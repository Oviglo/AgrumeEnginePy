"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

tilemap.py: Create map with tiles

"""

from pygame.surface import Surface
from pygame.math import Vector2
from enum import Enum
from pygame import Rect, Color, transform
from .entity import Entity
from pygame.draw import line

class TileCollisionType(Enum):
    NONE = 'none'
    SOLID = 'solid'

class Tile:
    """ Tile definition
    pos: position on tileset image
    """
    def __init__(self, pos: Vector2):
        self.pos = pos

class TilemapData():
    """
        Data in tilemap
    """
    def __init__(self, pos: Vector2, tile: Tile, collision_type: TileCollisionType = TileCollisionType.NONE) -> None:
        self.pos: Vector2 = pos
        self.collision_type: TileCollisionType = collision_type
        self.tile: Tile = tile
    
    @staticmethod
    def generate_index(x: int, y: int) -> str:
        return str(int(x)) + ';' + str(int(y))

class Tilemap(Entity):
    def __init__(self, tileset: Surface):
        super().__init__()
        self.__tile_size: int = 16
        self.tileset: Surface = tileset
        self.__tiles: dict[int, Tile] = {}
        self.__data: dict[str, TilemapData] = {}
        self.need_redraw: bool = True

        # Grid
        self.grid_color: Color = Color(10, 10, 10, 120)
        self.show_grid: bool = False

        # Dynamic size
        self.__size: Vector2 = Vector2(1, 1)

        self.__generate_tiles()

    def __generate_tiles(self) -> None:
        tileset_rect = self.tileset.get_rect()
        i = 0
        for y in range(0, tileset_rect.h // self.tile_size):
            for x in range(0, tileset_rect.w // self.tile_size):
                self.__tiles[i] = Tile(Vector2(x, y))
                i += 1


    @property
    def tile_size(self) -> int:
        return self.__tile_size

    @tile_size.setter
    def tile_size(self, tile_size: int) -> None:
        self.__tile_size = max(8, tile_size)
        self.__generate_tiles()

    @property
    def size(self) -> Vector2:
        return self.__size

    def set_tile_by_id(self, pos: Vector2, id: int, collision_type: TileCollisionType = TileCollisionType.NONE) -> None:
        tile = self.get_tile_by_id(id)
        if not tile:
            return

        tile_index = TilemapData.generate_index(pos.x, pos.y)
        self.__data[tile_index] = TilemapData(pos, tile, collision_type)

        # Resize tilemap
        self.__size.x = max(self.__size.x, pos.x + 1)
        self.__size.y = max(self.__size.y, pos.y + 1)
        self.rect.w = self.__size.x * self.__tile_size
        self.rect.h = self.__size.y * self.__tile_size
        self.hitbox_rect = self.rect
        self.image = transform.scale(self.image, (self.rect.w, self.rect.h))

        self.need_redraw = True

    def get_tile_by_id(self, id: int) -> Tile|None:
        if id in self.__tiles:
            return self.__tiles[id]

        return None

    def draw_tile_rect(self, dest: Surface, rect: Rect) -> None:
        tiles = self.get_tiles_in_rect(rect)
        for data in tiles:
            dest.blit(self.tileset, (data.pos.x * self.tile_size, data.pos.y * self.tile_size), Rect(data.tile.pos.x * self.tile_size, data.tile.pos.y * self.tile_size, self.tile_size, self.tile_size))

    def draw_rect(self, dest: Surface, rect: Rect) -> None:
        self.draw_tile_rect(dest, rect)
    
    def get_tiles_in_rect(self, rect: Rect) -> list[TilemapData]:
        result = []
        for key, tile_data in self.__data.items():
            # Créer le rectangle du tile (position + taille)
            tile_rect = Rect(
                int(tile_data.pos.x * self.tile_size),
                int(tile_data.pos.y * self.tile_size),
                self.tile_size,
                self.tile_size
            )
            # Vérifier la collision entre les deux rectangles
            if rect.colliderect(tile_rect):
                result.append(tile_data)
        return result

    def update(self, delta: float) -> None:
        super().update(delta)
        if self.need_redraw:
            self.image.set_colorkey((255, 0, 255))
            self.image.fill(Color(255, 0, 255))
            self.draw_rect(self.image, self.rect)
            
            if self.show_grid:
                self.draw_grid()
            self.need_redraw = False

    def get_rect_at(self, pos: Vector2|tuple) -> Rect:
        if isinstance(pos, tuple):
            pos = Vector2(pos[0], pos[1])

        pos.x //= self.tile_size
        pos.y //= self.tile_size
        pos.x *= self.tile_size
        pos.y *= self.tile_size

        return Rect(pos.x, pos.y, self.tile_size, self.tile_size)

    def get_tile_rect(self, tile: TilemapData) -> Rect:
        return Rect(tile.pos.x * self.tile_size, tile.pos.y * self.tile_size, self.tile_size, self.tile_size)

    def get_collision_type_at(self, pos: Vector2|tuple) -> TileCollisionType:
        if isinstance(pos, tuple):
            pos = Vector2(pos[0], pos[1])
        
        pos.x //= self.tile_size
        pos.y //= self.tile_size

        index = TilemapData.generate_index(pos.x, pos.y)
        if index in self.__data:
            return self.__data[index].collision_type

        return TileCollisionType.NONE

    def is_rect_collide(self, rect: Rect) -> bool:
        tiles = self.get_tiles_in_rect(rect)
        for tile in tiles:
            if tile.collision_type == TileCollisionType.SOLID:
                return True

        return False

    def get_collide_tiles(self, rect: Rect) -> list[TilemapData]:
        tiles_in_rect = self.get_tiles_in_rect(rect)
        tiles: list[TilemapData] = []
        for tile in tiles_in_rect:
            tile_rect = self.get_tile_rect(tile)
            if tile.collision_type == TileCollisionType.SOLID and rect.colliderect(tile_rect):
                tiles.append(tile)

        return tiles

    def draw_grid(self):
        for x in range(0, int(self.image.width), self.tile_size):
            line(self.image, self.grid_color, (x, 0), (x, int(self.image.height)))
        for y in range(0, int(self.image.height), self.tile_size):
            line(self.image, self.grid_color, (0, y), (int(self.image.width), y))

    def get_collide_rects(self, rect: Rect) -> list[Rect]:
        tiles = self.get_collide_tiles(rect)
        rects = []
        for tile in tiles:
            rects.append(self.get_tile_rect(tile))

        return rects