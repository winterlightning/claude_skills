'A seated figure leans back while lifting the legs diagonally upward to the right. The arms reach forward above the legs, forming a compact open V around the bent torso.\nConstruction: Bounds (6,6)-(42,42). Clear V of leaning back and raised legs, arms reach ahead. Remove doubled legs and fingers; asymmetric side view.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4b7c54bf-c80a-553f-8915-d3d104cd06f9'
SOURCE_PATH = 'pictographic-primitives/sports/yoga boat stretching pose_4b7c54bf-c80a-553f-8915-d3d104cd06f9.svg'
AUTHOR = 'gpt-6'

class BoatPose(Solo48):
    icon_id = 'boat-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('boat', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (6, 9), (12, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (12, 9), (6, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (15, 21), (26, 42), (42, 24), closed=False)
        self.add_polyline('arms', (15, 21), (31, 13), closed=False)
        self.relate("connect", 'body', 'arms')
