"""A circular autonomous floor cleaner with its central lidar sensor and two paired edge brushes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="96e6e169-e425-5a01-9657-76e56fb484e5"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__robot-vacuum/20260926T171117Z-thuan-mac-1/reference/cleaning robot_96e6e169-e425-5a01-9657-76e56fb484e5.svg"
AUTHOR="gpt-6"
class RobotVacuum(Solo48):
    icon_id="robot-vacuum"
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="wayfinding"
    aliases=()
    keywords=("robot", "vacuum", "cleaning", "automatic", "floor", "appliance")
    def build(self):
        for n,a,b in (("body-upper",(6,24),(42,24)),("body-lower",(42,24),(6,24))):
            self.add_arc(n,a,b,radius_x=18,sweep=True)
        self.add_contour("body","body-upper","body-lower",closed=True)
        for n,cx,cy,r in (("lidar",24,19,4),):
            self.add_arc(n+"-upper",(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(n+"-lower",(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(n,n+"-upper",n+"-lower",closed=True)
        self.add_line("left-edge-brush",(12,36),(6,42))
        self.add_line("right-edge-brush",(36,36),(42,42))
        self.relate("connect","body","left-edge-brush")
        self.relate("connect","body","right-edge-brush")
