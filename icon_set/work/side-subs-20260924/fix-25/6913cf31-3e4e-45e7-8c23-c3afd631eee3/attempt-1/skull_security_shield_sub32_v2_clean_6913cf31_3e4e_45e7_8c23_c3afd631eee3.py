"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '6913cf31-3e4e-45e7-8c23-c3afd631eee3'
SOURCE_PATH = 'pictographic-primitives/war/shield skull_6913cf31-3e4e-45e7-8c23-c3afd631eee3.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('shield outline with curved top and pointed base', 'skull with open-bottom jaw', 'two eye dots', 'detached central jaw stroke')
class Drawing(Sub32):
    icon_id = 'skull-security-shield-sub32-v2-clean'
    variant_of = 'skull-security-shield-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Skull Security Protection Shield', 'core_parts': ('shield outline with curved top and pointed base', 'skull with open-bottom jaw', 'two eye dots', 'detached central jaw stroke'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Widen the open skull jaw and separate the eye dots from the shorter detached central jaw stroke.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.add_bezier('shield',(2,5),((10,1),(22,1),(30,5)),((30,11),(30,16),(29,20)),((27,25),(21,28),(16,30)),((11,28),(5,25),(3,20)),((2,16),(2,11),(2,5)))
        self.add_contour('frame','shield',closed=True)
        self.skull(open_jaw=True)

    def skull(self,open_jaw=False):
        self.add_bezier('cranium',(11,23),((11,20),(11,19),(9,18)),((7,16),(8,11),(10,9)),((12,7),(20,7),(22,9)),((24,11),(25,16),(23,18)),((21,19),(21,20),(21,23)))
        if not open_jaw:
            self.add_line('jaw',(21,23),(11,23))
            self.add_contour('skull','cranium','jaw',closed=True)
        self.add_dot('eye-left',(13,14))
        self.add_dot('eye-right',(19,14))
        self.add_line('tooth',(16,21),(16,23))
        if not open_jaw:self.relate('connect','tooth','jaw')

