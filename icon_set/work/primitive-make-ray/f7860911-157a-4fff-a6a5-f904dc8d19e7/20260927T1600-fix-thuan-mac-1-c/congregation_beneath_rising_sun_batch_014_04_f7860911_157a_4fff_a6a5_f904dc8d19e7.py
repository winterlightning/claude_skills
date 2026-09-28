"""Congregation beneath a rising sun: three people side by side under a sun with side rays.

Revision of the disapproved drawing, whose r3 dot heads and thin sun arc read as an
alien face. Plan (HRECT_L, centerline (4,8)-(44,40)): sun dome r6 about (24,14) with
apex at 8 and two horizontal rays at y=12; three r3 heads at x=10/24/38, y=24 (8 apart
edge to edge); a continuous shoulder wave of six cubics whose apex knots (10,35),
(24,35), (38,35) sit exactly 8 below the heads with all controls on y>=35 so the
4-unit visible gap is certified by the control hull. Human reference: user.svg.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f7860911-157a-4fff-a6a5-f904dc8d19e7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__congregation-beneath-rising-sun-batch-014-04/20260927T150749Z-thuan-mac-1/reference/jumu ah_f7860911-157a-4fff-a6a5-f904dc8d19e7.svg"
AUTHOR = "claude-fable-5-1"


class CongregationBeneathRisingSun(Solo48):
    icon_id = "congregation-beneath-rising-sun-batch-014-04"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("jumu'ah", "friday congregation", "gathering at sunrise")
    keywords = ("congregation", "people", "group", "sun", "rays", "gathering", "prayer", "community")

    def build(self) -> None:
        # sun
        self.add_arc("sun-1", (18, 14), (24, 8), radius_x=6)
        self.add_arc("sun-2", (24, 8), (30, 14), radius_x=6)
        self.add_contour("sun", "sun-1", "sun-2")
        self.add_line("ray-left", (4, 12), (9, 12))
        self.add_line("ray-right", (39, 12), (44, 12))
        # heads
        for i, cx in enumerate((10, 24, 38)):
            r, cy = 3, 24
            pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r)]
            for j in range(4):
                self.add_arc(f"head-{i}-{j}", pts[j], pts[(j + 1) % 4], radius_x=r)
            self.add_contour(f"head-{i}", *(f"head-{i}-{j}" for j in range(4)), closed=True)
        # shoulders wave: feet at 4, 17, 31, 44; apexes at 10, 24, 38
        feet = [4, 17, 31, 44]
        apex = [10, 24, 38]
        members = []
        for i in range(3):
            f0, f1, a = feet[i], feet[i + 1], apex[i]
            self.add_bezier(f"shoulder-{i}-up", (f0, 40), ((f0, 35), (a - 3, 35), (a, 35)))
            self.add_bezier(f"shoulder-{i}-down", (a, 35), ((a + 3, 35), (f1, 35), (f1, 40)))
            members += [f"shoulder-{i}-up", f"shoulder-{i}-down"]
        self.add_contour("shoulders", *members)
        for i in range(3):
            self.mark_human_figure(f"person-{i}", head=f"head-{i}", torso=f"shoulder-{i}-up", torso_junction="end")
