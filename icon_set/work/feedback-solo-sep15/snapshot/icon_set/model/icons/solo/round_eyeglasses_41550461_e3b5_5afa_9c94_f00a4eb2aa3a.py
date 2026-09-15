"""Oval eyeglasses with matched lenses, an arched bridge and unfolded temples.
Lucide glasses informs the paired lenses and open arms. HRECT_L ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41550461-e3b5-5afa-9c94-f00a4eb2aa3a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/glasses retro_41550461-e3b5-5afa-9c94-f00a4eb2aa3a.svg'
AUTHOR = 'gpt-6'


class RoundEyeglasses(Solo48):
    icon_id = 'round-eyeglasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('round', 'eyeglasses')

    def build(self) -> None:
        # Open temples reach y=8; paired lenses end at y=40. HRECT_L ink
        # (2,6)-(46,42). Keep the lens proportions while unfolding the arms.
        radius_x, radius_y = 8, 10
        lens_y = 40 - radius_y
        for side, cx in (('left', 12), ('right', 36)):
            self.add_arc(side+'-lens-top', (cx-radius_x,lens_y), (cx+radius_x,lens_y),
                         radius_x=radius_x, radius_y=radius_y)
            self.add_arc(side+'-lens-bottom', (cx+radius_x,lens_y), (cx-radius_x,lens_y),
                         radius_x=radius_x, radius_y=radius_y)
            self.add_contour(side+'-lens', side+'-lens-top', side+'-lens-bottom', closed=True)
        self.add_arc('bridge', (20,lens_y), (28,lens_y), radius_x=4, radius_y=4)
        self.add_polyline('temple-left', (4,lens_y), (4,16), (8,8))
        self.add_polyline('temple-right', (44,lens_y), (44,16), (40,8))
        self.relate('connect', 'left-lens', 'bridge')
        self.relate('connect', 'right-lens', 'bridge')
        self.relate('connect', 'left-lens', 'temple-left')
        self.relate('connect', 'right-lens', 'temple-right')

