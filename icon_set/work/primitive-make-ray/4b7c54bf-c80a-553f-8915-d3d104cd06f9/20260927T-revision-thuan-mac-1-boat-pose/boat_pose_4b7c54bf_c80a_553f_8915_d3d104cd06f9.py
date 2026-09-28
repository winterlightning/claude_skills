'A seated figure leans back while lifting the legs diagonally upward to the right. The arms reach forward above the legs, forming a compact open V around the bent torso.\nConstruction: Bounds (6,6)-(42,42). Clear V of leaning back and raised legs, arms reach ahead. Remove doubled legs and fingers; asymmetric side view.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4b7c54bf-c80a-553f-8915-d3d104cd06f9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__boat-pose/20260927T152212Z-thuan-mac-1/reference/yoga boat stretching pose_4b7c54bf-c80a-553f-8915-d3d104cd06f9.svg'
AUTHOR = "gpt-6"

class BoatPose(Solo48):
    icon_id = 'boat-pose'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('boat', 'pose', 'yoga', 'exercise')

    def build(self):
        # A larger detached head, leaning torso, raised leg and reaching arm.
        self.add_arc('head-top',(6,11),(16,11),radius_x=5,radius_y=5,sweep=True)
        self.add_arc('head-bottom',(16,11),(6,11),radius_x=5,radius_y=5,sweep=True)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_bezier('torso',(16,23),((18,30),(22,37),(26,42)))
        self.add_bezier('raised-legs',(26,42),((30,41),(36,31),(42,24)))
        self.add_line('arm',(16,23),(34,17))
        self.relate('connect','torso','raised-legs')
        self.relate('connect','torso','arm')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
