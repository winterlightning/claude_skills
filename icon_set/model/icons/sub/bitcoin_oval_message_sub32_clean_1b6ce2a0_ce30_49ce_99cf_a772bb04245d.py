"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('oval speech bubble', 'lower-left tail', 'Bitcoin B with two bowls', 'two top and bottom currency ticks')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '9faed3cbcf8f10cab9fa42d0b15cf7e0dbcddfe40c9b06ad46dd89356982a854'}
    icon_id = 'bitcoin-oval-message-sub32-clean'
    variant_of = 'bitcoin-oval-message-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Bitcoin Speech Bubble', 'core_parts': ('oval speech bubble', 'lower-left tail', 'Bitcoin B with two bowls', 'two top and bottom currency ticks'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Rebuild smooth Bitcoin bowls with exact bar and currency tick connections inside the oval bubble.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.oval()

        self.add_line('stem',(11,8),(11,21))
        self.add_line('top',(9,10),(18,10))
        self.add_bezier('bowls',(18,10),((23,10),(23,15),(18,15)),((24,15),(24,20),(18,20)))
        self.add_line('bottom',(18,20),(9,20))
        self.add_line('middle',(11,15),(18,15))
        self.add_line('tick-top',(17,8),(17,10))
        self.add_line('tick-bottom',(17,20),(17,21))
        self.relate('connect','stem','top','middle','bottom')
        self.relate('connect','tick-top','top')
        self.relate('connect','tick-bottom','bottom')
        self.relate('connect','bowls','top','middle','bottom')

    def oval(self):
        self.add_bezier('bubble',(7,23),((4,21),(2,18),(2,15)),((2,8),(8,2),(16,2)),((24,2),(30,8),(30,15)),((30,23),(23,27),(16,27)),((14,27),(12,26),(11,25)))
        self.add_line('tail-lower',(11,25),(4,30))
        self.add_line('tail-upper',(4,30),(7,23))
        self.add_contour('frame','bubble','tail-lower','tail-upper',closed=True)

