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

class Tilemap():
    def __init__(self):
        self.__tile_size: int = 16
        self.tileset: Surface = None
        self.data = {}

    @property
    def tile_size(self) -> int:
        return self.__tile_size

    @tile_size.setter
    def tile_size(self, tile_size: int) -> None:
        self.__tile_size = tile_size