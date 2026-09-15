"""Diving Weight Block. Symmetric block and paired vertical belt slots; square the corners to preserve two open slots.
Keyshape HRECT_L, visible extremes (2, 6, 46, 42); centerline envelope inset by 2.
Construction: Lucide caravan: rounded rectangle construction. Source establishes the subject and pose.
Shared circles and rounded rectangles keep repeated radii coherent."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c37d1a4-21b0-4a85-a943-791082ef27bd'
SOURCE_PATH = 'pictographic-primitives/recreation/diving block weight_6c37d1a4-21b0-4a85-a943-791082ef27bd.svg'
AUTHOR = 'gpt-6'


class DivingWeightBlock(Solo48):
    icon_id = 'diving-weight-block'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/recreation"
    aliases = ()
    keywords = ('diving', 'weight', 'block')

    def build(self) -> None:
        self.add_line('block-1', (4, 8), (44, 8))
        self.add_line('block-2', (44, 8), (44, 40))
        self.add_line('block-3', (44, 40), (4, 40))
        self.add_line('block-4', (4, 40), (4, 8))
        self.add_contour('block', 'block-1', 'block-2', 'block-3', 'block-4', closed=True)
        self.add_line('slot-left-1', (12, 16), (20, 16))
        self.add_line('slot-left-2', (20, 16), (20, 32))
        self.add_line('slot-left-3', (20, 32), (12, 32))
        self.add_line('slot-left-4', (12, 32), (12, 16))
        self.add_contour('slot-left', 'slot-left-1', 'slot-left-2', 'slot-left-3', 'slot-left-4', closed=True)
        self.add_line('slot-right-1', (28, 16), (36, 16))
        self.add_line('slot-right-2', (36, 16), (36, 32))
        self.add_line('slot-right-3', (36, 32), (28, 32))
        self.add_line('slot-right-4', (28, 32), (28, 16))
        self.add_contour('slot-right', 'slot-right-1', 'slot-right-2', 'slot-right-3', 'slot-right-4', closed=True)
