from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:

    # Takes 4 arguments: entities is the Set of entities, 
    # event_handler is the same one from main.py
    # player is the player entity separate from the set since it will be acessed way more often
    # game_map is the Game Map
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    # Iterates through events that are passed in
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            # Handles events passed through
            action = self.event_handler.dispatch(event)
            # Unrecognized key presses, skips rest of loop
            if action is None:
                    continue  
            # Calls perfrom method from Action class
            action.perform(self, self.player)
            
    # Handles screen drawing
    def render(self, console: Console, context: Context) -> None:
        # Calls game map's render method to draw the map
        self.game_map.render(console)
        #Iterates through entities and prints their locations, etc.
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()