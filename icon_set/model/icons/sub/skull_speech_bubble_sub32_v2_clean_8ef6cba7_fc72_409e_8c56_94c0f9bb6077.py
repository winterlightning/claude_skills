"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '8ef6cba7-fc72-409e-8c56-94c0f9bb6077'
SOURCE_PATH = 'pictographic-primitives/symbol/messages bubble square skull_8ef6cba7-fc72-409e-8c56-94c0f9bb6077.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded rectangular speech bubble', 'lower-left tail', 'skull with closed jaw', 'two eye dots', 'one central jaw divider')
class Drawing(Sub32):
    exception = {'reason': 'User-approved complete reference composition; accept remaining visual/grid/spacing findings while preserving 32x32 and uniform 4px strokes.', 'approved_by': 'user', 'approved_on': '2026-09-24', 'svg_sha256': '11eb4946e49c807af5aa1b0735be180ade96b5c40e7698636c6bf7d213a83485'}
    icon_id = 'skull-speech-bubble-sub32-v2-clean'
    variant_of = 'skull-speech-bubble-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Skull Speech Bubble', 'core_parts': ('rounded rectangular speech bubble', 'lower-left tail', 'skull with closed jaw', 'two eye dots', 'one central jaw divider'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Widen the closed skull jaw and raise the eye dots while retaining the entire bubble and tail.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.message()
        self.skull()

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

    def skull(self,open_jaw=False):
        self.add_bezier('cranium',(11,21),((11,20),(11,19),(9,18)),((7,16),(8,11),(10,9)),((12,7),(20,7),(22,9)),((24,11),(25,16),(23,18)),((21,19),(21,20),(21,21)))
        if not open_jaw:
            self.add_line('jaw',(21,21),(11,21))
            self.add_contour('skull','cranium','jaw',closed=True)
        self.add_dot('eye-left',(13,13))
        self.add_dot('eye-right',(19,13))
        self.add_line('tooth',(16,19),(16,21))
        if not open_jaw:self.relate('connect','tooth','jaw')

