"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

agrume.py: Main engine class, init Pygame

"""

import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from pygame.time import Clock
from .scene import Scene

class Agrume:
    def __init__(self, name: str, window_size: Vector2 = Vector2(1280, 768), viewport_size: Vector2 = None):
        pygame.init()
        self.name: str = name
        self.window_size: Vector2 = window_size
        self.viewport_size: Vector2 = viewport_size if viewport_size else window_size
        self.window_surface: Surface = pygame.display.set_mode(self.window_size)
        self.viewport_surface: Surface = Surface(self.viewport_size)
        pygame.display.set_caption(self.name)
        self.is_running = True
        self.clock = Clock()
        self.delta_time = 0.0
        self.framerate = 60
        self.current_scene: Scene = None

    def run(self, update_callback: function = None) -> None:
        """ Run the game loop
        """
        while (self.is_running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            # Update & draw current scene
            if self.current_scene:
                self.current_scene.update(self.delta_time)
                self.current_scene.draw(self.viewport_surface)

            # Resize viewport surface into window
            self.window_surface.blit(pygame.transform.scale(self.viewport_surface, self.window_surface.get_size()), (0, 0))
            pygame.display.update()

            if update_callback:
                update_callback(self.delta_time)

            self.delta_time = self.clock.tick(self.framerate) / 1000.0
            self.delta_time = max(0.001, min(self.delta_time, 0.1)) + 1.0
            

        pygame.quit()

    def set_current_scene(self, scene: Scene) -> None:
        self.current_scene = scene
