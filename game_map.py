import numpy as np
from tcod.console import Console

import tile_types

class GameMap:
    def __init__(self, width: int, height: int):
        # Initializes width and height
        self.width, self.height = width, height

        # Creates 2D array filled with the floor tile type
        self.tiles = np.full((width, height), fill_value=tile_types.floor, order="F")

        # Creates 3 tile wall at specified location
        self.tiles[30:33, 22] = tile_types.wall

    # Returns true if x and y values are in the map's bounds        
    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= x < self.height
    
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height]