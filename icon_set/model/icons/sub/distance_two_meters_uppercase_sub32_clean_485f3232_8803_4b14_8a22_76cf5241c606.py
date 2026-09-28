"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '485f3232-8803-4b14-8a22-76cf5241c606'
SOURCE_PATH = 'pictographic-primitives/state/arrow distance 2m_485f3232-8803-4b14-8a22-76cf5241c606.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('digit 2', 'uppercase M', 'horizontal double-headed arrow below text')

class Drawing(Sub32):
    icon_id = 'distance-two-meters-uppercase-sub32-clean'
    variant_of = 'distance-two-meters-uppercase-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Two Meter Distance Arrow', 'core_parts': ('digit 2', 'uppercase M', 'horizontal double-headed arrow below text'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Widen the uppercase M to open its central valley; snap reused glyphs to the integer grid.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-m-uppercase')

    def build(self):
        self.add_line('text-2-0-0-0-0', (3, 2), (9, 2))
        self.primitives.append(Bezier('text-2-0-0-0-1', Point(*(9, 2)), Point(*(10, 7)), (((11, 2), (12, 5), (10, 7)),)))
        self.add_contour('glyph-2-0-0-0', *['text-2-0-0-0-0', 'text-2-0-0-0-1'], closed=False)
        self.add_line('text-2-0-0-1-0', (10, 7), (4, 12))
        self.primitives.append(Bezier('text-2-0-0-2-0', Point(*(4, 12)), Point(*(3, 15)), (((4, 12), (3, 14), (3, 15)),)))
        self.add_line('text-2-0-0-3-0', (3, 15), (3, 15))
        self.primitives.append(Bezier('text-2-0-0-3-1', Point(*(3, 15)), Point(*(4, 16)), (((3, 16), (3, 16), (4, 16)),)))
        self.add_line('text-2-0-0-3-2', (4, 16), (11, 16))
        self.add_contour('glyph-2-0-0-3', *['text-2-0-0-3-0', 'text-2-0-0-3-1', 'text-2-0-0-3-2'], closed=False)
        self.add_line('text-M-0-0-0-0', (18, 16), (18, 2))
        self.add_line('text-M-0-0-0-1', (18, 2), (24, 11))
        self.add_line('text-M-0-0-0-2', (24, 11), (30, 2))
        self.add_contour('glyph-M-0-0-0', *['text-M-0-0-0-0', 'text-M-0-0-0-1', 'text-M-0-0-0-2'], closed=False)
        self.add_line('text-M-0-0-1-0', (30, 2), (30, 16))
        self.add_line('shaft', (2, 26), (30, 26))
        self.add_polyline('left-head', (6, 22), (2, 26), (6, 30))
        self.add_polyline('right-head', (26, 22), (30, 26), (26, 30))
        self.relate('connect', 'shaft', 'left-head-1', 'left-head-2', 'right-head-1', 'right-head-2')
