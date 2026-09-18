"""Independent 32px profile of cursor.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1d7d06ed-e8d1-45e5-bf6a-390fe16ad950'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cursor_1d7d06ed-e8d1-45e5-bf6a-390fe16ad950.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1d7d06ed-e8d1-45e5-bf6a-390fe16ad950', 'pictographic-primitives/interface-essential/cursor_1d7d06ed-e8d1-45e5-bf6a-390fe16ad950.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cursor',)
SOLO_SOURCE_ICON_IDS = ('cursor',)
REFERENCE_EXPORT_SHA256 = 'ca09766934a09880c8ffc02cd535ee6995a399d83059ea7b1b77769b9dce0d9e'

class Drawing(Sub32):
    icon_id = 'cursor-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 14), (5, 2))
        self.add_line('p1-r1-2', (5, 2), (7, 30))
        self.add_line('p1-r1-3', (7, 30), (14, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (14, 17), (27, 14))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (14, 17), (21, 28))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p3-r1-1')
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
