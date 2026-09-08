"""Koala gripping a forked branch. Large ear, round head and seated haunch retained; far ear omitted. Lucide cat guides the head; directional pose stays asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95f00a8c-536e-5767-97fa-8968fad8e99a'
SOURCE_PATH = 'pictographic-primitives/animals/koala bamboo_95f00a8c-536e-5767-97fa-8968fad8e99a.svg'
AUTHOR = 'gpt-6'


class KoalaWithBranch(Solo48):
    icon_id = 'koala-with-branch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('koala', 'branch', 'eucalyptus', 'holding', 'marsupial', 'australia', 'animal', 'sitting')

    def build(self) -> None:
        # Exact visible extremes: (0, 0, 48, 48); centerline inset 2.
        self.add_arc('head-right', (23, 3), (23, 25), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('head-left-bottom', (23, 25), (12, 14), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('head-left-top', (12, 14), (23, 3), radius_x=11, radius_y=11, sweep=True, large_arc=False)
        self.add_contour('head', 'head-right', 'head-left-bottom', 'head-left-top', closed=True)
        self.add_arc('ear-a', (23, 3), (15, 2), radius_x=8, radius_y=1, sweep=False, large_arc=False)
        self.add_arc('ear-b', (15, 2), (5, 10), radius_x=10, radius_y=8, sweep=False, large_arc=False)
        self.add_arc('ear-c', (5, 10), (12, 14), radius_x=7, radius_y=4, sweep=False, large_arc=False)
        self.add_contour('ear', 'ear-a', 'ear-b', 'ear-c', closed=False)
        self.relate("connect", 'ear', 'head')
        self.add_arc('nose-right', (24, 10), (24, 18), radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('nose-left', (24, 18), (24, 10), radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('nose', 'nose-right', 'nose-left', closed=True)
        self.add_arc('back', (12, 14), (2, 35), radius_x=30, radius_y=30, sweep=False, large_arc=False)
        self.add_arc('haunch', (2, 35), (16, 46), radius_x=14, radius_y=11, sweep=False, large_arc=False)
        self.add_line('base', (16, 46), (31, 46))
        self.add_arc('foot', (31, 46), (31, 38), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('foot-top-a', (31, 38), (29, 38))
        self.add_line('foot-top-b', (29, 38), (20, 38))
        self.add_arc('wrist', (20, 38), (18, 34), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('arm-bottom', (18, 34), (23, 29))
        self.add_line('hand-bottom-a', (23, 29), (34, 29))
        self.add_line('hand-bottom-b', (34, 29), (37, 29))
        self.add_arc('hand', (37, 29), (37, 23), radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_line('arm-top', (37, 23), (23, 25))
        self.add_contour('body', 'back', 'haunch', 'base', 'foot', 'foot-top-a', 'foot-top-b', 'wrist', 'arm-bottom', 'hand-bottom-a', 'hand-bottom-b', 'hand', 'arm-top', closed=False)
        self.relate("connect", 'body', 'head')
        self.add_line('branch-top', (40, 16), (43, 9))
        self.add_line('branch-grip', (40, 16), (37, 23))
        self.add_line('fork', (40, 16), (46, 16))
        self.relate("connect", 'branch-top', 'branch-grip')
        self.relate("connect", 'branch-top', 'fork')
        self.relate("connect", 'branch-grip', 'fork')
        self.relate("connect", 'branch-grip', 'body')
        self.add_line('branch-lower', (34, 29), (29, 38))
        self.relate("connect", 'branch-lower', 'body')
