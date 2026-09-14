"""Round glasses with matched lenses and arched bridge. Lucide glasses informs repeated circles; tiny temple stubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '470b6a50-6961-58f3-a538-29fd0c973118'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/glasses_470b6a50-6961-58f3-a538-29fd0c973118.svg'
AUTHOR = 'gpt-6'

class RoundGlasses(Solo48):
    icon_id = 'round-glasses'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('round', 'glasses')

    def build(self) -> None:
        # Open temples reach y=8; paired lenses end at y=40. HRECT_L ink
        # (2,6)-(46,42). Keep the lens proportions while unfolding the arms.
        radius_x, radius_y = 8, 8
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

