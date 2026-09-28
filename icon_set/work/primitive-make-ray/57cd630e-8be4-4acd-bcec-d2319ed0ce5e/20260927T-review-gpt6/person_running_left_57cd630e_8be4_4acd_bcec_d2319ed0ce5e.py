"""Left-facing runner with a forward arm, separated legs, and two trailing speed marks. Human proportions follow icon_set/references/human_ref/full_body_ref.png; Lucide construction: no useful exact subject match found."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID="57cd630e-8be4-4acd-bcec-d2319ed0ce5e"
SOURCE_PATH="icon_set/work/primitive-fix-thuan/solo__person-running-left/20260926T171117Z-thuan-mac-1/reference/safety fire exit_57cd630e-8be4-4acd-bcec-d2319ed0ce5e.svg"
AUTHOR="gpt-6"
class PersonRunningLeft(Solo48):
    icon_id="person-running-left"
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="wayfinding"
    aliases=()
    keywords=("running", "person", "left", "speed", "escape", "motion")
    def build(self):
        self.add_arc("head-upper",(11,11),(21,11),radius_x=5)
        self.add_arc("head-lower",(21,11),(11,11),radius_x=5)
        self.add_contour("head","head-upper","head-lower",closed=True)
        self.add_line("torso-upper",(16,24),(16,30))
        self.add_line("torso-lower",(16,30),(22,31))
        self.add_polyline("arm-forward",(16,25),(10,23),(6,25))
        self.add_polyline("arm-back",(16,25),(22,23),(27,25))
        self.add_polyline("leg-forward",(16,30),(10,34),(6,42))
        self.add_polyline("leg-back",(16,30),(24,34),(34,38),(42,38))
        self.add_line("speed-upper",(35,16),(42,16))
        self.add_line("speed-lower",(35,27),(42,27))
        for limb in ("arm-forward","arm-back"):
            self.relate("connect",limb,"torso-upper")
        for limb in ("leg-forward","leg-back"):
            self.relate("connect",limb,"torso-lower")
        self.relate("connect","torso-upper","torso-lower")
        self.mark_human_figure("person",head="head",torso="torso-upper",torso_junction="start")
