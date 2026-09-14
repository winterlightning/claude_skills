'An inverted person spreads both legs upward and arms outward.\nConstruction: Vertical centerlines (8,6)-(40,42). Mirror limbs around x24; simplify torso outline into one connected stroke.\nLucide: accessibility: circular head and articulated open limbs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc035e5f-5b48-4659-93ae-3cdb21c1bf16'
SOURCE_PATH = 'pictographic-primitives/sports/wide seat inversion pose_cc035e5f-5b48-4659-93ae-3cdb21c1bf16.svg'
AUTHOR = 'gpt-6'

class WideLegInversionPose(Solo48):
    icon_id = 'wide-leg-inversion-pose'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('wide', 'leg', 'inversion', 'pose', 'sport')

    def build(self):
        self.add_polyline('legs', (8, 6), (24, 22), (40, 6), closed=False)
        self.add_line('torso', (24, 22), (24, 28))
        self.relate("connect", 'legs', 'torso')
        self.add_polyline('arms', (8, 33), (24, 28), (40, 33), closed=False)
        self.relate("connect", 'arms', 'torso')
        self.add_arc('head-top', (21, 41), (27, 41), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 41), (21, 41), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
