'A figure balances on a downward arm and bent supporting leg beneath a horizontal torso. The other leg extends diagonally upward to the right, while the head projects left.\nConstruction: Bounds (6,6)-(42,42). Torso connects floor support with raised right leg; other knee bends down. Preserve asymmetric pose and remove outlined limb thickness.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75a623a7-979a-5bf4-b984-c54e5a617f21'
SOURCE_PATH = 'pictographic-primitives/sports/yoga half moon pose_75a623a7-979a-5bf4-b984-c54e5a617f21.svg'
AUTHOR = 'gpt-6'

class RaisedLegFloorBalance(Solo48):
    icon_id = 'raised-leg-floor-balance'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ()
    keywords = ('raised', 'leg', 'floor', 'balance', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (6, 18), (12, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (12, 18), (6, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (21, 42), (21, 25), (30, 25), (42, 6), closed=False)
        self.add_polyline('support-leg', (30, 25), (30, 42), (42, 42), closed=False)
        self.relate("connect", 'body', 'support-leg')
