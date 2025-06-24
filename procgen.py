from typing import Tuple

from game_map import GameMap
import tile_types

class RectangularRoom:
    # Initialize rectangular room with its dimensions
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = width + x
        self.y2 = y + height
    
    @property
    def inner(self) -> Tuple[slice, slice]:
        # returns inner area of the room as 2D array index
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)
    
def generate_dungeon(map_width: int, map_height: int) -> GameMap:
    dungeon = GameMap(map_width, map_height)
    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)
    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor

    return dungeon


    