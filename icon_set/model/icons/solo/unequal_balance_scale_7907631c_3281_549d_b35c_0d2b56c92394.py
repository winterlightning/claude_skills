"""A balance scale stands on a central upright and low foot, with its crossbeam sloping down to the right. Two hanging bowls have triangular suspension lines, and the right bowl hangs lower.
Lucide scale suspension triangles and curved bowls. Right pan sits lower; shared pan dimensions preserve equal construction with an unequal beam angle.
HRECT_L: centerline extremes (6,8)-(42,40); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7907631c-3281-549d-b35c-0d2b56c92394'
SOURCE_PATH = 'pictographic-primitives/work/legal scale unequal_7907631c-3281-549d-b35c-0d2b56c92394.svg'
AUTHOR = 'gpt-6'

class UnequalBalanceScale(Solo48):
    icon_id = 'unequal-balance-scale'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('scale', 'balance', 'unequal', 'justice', 'weighing', 'legal')

    def build(self) -> None:
        """Opening repair: Removed the redundant horizontal pan dividers, leaving two clear bowl-and-suspension contours."""
        self.add_polyline('upright', (24, 8), (24, 13), (24, 40), closed=False)
        self.add_polyline('foot', (16, 40), (24, 40), (32, 40), closed=False)
        self.relate('connect', 'upright', 'foot')
        self.add_polyline('beam', (10, 10), (24, 13), (38, 16), closed=False)
        self.relate('connect', 'beam', 'upright')
        self.add_polyline('left-suspension', (6, 24), (10, 10), (16, 24), closed=False)
        self.add_arc('left-pan', (16, 24), (6, 24), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.relate('connect', 'left-suspension', 'left-pan')
        self.relate('connect', 'left-suspension', 'beam')
        self.add_polyline('right-suspension', (32, 30), (38, 16), (42, 30), closed=False)
        self.add_arc('right-pan', (42, 30), (32, 30), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.relate('connect', 'right-suspension', 'right-pan')
        self.relate('connect', 'right-suspension', 'beam')
