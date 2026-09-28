'Left-facing witch with a gently curved pointed hat, hooked nose, rounded chin and flowing hair.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg reviewed for head proportions; source retains a continuous profile neck.\nOmissions: Eye, small folded hat notch and hair strand details omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '60df543d-dca5-4914-a5c9-114df422b161'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__witch-in-pointed-hat/20260927T140835Z-thuan-mac-1/reference/witch_60df543d-dca5-4914-a5c9-114df422b161.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id='witch-in-pointed-hat'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases=()
    keywords=('witch', 'in', 'pointed', 'hat')
    def build(self):
        # Crooked brim and long nose make the reference a witch profile rather
        # than a generic peaked hat. The single far hair lock stays separate.
        self.add_polyline('hat',(6,20),(30,6),(42,20),(36,20),(18,20),(6,20),closed=True)
        self.add_line('face-upper',(18,20),(18,27))
        self.add_bezier('nose',(18,27),((17,29),(11,29),(10,31)))
        self.add_bezier('jaw',(10,31),((15,32),(12,38),(22,42)))
        self.add_contour('profile','face-upper','nose','jaw')
        self.add_bezier('hair',(36,20),((33,28),(35,36),(40,42)))
        self.relate('connect','hat','profile')
        self.relate('connect','hat','hair')
