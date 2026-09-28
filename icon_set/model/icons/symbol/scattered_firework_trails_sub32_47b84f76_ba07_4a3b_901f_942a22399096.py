"""Independent 32px profile of scattered-firework-trails.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '47b84f76-ba07-4a3b-901f-942a22399096'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/firework_47b84f76-ba07-4a3b-901f-942a22399096.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('47b84f76-ba07-4a3b-901f-942a22399096', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/events/firework_47b84f76-ba07-4a3b-901f-942a22399096.svg'),)
PROFILE_SOURCE_KEYS = ('solo/scattered-firework-trails',)
SOLO_SOURCE_ICON_IDS = ('scattered-firework-trails',)
REFERENCE_EXPORT_SHA256 = '5d4fc511560dc464bc10b21767030c96885e036d8ba23ef86aefd21b91d1e800'

class Drawing(Sub32):
    icon_id = 'scattered-firework-trails-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'events'
    categories = ('primitives', 'events')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (8, 16), (7, 8))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (8, 16), (2, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (8, 16), (7, 22))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (8, 16), (14, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (8, 16), (15, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (22, 14), ((24, 11), (27, 10), (30, 8)))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_bezier('p7-r1-1', (22, 24), ((25, 24), (28, 25), (30, 27)))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (16, 2), (16, 5))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (16, 28), (16, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-1', 'p3-r1-1')
        self.relate('connect', 'p1-r1-1', 'p4-r1-1')
        self.relate('connect', 'p1-r1-1', 'p5-r1-1')
        self.relate('connect', 'p2-r1-1', 'p3-r1-1')
        self.relate('connect', 'p2-r1-1', 'p4-r1-1')
        self.relate('connect', 'p2-r1-1', 'p5-r1-1')
        self.relate('connect', 'p3-r1-1', 'p4-r1-1')
        self.relate('connect', 'p3-r1-1', 'p5-r1-1')
        self.relate('connect', 'p4-r1-1', 'p5-r1-1')
