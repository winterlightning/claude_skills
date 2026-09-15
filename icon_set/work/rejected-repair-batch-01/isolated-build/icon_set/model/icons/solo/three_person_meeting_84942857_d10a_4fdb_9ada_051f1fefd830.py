"""Three head-and-shoulder figures form a triangular group, with one centered above the other two. Curved connecting arcs fill the spaces between the figures, suggesting a circular seating arrangement.
Lucide users circular heads and shoulder arcs. Three figures retain triangular seating; one connecting arc suggests the circular arrangement. Two outer ring fragments omitted to avoid crowding. Left/right figures mirror about x=24.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84942857-d10a-4fdb-9ada-051f1fefd830'
SOURCE_PATH = 'pictographic-primitives/work/team meeting_84942857-d10a-4fdb-9ada-051f1fefd830.svg'
AUTHOR = 'gpt-6'


class ThreePersonMeeting(Solo48):
    icon_id = 'three-person-meeting'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('people', 'meeting', 'team', 'group', 'circle', 'collaboration')

    def build(self) -> None:
        self.add_arc('top-head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('top-head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('top-head', 'top-head-top', 'top-head-bottom', closed=True)
        self.add_arc('top-left', (16, 22), (24, 12), radius_x=8, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('top-right', (24, 12), (32, 22), radius_x=8, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('top-bust', 'top-left', 'top-right', closed=False)
        self.relate("connect", 'top-head', 'top-bust')
        self.add_arc('left-head-top', (7, 32), (13, 32), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('left-head-bottom', (13, 32), (7, 32), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('left-head', 'left-head-top', 'left-head-bottom', closed=True)
        self.add_arc('left-outer', (6, 42), (10, 35), radius_x=4, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('left-inner', (10, 35), (18, 42), radius_x=8, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('left-bust', 'left-outer', 'left-inner', closed=False)
        self.relate("connect", 'left-head', 'left-bust')
        self.add_arc('right-head-top', (35, 32), (41, 32), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('right-head-bottom', (41, 32), (35, 32), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('right-head', 'right-head-top', 'right-head-bottom', closed=True)
        self.add_arc('right-inner', (30, 42), (38, 35), radius_x=8, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('right-outer', (38, 35), (42, 42), radius_x=4, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('right-bust', 'right-inner', 'right-outer', closed=False)
        self.relate("connect", 'right-head', 'right-bust')
        self.add_arc('meeting-ring', (18, 42), (30, 42), radius_x=6, radius_y=3, sweep=True, large_arc=False)
        self.relate("connect", 'meeting-ring', 'left-bust')
        self.relate("connect", 'meeting-ring', 'right-bust')
