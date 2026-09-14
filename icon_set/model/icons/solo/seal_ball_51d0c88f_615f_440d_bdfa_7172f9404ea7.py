"""seal-balancing-ball: SQUARE ink (6,6)-(42,42). Raised head below plain ball; eye omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '51d0c88f-615f-440d-bdfa-7172f9404ea7'
SOURCE_PATH = 'pictographic-primitives/animals/seal ball_51d0c88f-615f-440d-bdfa-7172f9404ea7.svg'
AUTHOR = 'gpt-6'

class SealBalancingBall(Solo48):
    icon_id = 'seal-balancing-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('seal', 'ball', 'balance', 'circus', 'sea lion', 'trick', 'show', 'marine')

    def build(self) -> None:
        """Opening repair: Made the balanced ball round, preserving its nose contact and the seal’s silhouette."""
        self.add_arc('ball-1', (12, 6), (12, 18), sweep=True, radius_x=6, radius_y=6)
        self.add_arc('ball-2', (12, 18), (12, 6), sweep=True, radius_x=6, radius_y=6)
        self.add_contour('ball', 'ball-1', 'ball-2', closed=True)
        self.add_arc('body-1', (12, 18), (22, 28), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-2', (22, 28), (22, 34))
        self.add_arc('body-3', (22, 34), (36, 40), radius_x=24, radius_y=18, sweep=True)
        self.add_line('body-4', (36, 40), (40, 40))
        self.add_arc('body-5', (40, 40), (42, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-6', (42, 42), (20, 42))
        self.add_line('body-7', (20, 42), (12, 42))
        self.add_arc('body-8', (12, 42), (6, 36), radius_x=10, radius_y=10, sweep=True)
        self.add_line('body-9', (6, 36), (6, 28))
        self.add_arc('body-10', (6, 28), (12, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', closed=True)
        self.add_arc('flipper-1', (15, 39), (20, 42), radius_x=12, radius_y=12, sweep=False)
        self.add_contour('flipper', 'flipper-1', closed=False)
        self.relate('connect', 'body', 'flipper')
        self.relate('connect', 'body', 'ball')
