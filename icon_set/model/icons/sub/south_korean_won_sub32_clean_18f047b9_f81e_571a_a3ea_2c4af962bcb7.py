"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '18f047b9-f81e-571a-a3ea-2c4af962bcb7'
SOURCE_PATH = 'pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('W-shaped four diagonal strokes', 'one horizontal crossbar')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': 'd31bda5e3d03ae2c77c1109c8045f9e3ae29a4d2cdc364f6567cfd0211344b0d'}
    icon_id = 'south-korean-won-sub32-clean'
    variant_of = 'south-korean-won-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'South Korean Won Symbol', 'core_parts': ('W-shaped four diagonal strokes', 'one horizontal crossbar'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Lower the single currency bar to balance the three triangular openings without adding a second bar.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.add_polyline('won',(2,2),(9,30),(16,2),(23,30),(30,2))
        self.add_line('bar',(2,18),(30,18))
        for i in range(1,5):self.relate('connect','bar',f'won-{i}')

