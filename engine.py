from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler


class Engine:

    # Takes 3 arguments: entities is the Set of entities, 
    # event_handler is the same one from main.py
    # player is the player entity separate from the set since it will be acessed way more often
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.player = player

    # Iterates through events that are passed in
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            # Handles events passed through
            action = self.event_handler.dispatch(event)
            # Unrecognized key presses, skips rest of loop
            if action is None:
                    continue  
            # If action is instance of MovementAction, moves @ symbol
            if isinstance(action, MovementAction):
                # Grabs dx and dy values from MovementAction and 
                # adds it to player_x and player_y
                self.player.move(dx=action.dx, dy=action.dy)
                # If user hits Esc, exit program
            elif isinstance(action, EscapeAction):
                raise SystemExit()
            
    # Handles screen drawing
    def render(self, console: Console, context: Context) -> None:
        #Iterates through entities and prints their locations, etc.
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()