"""Flower Award Rosette. Uses six broad lobes and a small circular center ring; preserves the notched ribbon tails.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide award: rosette above a notched ribbon; supplied source adds the lobed flower outline.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58f87e29-b0b5-42be-b412-f3b9d5882e0e'
SOURCE_PATH = 'pictographic-primitives/symbol/award flower shape_58f87e29-b0b5-42be-b412-f3b9d5882e0e.svg'
AUTHOR = 'gpt-6'


class AwardFlowerRosette(Solo48):
    icon_id = 'award-flower-rosette'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('award', 'rosette', 'badge', 'prize', 'ribbon', 'medal', 'winner', 'achievement')

    def build(self) -> None:
        self.add_arc('top', (18, 10), (30, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('ne-outer', (30, 10), (40, 16), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('ne-inner', (40, 16), (36, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('se-inner', (36, 20), (40, 24), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('se-outer', (40, 24), (30, 30), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('bottom', (30, 30), (18, 30), radius_x=6, radius_y=4, sweep=True)
        self.add_arc('sw-outer', (18, 30), (8, 24), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('sw-inner', (8, 24), (12, 20), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('nw-inner', (12, 20), (8, 16), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('nw-outer', (8, 16), (18, 10), radius_x=10, radius_y=6, sweep=True)
        self.add_contour('rosette', 'top', 'ne-outer', 'ne-inner', 'se-inner', 'se-outer', 'bottom', 'sw-outer', 'sw-inner', 'nw-inner', 'nw-outer', closed=True)
        self.add_arc('center-ring-right', (24, 17), (24, 23), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('center-ring-left', (24, 23), (24, 17), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('center-ring', 'center-ring-right', 'center-ring-left', closed=True)
        self.add_polyline('ribbon', (18, 30), (12, 42), (24, 38), (36, 42), (30, 30))
        self.relate("connect", 'rosette', 'ribbon')
