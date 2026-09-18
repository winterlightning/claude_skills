"""Independent 32px profile of bell-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '6969bce5-a6ce-4d22-88c4-77791dfa309a'
SOURCE_PATH = 'pictographic-primitives/symbol/bell_6969bce5-a6ce-4d22-88c4-77791dfa309a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6969bce5-a6ce-4d22-88c4-77791dfa309a', 'pictographic-primitives/symbol/bell_6969bce5-a6ce-4d22-88c4-77791dfa309a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bell-symbol',)
SOLO_SOURCE_ICON_IDS = ('bell-symbol',)
REFERENCE_EXPORT_SHA256 = '8a631da03da80ce128b97882e9934cdc0680872cb6d110cf8aaa4e7d5390c840'

class Drawing(Sub32):
    icon_id = 'bell-symbol-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 30), (5, 19))
        self.add_arc('p1-r1-2', (5, 19), (16, 8), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('p1-r1-3', (16, 8), (27, 19), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (27, 19), (27, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (5, 30), (27, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p3-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
