"""Person Holding a Bottle. Bent arm reaches the bottle; keep a long neck and broad body, omit cap seam. Deliberate rightward pose.
Keyshape SQUARE, visible extremes (4, 4, 44, 44); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fd9f0d0-c938-40e5-aa02-cf196a735373'
SOURCE_PATH = 'pictographic-primitives/recreation/drinking bottle_7fd9f0d0-c938-40e5-aa02-cf196a735373.svg'
AUTHOR = 'gpt-6'


class PersonHoldingABottle(Solo48):
    icon_id = 'person-holding-a-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "recreation"
    categories = ("primitives", "recreation")
    aliases = ()
    keywords = ('person', 'holding', 'a', 'bottle')

    def build(self) -> None:
        self.add_arc('head-top', (8, 16), (18, 16), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('head-bottom', (18, 16), (8, 16), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('person-1', (6, 42), (6, 34))
        self.add_line('person-2', (6, 34), (12, 30))
        self.add_line('person-3', (12, 30), (18, 32))
        self.add_line('person-4', (18, 32), (22, 39))
        self.add_line('person-5', (22, 39), (30, 39))
        self.add_contour('person', 'person-1', 'person-2', 'person-3', 'person-4', 'person-5', closed=False)
        self.add_line('bottle-1', (32, 17), (32, 6))
        self.add_line('bottle-2', (32, 6), (40, 6))
        self.add_line('bottle-3', (40, 6), (40, 17))
        self.add_line('bottle-4', (40, 17), (42, 23))
        self.add_line('bottle-5', (42, 23), (42, 39))
        self.add_line('bottle-6', (42, 39), (30, 39))
        self.add_line('bottle-7', (30, 39), (30, 23))
        self.add_line('bottle-8', (30, 23), (32, 17))
        self.add_contour('bottle', 'bottle-1', 'bottle-2', 'bottle-3', 'bottle-4', 'bottle-5', 'bottle-6', 'bottle-7', 'bottle-8', closed=True)
        self.relate("connect", 'person', 'bottle')
