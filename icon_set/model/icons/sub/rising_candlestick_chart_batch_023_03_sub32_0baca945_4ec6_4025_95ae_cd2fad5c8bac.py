"""Independent 32px profile of rising-candlestick-chart-batch-023-03.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0baca945-4ec6-4025-95ae-cd2fad5c8bac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0baca945-4ec6-4025-95ae-cd2fad5c8bac', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rising-candlestick-chart-batch-023-03',)
SOLO_SOURCE_ICON_IDS = ('rising-candlestick-chart-batch-023-03',)
REFERENCE_EXPORT_SHA256 = 'd77513dca53491b44f429393093095e9266932f9596acf15e72b9f4e464ca7be'

class Drawing(Sub32):
    icon_id = 'rising-candlestick-chart-batch-023-03-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (2, 16), (5, 16))
        self.add_line('p1-r1-2', (5, 16), (8, 16))
        self.add_line('p1-r1-3', (8, 16), (8, 24))
        self.add_line('p1-r1-4', (8, 24), (5, 24))
        self.add_line('p1-r1-5', (5, 24), (2, 24))
        self.add_line('p1-r1-6', (2, 24), (2, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (5, 12), (5, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 24), (5, 27))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (13, 12), (16, 12))
        self.add_line('p4-r1-2', (16, 12), (19, 12))
        self.add_line('p4-r1-3', (19, 12), (19, 20))
        self.add_line('p4-r1-4', (19, 20), (16, 20))
        self.add_line('p4-r1-5', (16, 20), (13, 20))
        self.add_line('p4-r1-6', (13, 20), (13, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', 'p4-r1-6', closed=False)
        self.add_line('p5-r1-1', (16, 8), (16, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (16, 20), (16, 24))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (24, 8), (27, 8))
        self.add_line('p7-r1-2', (27, 8), (30, 8))
        self.add_line('p7-r1-3', (30, 8), (30, 16))
        self.add_line('p7-r1-4', (30, 16), (27, 16))
        self.add_line('p7-r1-5', (27, 16), (24, 16))
        self.add_line('p7-r1-6', (24, 16), (24, 8))
        self.add_contour('path-7-1', 'p7-r1-1', 'p7-r1-2', 'p7-r1-3', 'p7-r1-4', 'p7-r1-5', 'p7-r1-6', closed=False)
        self.add_line('p8-r1-1', (27, 5), (27, 8))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (27, 16), (27, 20))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-4', 'p3-r1-1')
        self.relate("connect", 'p1-r1-5', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-1')
        self.relate("connect", 'p4-r1-2', 'p5-r1-1')
        self.relate("connect", 'p4-r1-4', 'p6-r1-1')
        self.relate("connect", 'p4-r1-5', 'p6-r1-1')
        self.relate("connect", 'p7-r1-1', 'p8-r1-1')
        self.relate("connect", 'p7-r1-2', 'p8-r1-1')
        self.relate("connect", 'p7-r1-4', 'p9-r1-1')
        self.relate("connect", 'p7-r1-5', 'p9-r1-1')
