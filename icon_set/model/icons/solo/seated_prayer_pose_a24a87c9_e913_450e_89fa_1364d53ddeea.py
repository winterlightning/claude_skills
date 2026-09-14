'A cross-legged figure holds both hands together in a pointed prayer shape at the center of the chest. Rounded bent arms enclose the hands beneath a separate circular head.\nConstruction: Bounds (6,6)-(42,42). Joined palms at chest and paired bent elbows above crossed legs. Omit finger detail and duplicated outlines.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a24a87c9-e913-450e-89fa-1364d53ddeea'
SOURCE_PATH = 'pictographic-primitives/sports/yoga meditation pose_a24a87c9-e913-450e-89fa-1364d53ddeea.svg'
AUTHOR = 'gpt-6'

class SeatedPrayerPose(Solo48):
    icon_id = 'seated-prayer-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/sports"
    aliases = ()
    keywords = ('seated', 'prayer', 'pose', 'yoga', 'exercise')

    def build(self):
        self.add_arc('head-top', (21, 9), (27, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-bottom', (27, 9), (21, 9), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('prayer-arms', (24, 21), (10, 30), (24, 34), (38, 30), (24, 21), closed=False)
        self.add_line('palms', (24, 21), (24, 26))
        self.relate("connect", 'palms', 'prayer-arms')
        self.add_line('torso', (24, 34), (24, 38))
        self.relate("connect", 'prayer-arms', 'torso')
        self.add_polyline('leg-l', (6, 34), (24, 38), (42, 42), closed=False)
        self.add_polyline('leg-r', (42, 34), (24, 38), (6, 42), closed=False)
        self.relate("connect", 'leg-l', 'leg-r')
        self.relate("connect", 'torso', 'leg-l')
        self.relate("connect", 'torso', 'leg-r')
