'A figure sits upright with two crossed legs beneath a rounded torso. Both arms curve inward toward the abdomen, leaving a small central gap below the circular head.\nConstruction: Bounds (6,6)-(42,42). Mirrored arms curve inward over crossed legs; remove double limb contours and fingers.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ded0b984-4a7d-5b44-8214-e8c48cf563e0'
SOURCE_PATH = 'pictographic-primitives/sports/yoga meditate_ded0b984-4a7d-5b44-8214-e8c48cf563e0.svg'
AUTHOR = 'gpt-6'

class SeatedMeditationCurvedArms(Solo48):
    icon_id = 'seated-meditation-curved-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('seated', 'meditation', 'curved', 'arms', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_arc('shoulder-l', (10, 28), (24, 21), radius_x=14, radius_y=7, sweep=True)
        self.add_arc('shoulder-r', (24, 21), (38, 28), radius_x=14, radius_y=7, sweep=True)
        self.add_contour('shoulders', 'shoulder-l', 'shoulder-r', closed=False)
        self.add_polyline('arm-l', (10, 28), (10, 32), (18, 32), closed=False)
        self.add_polyline('arm-r', (38, 28), (38, 32), (30, 32), closed=False)
        self.relate("connect", 'shoulders', 'arm-l')
        self.relate("connect", 'shoulders', 'arm-r')
        self.add_line('torso', (24, 21), (24, 38))
        self.relate("connect", 'shoulders', 'torso')
        self.add_polyline('leg-l', (6, 34), (24, 38), (42, 42), closed=False)
        self.add_polyline('leg-r', (42, 34), (24, 38), (6, 42), closed=False)
        self.relate("connect", 'leg-l', 'leg-r')
        self.relate("connect", 'torso', 'leg-l')
        self.relate("connect", 'torso', 'leg-r')
