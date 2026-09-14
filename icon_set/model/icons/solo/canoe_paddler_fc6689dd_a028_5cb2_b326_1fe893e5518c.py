"""Canoe Paddler. Seated right-facing paddler with a raised paddle and curved bow; omit decorative waves.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide person-standing: a circular head and sparse articulated limbs. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc6689dd-a028-5cb2-b326-1fe893e5518c'
SOURCE_PATH = 'pictographic-primitives/recreation/canoe person_fc6689dd-a028-5cb2-b326-1fe893e5518c.svg'
AUTHOR = 'gpt-6'


class CanoePaddler(Solo48):
    icon_id = 'canoe-paddler'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('canoe', 'paddler')

    def build(self) -> None:
        self.add_arc('head-top', (16, 11), (22, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (22, 11), (16, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('paddler-1', (12, 30), (17, 22))
        self.add_line('paddler-2', (17, 22), (25, 23))
        self.add_line('paddler-3', (25, 23), (34, 14))
        self.add_contour('paddler', 'paddler-1', 'paddler-2', 'paddler-3', closed=False)
        self.add_line('paddle-1', (39, 8), (31, 20))
        self.add_line('paddle-2', (31, 20), (23, 32))
        self.add_contour('paddle', 'paddle-1', 'paddle-2', closed=False)
        self.relate("connect", 'paddler', 'paddle')
        self.add_line('gunwale', (4, 32), (23, 32))
        self.relate("connect", 'paddler', 'gunwale')
        self.relate("connect", 'paddle', 'gunwale')
        self.add_line('hull-1', (4, 32), (11, 40))
        self.add_line('hull-2', (11, 40), (35, 40))
        self.add_arc('bow', (35, 40), (43, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_line('tip', (43, 32), (44, 29))
        self.add_contour('canoe', 'hull-1', 'hull-2', 'bow', 'tip', closed=False)
        self.relate("connect", 'canoe', 'gunwale')
