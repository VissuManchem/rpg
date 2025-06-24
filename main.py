#!/usr/bin/env python3
import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    # Variables to determine screen size
    screen_width = 80
    screen_height = 50

    # Dimensions of the map
    map_width = 80
    map_height = 45

    # Tell TCOD what font to use. In this case, it would be the dejavu PNG
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #Creates instance of our EventHandler. Receives and processes events
    event_handler = EventHandler()

    # Initialize player and NPCs using Entity class
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    # All entities on map stores in this set
    entities = {npc, player}
    # Initializes GameMap
    game_map = generate_dungeon(map_width, map_height)
    #Initialize new Engine
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # Screen is created here
    with tcod.context.new_terminal(
        screen_width, # width
        screen_height, # height
        tileset=tileset, # tileset/fonts from earlier
        title="My First Python RPG", # window title
        vsync = True # VSync
    ) as context:
        
        # creates console that we'll be writing to
        root_console = tcod.Console(screen_width, screen_height, order="F")

        # Game loop
        while True:
            # print @ at the given coordinates
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()