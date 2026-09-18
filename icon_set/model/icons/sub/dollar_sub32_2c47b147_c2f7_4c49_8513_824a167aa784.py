"""Independent 32px profile of dollar.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2c47b147-c2f7-4c49-8513-824a167aa784'
SOURCE_PATH = 'pictographic-primitives/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c47b147-c2f7-4c49-8513-824a167aa784', 'pictographic-primitives/symbol/dollar_2c47b147-c2f7-4c49-8513-824a167aa784.svg'), ('7930e153-2438-44ec-8db7-960bb9aa10cc', 'pictographic-primitives/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.svg'))
PROFILE_SOURCE_KEYS = ('solo/dollar', 'solo/dollar-sign')
SOLO_SOURCE_ICON_IDS = ('dollar', 'dollar-sign')
REFERENCE_EXPORT_SHA256 = 'eec24736fc812de2d9f5ca8cd10e1c2dcdd65a51e04f3ae8065466bebe6bfca7'

class Drawing(Sub32):
    icon_id = 'dollar-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (26, 9), ((24, 6), (20, 5), (16, 5)))
        self.add_bezier('p1-r1-2', (16, 5), ((10, 5), (5, 6), (5, 10)))
        self.add_bezier('p1-r1-3', (5, 10), ((5, 15), (10, 15), (16, 16)))
        self.add_bezier('p1-r1-4', (16, 16), ((22, 17), (27, 17), (27, 22)))
        self.add_bezier('p1-r1-5', (27, 22), ((27, 26), (22, 27), (16, 27)))
        self.add_bezier('p1-r1-6', (16, 27), ((12, 27), (8, 26), (6, 23)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 2), (16, 5))
        self.add_line('p2-r1-2', (16, 5), (16, 16))
        self.add_line('p2-r1-3', (16, 16), (16, 27))
        self.add_line('p2-r1-4', (16, 27), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-2')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-4')
        self.relate("connect", 'p1-r1-6', 'p2-r1-3')
        self.relate("connect", 'p1-r1-6', 'p2-r1-4')
