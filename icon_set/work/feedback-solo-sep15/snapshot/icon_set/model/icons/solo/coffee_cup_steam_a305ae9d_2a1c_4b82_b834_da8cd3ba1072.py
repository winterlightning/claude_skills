"""Coffee Cup with Steam. Retains the identifying silhouette and visible features.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide coffee: flat rim, straight sides, tangent rounded bottom and a right-side loop handle; source determines two wavy steam lines.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a305ae9d-2a1c-4b82-b834-da8cd3ba1072'
SOURCE_PATH = 'pictographic-primitives/symbol/coffee_a305ae9d-2a1c-4b82-b834-da8cd3ba1072.svg'
AUTHOR = 'gpt-6'


class CoffeeCupSteam(Solo48):
    icon_id = 'coffee-cup-steam'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('coffee', 'cup', 'tea', 'hot', 'drink', 'steam', 'cafe', 'beverage')

    def build(self) -> None:
        self.add_line('rim-1', (6, 23), (30, 23))
        self.add_line('right-1', (30, 23), (30, 24))
        self.add_line('right-2', (30, 24), (30, 34))
        self.add_arc('se', (30, 34), (22, 42), radius_x=8, radius_y=8, sweep=True)
        self.add_line('bottom', (22, 42), (14, 42))
        self.add_arc('sw', (14, 42), (6, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_line('left', (6, 34), (6, 23))
        self.add_contour('cup', 'rim-1', 'right-1', 'right-2', 'se', 'bottom', 'sw', 'left', closed=True)
        self.add_line('handle-top', (30, 24), (36, 24))
        self.add_arc('handle-ne', (36, 24), (42, 29), radius_x=6, radius_y=5, sweep=True)
        self.add_arc('handle-se', (42, 29), (36, 34), radius_x=6, radius_y=5, sweep=True)
        self.add_line('handle-bottom', (36, 34), (30, 34))
        self.add_contour('handle', 'handle-top', 'handle-ne', 'handle-se', 'handle-bottom')
        self.relate("connect", 'cup', 'handle')
        self.add_arc('steam-one-a', (12, 6), (12, 10), radius_x=2, radius_y=2, sweep=False)
        self.add_arc('steam-one-b', (12, 10), (12, 14), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('steam-one', 'steam-one-a', 'steam-one-b')
        self.add_arc('steam-two-a', (24, 6), (24, 10), radius_x=2, radius_y=2, sweep=False)
        self.add_arc('steam-two-b', (24, 10), (24, 14), radius_x=2, radius_y=2, sweep=True)
        self.add_contour('steam-two', 'steam-two-a', 'steam-two-b')
