"""Independent 32px profile of skull.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b01deac-dd2c-4265-92f5-d17735f0c07e', 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'), ('85266d86-6f31-4d3b-91ca-d5a232d0c46c', 'pictographic-primitives/interface-essential/skull_85266d86-6f31-4d3b-91ca-d5a232d0c46c.svg'), ('bf02abda-c65a-4ff2-af41-3fdc5c490cc7', 'pictographic-primitives/interface-essential/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.svg'))
PROFILE_SOURCE_KEYS = ('solo/skull', 'solo/skull-85266d86', 'solo/skull-bf02abda')
SOLO_SOURCE_ICON_IDS = ('skull', 'skull-85266d86', 'skull-bf02abda')
REFERENCE_EXPORT_SHA256 = '25b205a3c21b4763f24a7fe4a450a28bf3c3d6bb04cd6302737e3eff5567e46c'

class DrawingContainerSymbol(Sub32):
    icon_id = 'skull-sub32-symbol'
    related_origin_icon_id = 'skull-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/skull-sub32'
    counterpart_icon_id = 'skull-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        # Skull: rounded cranium narrowing to the jaw, two eye dots, a tooth line.
        self.add_bezier('s-1', (8, 30), ((8, 28), (8, 26), (7, 24)))
        self.add_bezier('s-2', (7, 24), ((5, 21), (4, 20), (4, 15)))
        self.add_bezier('s-3', (4, 15), ((4, 8), (9, 2), (16, 2)))
        self.add_bezier('s-4', (16, 2), ((23, 2), (28, 8), (28, 15)))
        self.add_bezier('s-5', (28, 15), ((28, 20), (27, 21), (25, 24)))
        self.add_bezier('s-6', (25, 24), ((24, 26), (24, 28), (24, 30)))
        self.add_contour('skull', 's-1', 's-2', 's-3', 's-4', 's-5', 's-6')
        self.add_dot('eye-l', (12, 15))
        self.add_dot('eye-r', (20, 15))
        self.add_line('tooth', (16, 26), (16, 30))
