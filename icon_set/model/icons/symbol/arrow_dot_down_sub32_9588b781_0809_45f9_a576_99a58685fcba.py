"""Independent 32px profile of arrow-dot-down.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
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
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Arrow pointing down with a dotted tail: two dots, then the arrow, every gap 4 units.
        self.add_dot('dot-1', (16, 2))
        self.add_dot('dot-2', (16, 10))
        self.add_line('stem', (16, 18), (16, 30))
        self.add_polyline('head', (4, 18), (16, 30), (28, 18))
        self.relate('connect', 'stem', 'head')
