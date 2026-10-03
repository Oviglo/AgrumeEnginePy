"""                                                     
 _____                          _____         _         
|  _  |___ ___ _ _ _____ ___   |   __|___ ___|_|___ ___ 
|     | . |  _| | |     | -_|  |   __|   | . | |   | -_|
|__|__|_  |_| |___|_|_|_|___|  |_____|_|_|_  |_|_|_|___|
      |___|                              |___|          

Author: Loïc Ovigne

input.py: Input manager

"""
from pygame.event import Event
import pygame


class Input:
    def __init__(self):
        self.inputs = {}

    def add_input(self, name: str, pygame_keys: list[int] ) -> None:
        input = {
            "keys": pygame_keys,
            "active": False
        }
        self.inputs[name] = input

    def search(self, event: Event) -> str:
        for [n, i] in self.inputs.items():
            for e in i["keys"]:
                if e == event.key:
                    return n

        return None


    def on_pygame_event(self, event:Event ) -> None:
        """ Don't call this function
        """
        if not hasattr(event, "key"):
            return
        
        name = self.search(event)
        if not name:
            return 
        active = event.type in [pygame.KEYDOWN, pygame.JOYBUTTONDOWN]
        self.inputs[name]["active"] = active


    def is_active(self, name: str) -> bool:
        if not name in self.inputs:
            return False

        return self.inputs[name]["active"]