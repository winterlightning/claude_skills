"""Independent 32px profile of state32-8220eff5-889a-4ed4-abe8-9cb5b3c749d9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8220eff5-889a-4ed4-abe8-9cb5b3c749d9'
SOURCE_PATH = 'icon_set/assets/combination-state32/8220eff5-889a-4ed4-abe8-9cb5b3c749d9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8220eff5-889a-4ed4-abe8-9cb5b3c749d9', 'icon_set/assets/combination-state32/8220eff5-889a-4ed4-abe8-9cb5b3c749d9.svg'),)
PROFILE_SOURCE_KEYS = ()
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'cddced20243ae2d76d4d5d56143a3bee1eef09d5322fdae3e453590bd8d8e140'

class Drawing(Sub32):
    icon_id = 'state32-8220eff5-889a-4ed4-abe8-9cb5b3c749d9'
    keyshape = Keyshape.HRECT_M
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 23), (2, 9))
        self.add_line('p1-r1-2', (2, 9), (7, 9))
        self.add_bezier('p1-r1-3', (7, 9), ((10, 9), (11, 11), (11, 12)))
        self.add_bezier('p1-r1-4', (11, 12), ((11, 14), (10, 16), (7, 16)))
        self.add_line('p1-r1-5', (7, 16), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (7, 16), ((10, 16), (12, 18), (12, 20)))
        self.add_bezier('p2-r1-2', (12, 20), ((12, 21), (10, 23), (7, 23)))
        self.add_line('p2-r1-3', (7, 23), (2, 23))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (18, 9), (18, 18))
        self.add_bezier('p3-r1-2', (18, 18), ((18, 18), (18, 18), (18, 18)))
        self.add_line('p3-r1-3', (18, 18), (30, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (27, 9), (27, 23))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
