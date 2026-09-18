"""Independent 32px profile of paintbrush.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '155f94d2-9337-4308-87e9-3df5169ddd1f'
SOURCE_PATH = 'pictographic-primitives/wayfinding/brush_155f94d2-9337-4308-87e9-3df5169ddd1f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('155f94d2-9337-4308-87e9-3df5169ddd1f', 'pictographic-primitives/wayfinding/brush_155f94d2-9337-4308-87e9-3df5169ddd1f.svg'), ('34da4047-8adb-44d7-8fac-ef87b6b6b4ee', 'pictographic-primitives/symbol/paintbrush_34da4047-8adb-44d7-8fac-ef87b6b6b4ee.svg'))
PROFILE_SOURCE_KEYS = ('solo/paintbrush', 'solo/paintbrush-symbol')
SOLO_SOURCE_ICON_IDS = ('paintbrush', 'paintbrush-symbol')
REFERENCE_EXPORT_SHA256 = 'afdfc6589c4aec16f15286ea1dc76820026b9dd3ca24d4d9c458bbff27b3a607'

class Drawing(Sub32):
    icon_id = 'paintbrush-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/wayfinding'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (22, 2), (30, 10), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (30, 10), (18, 21))
        self.add_line('p1-r1-3', (18, 21), (11, 14))
        self.add_line('p1-r1-4', (11, 14), (22, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_arc('p2-r1-1', (11, 14), (5, 21), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('p2-r1-2', (5, 21), (2, 30))
        self.add_arc('p2-r1-3', (2, 30), (18, 21), radius_x=16, radius_y=9, large_arc=False, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-3')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
