"""Independent 32px profile of feather.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '8ab28f10-44ce-40c6-b0df-2578356c15de'
SOURCE_PATH = 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ab28f10-44ce-40c6-b0df-2578356c15de', 'pictographic-primitives/symbol/feather_8ab28f10-44ce-40c6-b0df-2578356c15de.svg'),)
PROFILE_SOURCE_KEYS = ('solo/feather',)
SOLO_SOURCE_ICON_IDS = ('feather',)
REFERENCE_EXPORT_SHA256 = '306d142b45ce3c96f1e95efb9fa40788b4c3337c6868db586959fae3d43ad148'

class Drawing(Sub32):
    icon_id = 'feather-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (8, 24), ((6, 22), (5, 20), (5, 17)))
        self.add_bezier('p1-r1-2', (5, 17), ((5, 10), (18, 4), (26, 2)))
        self.add_bezier('p1-r1-3', (26, 2), ((27, 4), (27, 6), (27, 8)))
        self.add_bezier('p1-r1-4', (27, 8), ((27, 13), (23, 16), (20, 18)))
        self.add_bezier('p1-r1-5', (20, 18), ((20, 22), (16, 25), (12, 25)))
        self.add_bezier('p1-r1-6', (12, 25), ((11, 25), (10, 24), (8, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (5, 30), (8, 24))
        self.add_line('p2-r1-2', (8, 24), (17, 13))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-1', 'p2-r1-2')
        self.relate("connect", 'p1-r1-6', 'p2-r1-1')
        self.relate("connect", 'p1-r1-6', 'p2-r1-2')
