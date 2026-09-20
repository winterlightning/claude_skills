# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of skull.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b01deac-dd2c-4265-92f5-d17735f0c07e', 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'), ('85266d86-6f31-4d3b-91ca-d5a232d0c46c', 'pictographic-primitives/interface-essential/skull_85266d86-6f31-4d3b-91ca-d5a232d0c46c.svg'), ('bf02abda-c65a-4ff2-af41-3fdc5c490cc7', 'pictographic-primitives/interface-essential/skull_bf02abda-c65a-4ff2-af41-3fdc5c490cc7.svg'))
PROFILE_SOURCE_KEYS = ('solo/skull', 'solo/skull-85266d86', 'solo/skull-bf02abda')
SOLO_SOURCE_ICON_IDS = ('skull', 'skull-85266d86', 'skull-bf02abda')
REFERENCE_EXPORT_SHA256 = '25b205a3c21b4763f24a7fe4a450a28bf3c3d6bb04cd6302737e3eff5567e46c'

class DrawingContainerSymbol(Sub32):
    icon_id = 'skull-sub32-symbol'
    variant_of = 'skull-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/skull-sub32'
    counterpart_icon_id = 'skull-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('p1-r1-1', (9, 30), ((9, 28), (9, 26), (8, 24)))
        self.add_bezier('p1-r1-2', (8, 24), ((6, 21), (5, 20), (5, 15)))
        self.add_bezier('p1-r1-3', (5, 15), ((5, 8), (9, 2), (16, 2)))
        self.add_bezier('p1-r1-4', (16, 2), ((23, 2), (27, 8), (27, 15)))
        self.add_bezier('p1-r1-5', (27, 15), ((27, 20), (26, 21), (24, 24)))
        self.add_bezier('p1-r1-6', (24, 24), ((23, 27), (23, 28), (23, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (16, 30), (16, 26))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (11, 14), (11, 14))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (21, 14), (21, 14))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
