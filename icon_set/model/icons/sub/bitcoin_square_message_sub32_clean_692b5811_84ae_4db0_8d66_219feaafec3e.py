"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '692b5811-84ae-4db0-8d66-219feaafec3e'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square bitcoin_692b5811-84ae-4db0-8d66-219feaafec3e.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square speech bubble', 'lower-left tail', 'Bitcoin B with two bowls', 'two top and bottom currency ticks')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': 'a509f20a98d1279a963ea41476b9adbd56df77a5281d835978be2b064f05d900'}
    icon_id = 'bitcoin-square-message-sub32-clean'
    variant_of = 'bitcoin-square-message-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Bitcoin Message Speech Bubble', 'core_parts': ('rounded square speech bubble', 'lower-left tail', 'Bitcoin B with two bowls', 'two top and bottom currency ticks'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Deepen the bubble and rebuild Bitcoin with two smooth bowls and exact tick attachments.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.message()

        self.add_line('stem',(11,8),(11,22))
        self.add_line('top',(9,10),(18,10))
        self.add_bezier('bowls',(18,10),((23,10),(23,15),(18,15)),((24,15),(24,20),(18,20)))
        self.add_line('bottom',(18,20),(9,20))
        self.add_line('middle',(11,15),(18,15))
        self.add_line('tick-top',(17,8),(17,10))
        self.add_line('tick-bottom',(17,20),(17,22))
        self.relate('connect','stem','top','middle','bottom')
        self.relate('connect','tick-top','top')
        self.relate('connect','tick-bottom','bottom')
        self.relate('connect','bowls','top','middle','bottom')

    def message(self):
        self.add_line('frame-top',(4,2),(28,2))
        self.add_arc('frame-tr',(28,2),(30,4),radius_x=2)
        self.add_line('frame-right',(30,4),(30,25))
        self.add_arc('frame-br',(30,25),(28,27),radius_x=2)
        tail=[(28,27),(15,27),(9,30),(9,27),(4,27)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1):self.add_line(f'frame-tail-{i}',a,b)
        self.add_arc('frame-bl',(4,27),(2,25),radius_x=2)
        self.add_line('frame-left',(2,25),(2,4))
        self.add_arc('frame-tl',(2,4),(4,2),radius_x=2)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br',*[f'frame-tail-{i}' for i in range(1,5)],'frame-bl','frame-left','frame-tl',closed=True)

