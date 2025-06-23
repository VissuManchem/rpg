class Action:
    pass

# used when esc is pressed, exits the game
class EscapeAction(Action):
    pass

# Used when player is moving around
class MovementAction(Action):
    # dx and dy are coordinates where player is trying to move to
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy