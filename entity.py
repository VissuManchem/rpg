from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        # Entity's x and y coordinates
        self.x = x
        self.y = y
        #Keyboard character used to represent character
        self.char = char
        #Color of Entity, 3 numbers representing RBG value
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy