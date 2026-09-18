"""Independent 32px profile of nanobot.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'dd990e4b-d221-4af4-82e5-519aa93fd2a1'
SOURCE_PATH = 'pictographic-primitives/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dd990e4b-d221-4af4-82e5-519aa93fd2a1', 'pictographic-primitives/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/nanobot',)
SOLO_SOURCE_ICON_IDS = ('nanobot',)
REFERENCE_EXPORT_SHA256 = '7ad2a4aedf8e623d264f045f700872f67db3207d773da5b87af2b7f8083f3b0a'

class Drawing(Sub32):
    icon_id = 'nanobot-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 20), (6, 19))
        self.add_line('p1-r1-2', (6, 19), (6, 8))
        self.add_line('p1-r1-3', (6, 8), (7, 7))
        self.add_line('p1-r1-4', (7, 7), (15, 2))
        self.add_arc('p1-r1-5', (15, 2), (17, 2), radius_x=51, radius_y=51, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (17, 2), (25, 7))
        self.add_arc('p1-r1-7', (25, 7), (26, 8), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (26, 8), (26, 20))
        self.add_line('p1-r1-9', (26, 20), (25, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (7, 20), (15, 26))
        self.add_line('p2-r1-2', (15, 26), (17, 26))
        self.add_line('p2-r1-3', (17, 26), (25, 20))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_arc('p3-r1-1', (13, 13), (20, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('p3-r1-2', (20, 13), (13, 13), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_arc('p4-r1-1', (25, 30), (27, 25), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('p4-r1-2', (27, 25), (25, 20), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_arc('p5-r1-1', (7, 20), (5, 25), radius_x=8, radius_y=8, large_arc=False, sweep=False)
        self.add_line('p5-r1-2', (5, 25), (6, 28))
        self.add_arc('p5-r1-3', (6, 28), (7, 30), radius_x=15, radius_y=15, large_arc=False, sweep=False)
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p5-r1-1')
        self.relate("connect", 'p1-r1-9', 'p2-r1-3')
        self.relate("connect", 'p1-r1-9', 'p4-r1-2')
        self.relate("connect", 'p2-r1-1', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-2')
