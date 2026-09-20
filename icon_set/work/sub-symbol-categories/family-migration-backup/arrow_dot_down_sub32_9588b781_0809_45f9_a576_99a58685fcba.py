"""Independent 32px profile of arrow-dot-down.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9588b781-0809-45f9-a576-99a58685fcba'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot down_9588b781-0809-45f9-a576-99a58685fcba.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9588b781-0809-45f9-a576-99a58685fcba', 'pictographic-primitives/arrows/arrow dot down_9588b781-0809-45f9-a576-99a58685fcba.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-dot-down',)
SOLO_SOURCE_ICON_IDS = ('arrow-dot-down',)
REFERENCE_EXPORT_SHA256 = '2271a42d4d8d5732078882d4ffcc05164d93c15beb2b5beb3cabd14adc7b1eb5'

class Drawing(Sub32):
    icon_id = 'arrow-dot-down-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 19), (16, 30))
        self.add_line('p1-r1-2', (16, 30), (27, 19))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (16, 19), (16, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (16, 2), (16, 5))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 10), (16, 13))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
