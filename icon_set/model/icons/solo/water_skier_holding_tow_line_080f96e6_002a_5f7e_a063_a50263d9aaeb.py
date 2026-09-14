"""Water Skier. Skier leans back with bent knees against a rightward tow line; simplify doubled arms and water to keep the tow and ski readable.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '080f96e6-002a-5f7e-a063-a50263d9aaeb'
SOURCE_PATH = 'pictographic-primitives/recreation/nautic sports water skiing_080f96e6-002a-5f7e-a063-a50263d9aaeb.svg'
AUTHOR = 'gpt-6'


class WaterSkierHoldingTowLine(Solo48):
    icon_id = 'water-skier-holding-tow-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('water', 'skier', 'holding', 'tow', 'line')

    def build(self) -> None:
        self.add_arc('head-top', (9, 11), (15, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (15, 11), (9, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('body-1', (13, 23), (9, 29))
        self.add_line('body-2', (9, 29), (21, 32))
        self.add_line('body-3', (21, 32), (26, 40))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', closed=False)
        self.add_line('arms-1', (13, 23), (25, 23))
        self.add_line('arms-2', (25, 23), (32, 19))
        self.add_line('arms-3', (32, 19), (44, 19))
        self.add_contour('arms', 'arms-1', 'arms-2', 'arms-3', closed=False)
        self.relate("connect", 'body', 'arms')
        self.add_line('ski-1', (8, 40), (30, 40))
        self.add_line('ski-2', (30, 40), (36, 36))
        self.add_contour('ski', 'ski-1', 'ski-2', closed=False)
        self.relate("connect", 'body', 'ski')
        self.add_line('water', (4, 40), (8, 40))
        self.relate("connect", 'water', 'ski')
