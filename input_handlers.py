from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction

# EventDispatch allows us to send event to its proper method
class EventHandler(tcod.event.EventDispatch[Action]):

    # Is called when "X" is clicked at the top of the program, exits program
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()
    
    # Receives key press events, returns Action subclass if key is pressed, or None if no valid key is pressed
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        
        # Holds subclass of action that we assign it
        action: Optional[Action] = None

        # Holds actual key that is pressed
        key = event.sym

        # Checks if arrow key was pressed and move player accordingly
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT    :
            action = MovementAction(dx=1, dy=0)

        # Checks if esc was pressed and exits game for now
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
        
        return action
