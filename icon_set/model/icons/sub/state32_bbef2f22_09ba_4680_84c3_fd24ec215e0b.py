"""Independent 32px profile of state32-bbef2f22-09ba-4680-84c3-fd24ec215e0b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'bbef2f22-09ba-4680-84c3-fd24ec215e0b'
SOURCE_PATH = 'icon_set/assets/combination-state32/bbef2f22-09ba-4680-84c3-fd24ec215e0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bbef2f22-09ba-4680-84c3-fd24ec215e0b', 'icon_set/assets/combination-state32/bbef2f22-09ba-4680-84c3-fd24ec215e0b.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '2412320ef6d46b2f4e129544ca5259f2ce95ed8945ad6cb0696875c1c84fa9f5'

class Drawing(Sub32):
    icon_id = 'state32-bbef2f22-09ba-4680-84c3-fd24ec215e0b'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (11, 22), (11, 10))
        self.add_line('p1-r1-2', (11, 10), (16, 10))
        self.add_bezier('p1-r1-3', (16, 10), ((19, 10), (21, 11), (21, 13)))
        self.add_bezier('p1-r1-4', (21, 13), ((21, 15), (19, 16), (16, 16)))
        self.add_line('p1-r1-5', (16, 16), (11, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_arc('p2-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
