"""Independent 32px profile of beaker.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f1cab2ea-f7f8-47a0-972d-7983402b29a8'
SOURCE_PATH = 'pictographic-primitives/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f1cab2ea-f7f8-47a0-972d-7983402b29a8', 'pictographic-primitives/symbol/beaker_f1cab2ea-f7f8-47a0-972d-7983402b29a8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/beaker',)
SOLO_SOURCE_ICON_IDS = ('beaker',)
REFERENCE_EXPORT_SHA256 = '95b7b20a8d78444cd276bad327e730c6f1de876b8d4e59019a9e377f9632ea9c'

class Drawing(Sub32):
    icon_id = 'beaker-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (13, 2), (13, 8))
        self.add_bezier('p1-r1-2', (13, 8), ((13, 12), (5, 12), (5, 19)))
        self.add_arc('p1-r1-3', (5, 19), (27, 19), radius_x=11, radius_y=11, large_arc=False, sweep=False)
        self.add_bezier('p1-r1-4', (27, 19), ((27, 12), (20, 12), (20, 8)))
        self.add_line('p1-r1-5', (20, 8), (20, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (10, 2), (13, 2))
        self.add_line('p2-r1-2', (13, 2), (20, 2))
        self.add_line('p2-r1-3', (20, 2), (22, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')
