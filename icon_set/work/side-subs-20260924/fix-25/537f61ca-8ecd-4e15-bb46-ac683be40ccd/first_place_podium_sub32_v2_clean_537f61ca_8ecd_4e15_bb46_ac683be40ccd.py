"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '537f61ca-8ecd-4e15-bb46-ac683be40ccd'
SOURCE_PATH = 'pictographic-primitives/rating/ranking first_537f61ca-8ecd-4e15-bb46-ac683be40ccd.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('three podium blocks', 'taller central block', 'left block taller than right', 'numeral 1 on central block')
class Drawing(Sub32):
    icon_id = 'first-place-podium-sub32-v2-clean'
    variant_of = 'first-place-podium-sub32-v2'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'First Place Winner Podium', 'core_parts': ('three podium blocks', 'taller central block', 'left block taller than right', 'numeral 1 on central block'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Construct three squared podium blocks with a wide center and a shorter grid-fitted reused numeral.'}
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('digit-1',)
    def build(self):
        self.add_polyline('outline',(2,28),(2,14),(8,14),(8,4),(24,4),(24,16),(30,16),(30,28),closed=True)
        self.add_line('left-partition',(8,14),(8,28))
        self.add_line('right-partition',(24,16),(24,28))
        self.relate('connect','left-partition','outline-2','outline-3','outline-8')
        self.relate('connect','right-partition','outline-5','outline-6','outline-8')
        self.add_line('text-1-0-0-0-0',(16, 21),(16, 11))
        self.primitives.append(Bezier('text-1-0-0-1-0',Point(*(16, 11)),Point(*(16, 11)),(((16, 11), (16, 11), (16, 11)),)))
        self.add_line('text-1-0-0-2-0',(16, 11),(14, 11))
        self.add_line('text-1-0-1-0-0',(14, 21),(18, 21))

