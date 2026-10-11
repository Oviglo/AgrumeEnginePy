"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

animation.py: Animation manager for entities

"""

from pygame.math import Vector2
from pygame.surface import Surface
import pygame

class Animation:
    def __init__(self, frames: list[Surface], frame_duration: float = 10.0):
        self.frames = frames
        self.frame_duration = frame_duration
        self.is_play: bool = True
        self.current_frame_index = 0
        self.time_accumulator: float = 0.0
        self.loop: bool = True

    def update(self, delta: float) -> None:
        self.time_accumulator += delta
        if self.time_accumulator >= self.frame_duration:
            self.time_accumulator -= self.frame_duration
            if not self.is_play:
                return
            if self.loop or self.current_frame_index < len(self.frames) - 1:
                self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)

    def draw(self, target: Surface) -> None:
        target.blit(self.frames[self.current_frame_index], (0, 0))

    def play(self) -> None:
        self.current_frame_index = 0
        self.is_play = True

    def stop(self) -> None:
        self.is_play = False
        self.current_frame_index = 0

    def pause(self) -> None:
        self.is_play = False

    def resume(self) -> None:
        self.is_play = True

    def get_current_frame(self) -> Surface|None:
        return self.frames[self.current_frame_index]
