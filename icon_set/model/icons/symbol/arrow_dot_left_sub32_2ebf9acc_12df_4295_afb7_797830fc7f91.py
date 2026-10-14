"""Independent 32px profile of arrow-dot-left.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '2ebf9acc-12df-4295-afb7-797830fc7f91'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2ebf9acc-12df-4295-afb7-797830fc7f91', 'pictographic-primitives/arrows/arrow dot left_2ebf9acc-12df-4295-afb7-797830fc7f91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-dot-left',)
SOLO_SOURCE_ICON_IDS = ('arrow-dot-left',)
REFERENCE_EXPORT_SHA256 = 'bb53b6be13aba2b731adf2346e20696c0e42dc7ad0ad45ccccbf2b5829c9ce1f'

class Drawing(Sub32):
    icon_id = 'arrow-dot-left-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Arrow pointing left with a dotted tail: the arrow, then two dots, every gap 4 units.
        self.add_dot('dot-1', (30, 16))
        self.add_dot('dot-2', (22, 16))
        self.add_line('stem', (14, 16), (2, 16))
        self.add_polyline('head', (14, 4), (2, 16), (14, 28))
        self.relate('connect', 'stem', 'head')
