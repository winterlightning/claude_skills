'A figure sits upright with the legs crossed broadly in front. The arms extend down along the rounded torso, while a plain circular head sits centered above the shoulders.\nConstruction: Bounds (6,6)-(42,42). Shared axis with resting arms and broad crossed legs; simplify rounded torso outline into connected limb strokes. Equivalent source compositions share the same construction.\nLucide person-standing: separate circular head, shared shoulder and hip nodes; accessibility: bent limb runs. Pose direction follows the supplied reference.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'da87e4f0-75c3-43bf-bec0-675953355d74'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seated-meditation-broad-cross/20260927T091411Z-thuan-mac-1/reference/yoga meditation pose_da87e4f0-75c3-43bf-bec0-675953355d74.svg'
AUTHOR = "gpt-6"

class SeatedMeditationBroadCross(Solo48):
    icon_id = 'seated-meditation-broad-cross'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    categories = ("sports", "primitives")
    aliases = ()
    keywords = ('seated', 'meditation', 'broad', 'cross', 'yoga', 'exercise')

    # Revision plan: Replace the stiff trapezoid and straight X with a rounded upright torso and two curved crossed knees. Full body human reference governs the head and pose; Lucide person-standing informs shared joints.
    def build(self):
        # The head follows the torso axis; centerline gap to the shoulder is 9.
        self.add_arc('head-top', (20, 10), (28, 10), radius_x=4, sweep=True)
        self.add_arc('head-bottom', (28, 10), (20, 10), radius_x=4, sweep=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_bezier('shoulder-left', (6, 34), ((7, 27), (11, 22), (16, 22)))
        self.add_line('shoulder-top', (16, 22), (32, 22))
        self.add_bezier('shoulder-right', (32, 22), ((37, 22), (41, 27), (42, 34)))
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-top', 'shoulder-right')
        self.add_line('torso', (24, 22), (24, 38))
        self.relate('connect', 'shoulders', 'torso')
        self.add_bezier('left-knee', (6, 34), ((12, 32), (19, 37), (24, 38)))
        self.add_line('left-foot', (24, 38), (42, 42))
        self.add_contour('crossed-left', 'left-knee', 'left-foot')
        self.add_bezier('right-knee', (42, 34), ((36, 32), (29, 37), (24, 38)))
        self.add_line('right-foot', (24, 38), (6, 42))
        self.add_contour('crossed-right', 'right-knee', 'right-foot')
        self.relate('connect', 'shoulders', 'crossed-left')
        self.relate('connect', 'shoulders', 'crossed-right')
        self.relate('connect', 'torso', 'crossed-left')
        self.relate('connect', 'torso', 'crossed-right')
        self.relate('connect', 'crossed-left', 'crossed-right')
        self.mark_human_figure('person', head='head', torso='torso', torso_junction='start')
