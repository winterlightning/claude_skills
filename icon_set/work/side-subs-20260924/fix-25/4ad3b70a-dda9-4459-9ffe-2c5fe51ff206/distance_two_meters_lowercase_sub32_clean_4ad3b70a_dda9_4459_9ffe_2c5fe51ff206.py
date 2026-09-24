"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '4ad3b70a-dda9-4459-9ffe-2c5fe51ff206'
SOURCE_PATH = 'pictographic-primitives/state/arrow distance 2m_4ad3b70a-dda9-4459-9ffe-2c5fe51ff206.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('digit 2', 'lowercase m', 'horizontal double-headed arrow below text')
class Drawing(Sub32):
    icon_id = 'distance-two-meters-lowercase-sub32-clean'
    variant_of = 'distance-two-meters-lowercase-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Two Meters Distance Arrow', 'core_parts': ('digit 2', 'lowercase m', 'horizontal double-headed arrow below text'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Retain the smaller lowercase m and grid-fit the reused digit and letter for smoother consistent alignment.'}
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-m')
    def build(self):
        self.add_line('text-2-0-0-0-0',(3, 2),(9, 2))
        self.primitives.append(Bezier('text-2-0-0-0-1',Point(*(9, 2)),Point(*(10, 7)),(((11, 2), (12, 5), (10, 7)),)))
        self.add_contour('glyph-2-0-0-0',*['text-2-0-0-0-0', 'text-2-0-0-0-1'],closed=False)
        self.add_line('text-2-0-0-1-0',(10, 7),(4, 12))
        self.primitives.append(Bezier('text-2-0-0-2-0',Point(*(4, 12)),Point(*(3, 15)),(((4, 12), (3, 14), (3, 15)),)))
        self.add_line('text-2-0-0-3-0',(3, 15),(3, 15))
        self.primitives.append(Bezier('text-2-0-0-3-1',Point(*(3, 15)),Point(*(4, 16)),(((3, 16), (3, 16), (4, 16)),)))
        self.add_line('text-2-0-0-3-2',(4, 16),(11, 16))
        self.add_contour('glyph-2-0-0-3',*['text-2-0-0-3-0', 'text-2-0-0-3-1', 'text-2-0-0-3-2'],closed=False)
        self.add_line('text-m-0-0-0-0',(23, 10),(23, 16))
        self.add_line('text-m-0-1-0-0',(17, 16),(17, 10))
        self.primitives.append(Bezier('text-m-0-1-1-0',Point(*(17, 10)),Point(*(20, 6)),(((17, 8), (18, 6), (20, 6)),)))
        self.primitives.append(Bezier('text-m-0-1-2-0',Point(*(20, 6)),Point(*(23, 10)),(((22, 6), (23, 8), (23, 10)),)))
        self.primitives.append(Bezier('text-m-0-1-3-0',Point(*(23, 10)),Point(*(26, 6)),(((23, 8), (24, 6), (26, 6)),)))
        self.primitives.append(Bezier('text-m-0-1-4-0',Point(*(26, 6)),Point(*(29, 10)),(((28, 6), (29, 8), (29, 10)),)))
        self.add_line('text-m-0-1-4-1',(29, 10),(29, 16))
        self.add_contour('glyph-m-0-1-4',*['text-m-0-1-4-0', 'text-m-0-1-4-1'],closed=False)

        self.add_line('shaft',(2,26),(30,26))
        self.add_polyline('left-head',(6,22),(2,26),(6,30))
        self.add_polyline('right-head',(26,22),(30,26),(26,30))
        self.relate('connect','shaft','left-head-1','left-head-2','right-head-1','right-head-2')

