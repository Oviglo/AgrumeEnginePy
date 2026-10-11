"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

spritesheet.py

"""
from pygame.surface import Surface
from pygame.math import Vector2
from pygame.image import load
from pygame import Rect

class Spritesheet:
    def __init__(self, image_path: str, size: Vector2 = Vector2(1, 1)) -> None:
        self.image_path = image_path
        self._size = size
        self.frames: list[Surface] = []
        self.generate_frames()

    @property
    def size(self) -> Vector2:
        return self._size

    @size.setter
    def size(self, size: Vector2) -> None:
        if size.x <= 0 or size.y <= 0:
            print("Could not have size with 0")
            raise
        self._size = size

    def generate_frames(self) -> None:
        surf = load(self.image_path).convert_alpha()
        surf_rect = surf.get_rect()
        frame_w: int = surf_rect.w // self.size.x
        frame_h: int = surf_rect.h // self.size.y
        self.frames.clear()
        for y in range(int(self.size.y)):
            for x in range(int(self.size.x)):
                new_frame = surf.subsurface(Rect(x * frame_w, y * frame_h, frame_w, frame_h))
                self.frames.append(new_frame)
