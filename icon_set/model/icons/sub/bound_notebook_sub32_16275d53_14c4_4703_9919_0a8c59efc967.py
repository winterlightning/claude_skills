"""Independent 32px profile of bound-notebook.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '16275d53-14c4-4703-9919-0a8c59efc967'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/archive_16275d53-14c4-4703-9919-0a8c59efc967.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('16275d53-14c4-4703-9919-0a8c59efc967', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/content/archive_16275d53-14c4-4703-9919-0a8c59efc967.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bound-notebook',)
SOLO_SOURCE_ICON_IDS = ('bound-notebook',)
REFERENCE_EXPORT_SHA256 = '852464449953dbbeaf09e56dd7ab7126f3a1b74ff57760b92c53481c496b579b'

class Drawing(Sub32):
    icon_id = 'bound-notebook-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/bound'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (7, 2), (13, 2))
        self.add_line('p1-r1-2', (13, 2), (25, 2))
        self.add_arc('p1-r1-3', (25, 2), (30, 7), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (30, 7), (30, 25))
        self.add_arc('p1-r1-5', (30, 25), (25, 30), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-6', (25, 30), (7, 30))
        self.add_arc('p1-r1-7', (7, 30), (2, 25), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('p1-r1-8', (2, 25), (2, 7))
        self.add_arc('p1-r1-9', (2, 7), (7, 2), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (13, 2), (13, 8))
        self.add_line('p2-r1-2', (13, 8), (13, 15))
        self.add_line('p2-r1-3', (13, 15), (13, 22))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (8, 8), (13, 8))
        self.add_line('p3-r1-2', (13, 8), (18, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (8, 15), (13, 15))
        self.add_line('p4-r1-2', (13, 15), (18, 15))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (8, 22), (13, 22))
        self.add_line('p5-r1-2', (13, 22), (18, 22))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-2')
        self.relate("connect", 'p2-r1-2', 'p4-r1-1')
        self.relate("connect", 'p2-r1-2', 'p4-r1-2')
        self.relate("connect", 'p2-r1-3', 'p4-r1-1')
        self.relate("connect", 'p2-r1-3', 'p4-r1-2')
        self.relate("connect", 'p2-r1-3', 'p5-r1-1')
        self.relate("connect", 'p2-r1-3', 'p5-r1-2')
