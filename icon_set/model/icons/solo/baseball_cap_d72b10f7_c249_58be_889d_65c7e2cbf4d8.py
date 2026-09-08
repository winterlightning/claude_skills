"""A left-facing baseball cap with a long curved peak and one panel seam; top button omitted."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd72b10f7-c249-58be-889d-65c7e2cbf4d8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/cap_d72b10f7-c249-58be-889d-65c7e2cbf4d8.svg'
AUTHOR = 'astra-chatgpt'


class BaseballCap(Solo48):
    icon_id = 'baseball-cap'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('cap', 'baseball cap', 'hat', 'peak', 'brim', 'sports', 'headwear', 'clothing')

    def build(self) -> None:
        # HRECT_L: authored directly to its SOLO48 centerline extremes.
        self.add_line('back', (46, 28), (46, 25))
        self.add_arc('dome-r', (46, 25), (29, 8), radius_x=17, radius_y=17, sweep=False)
        self.add_arc('dome-l', (29, 8), (12, 25), radius_x=17, radius_y=17, sweep=False)
        self.add_line('front', (12, 25), (12, 28))
        self.add_line('edge-front', (12, 28), (32, 32))
        self.add_arc('edge-back', (32, 32), (46, 28), radius_x=14, radius_y=4, sweep=False)
        self.add_contour('crown', 'back', 'dome-r', 'dome-l', 'front', 'edge-front', 'edge-back', closed=True)
        self.add_line('peak-tip', (12, 28), (2, 34))
        self.add_arc('peak-left', (2, 34), (17, 40), radius_x=15, radius_y=6, sweep=False)
        self.add_arc('peak-right', (17, 40), (32, 32), radius_x=15, radius_y=8, sweep=False)
        self.add_contour('peak', 'peak-tip', 'peak-left', 'peak-right', closed=False)
        self.relate("connect", 'peak', 'crown')
        self.add_arc('panel', (29, 8), (32, 32), radius_x=20, radius_y=20, sweep=True)
        self.relate("connect", 'panel', 'crown')
        self.relate("connect", 'panel', 'peak')
