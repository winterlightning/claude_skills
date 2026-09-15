'A seated figure leans backward with both arms reaching diagonally up-right and the legs lifted in the same direction. The curved lower torso forms the base of an open V-shaped balance.\nConstruction: Bounds (6,6)-(42,42). Backward leaning torso and lifted legs form V; arms reach higher than batch-12 boat pose. Remove redundant outlines; preserve diagonal side view.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0692252-7dbb-4ed1-8ecb-dd659f3bd9b0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga stretch_e0692252-7dbb-4ed1-8ecb-dd659f3bd9b0.svg'
AUTHOR = 'gpt-6'

class BoatPoseUpwardReach(Solo48):
    icon_id = 'boat-pose-upward-reach'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('boat', 'pose', 'upward', 'reach', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (6, 20), (12, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (12, 20), (6, 20), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (18, 30), (27, 42), (42, 23), closed=False)
        self.add_polyline('reaching-arms', (18, 30), (29, 6), closed=False)
        self.relate("connect", 'body', 'reaching-arms')
