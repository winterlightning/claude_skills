"""Two busts face a shared table, with one set farther back at the upper left and one nearer at the lower right. Curved hairlines cross both circular heads, and the tabletop recedes diagonally.
Lucide user head and shoulder primitives. Rear-left and foreground-right participants flank a receding table; hairlines, chest mark and tabletop thickness omitted. Perspective asymmetry is intentional.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4c73429-f620-431b-88fc-a299ceb4f51c'
SOURCE_PATH = 'pictographic-primitives/work/recruiting employee boss interview_c4c73429-f620-431b-88fc-a299ceb4f51c.svg'
AUTHOR = 'gpt-6'


class JobInterview(Solo48):
    icon_id = 'job-interview'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('interview', 'people', 'recruiting', 'table', 'meeting', 'employee')

    def build(self) -> None:
        self.add_arc('rear-head-top', (10, 10), (18, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('rear-head-bottom', (18, 10), (10, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('rear-head', 'rear-head-top', 'rear-head-bottom', closed=True)
        self.add_arc('rear-shoulder', (6, 27), (14, 23), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('rear-arm', (14, 23), (22, 23))
        self.add_contour('rear-bust', 'rear-shoulder', 'rear-arm', closed=False)
        self.add_arc('front-head-top', (30, 27), (38, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('front-head-bottom', (38, 27), (30, 27), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('front-head', 'front-head-top', 'front-head-bottom', closed=True)
        self.add_arc('front-left', (26, 42), (34, 40), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_arc('front-right', (34, 40), (42, 42), radius_x=8, radius_y=2, sweep=True, large_arc=False)
        self.add_contour('front-bust', 'front-left', 'front-right', closed=False)
        self.add_polyline('table', (21, 35), (10, 35), (6, 39), closed=False)
        self.add_line('table-leg', (6, 39), (6, 42))
        self.relate("connect", 'table', 'table-leg')
