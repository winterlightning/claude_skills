"""Kite with Trailing Tails. Tilted kite with two loose tails; retain one spar and omit the second to avoid four tiny openings.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide sailboat: a simple fabric outline; no useful exact kite match. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e2671066-49d9-59b1-975f-f063fa8cff58'
SOURCE_PATH = 'pictographic-primitives/recreation/outdoors kite flying_e2671066-49d9-59b1-975f-f063fa8cff58.svg'
AUTHOR = 'gpt-6'


class KiteWithTrailingTails(Solo48):
    icon_id = 'kite-with-trailing-tails'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('kite', 'with', 'trailing', 'tails')

    def build(self) -> None:
        self.add_line('kite-1', (22, 6), (42, 6))
        self.add_line('kite-2', (42, 6), (42, 26))
        self.add_line('kite-3', (42, 26), (30, 28))
        self.add_line('kite-4', (30, 28), (18, 30))
        self.add_line('kite-5', (18, 30), (22, 6))
        self.add_contour('kite', 'kite-1', 'kite-2', 'kite-3', 'kite-4', 'kite-5', closed=True)
        self.add_line('spar', (22, 6), (42, 26))
        self.relate("connect", 'kite', 'spar')
        self.add_arc('tail-left-1', (18, 30), (10, 34), radius_x=6, radius_y=4, sweep=False)
        self.add_arc('tail-left-2', (10, 34), (6, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('tail-left', 'tail-left-1', 'tail-left-2', closed=False)
        self.relate("connect", 'kite', 'tail-left')
        self.add_arc('tail-right-1', (30, 28), (30, 36), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('tail-right-2', (30, 36), (27, 42), radius_x=6, radius_y=6, sweep=False)
        self.add_contour('tail-right', 'tail-right-1', 'tail-right-2', closed=False)
        self.relate("connect", 'kite', 'tail-right')
