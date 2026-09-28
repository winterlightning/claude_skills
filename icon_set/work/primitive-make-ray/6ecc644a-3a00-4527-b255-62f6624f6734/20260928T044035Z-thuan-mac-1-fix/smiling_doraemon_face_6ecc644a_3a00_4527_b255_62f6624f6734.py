"""Doraemon face: round head, two large touching ring eyes, philtrum and wide smile.

Plan: CIRCLE, rim r20 about (24,24); everything inside stays within r12 of the centre.
Eyes are two r4 rings sharing the point (24,18) (touching, as on Doraemon). The
philtrum drops from (24,30) into the apex of a r10 smile about (24,25). Whiskers and
the red nose ball cannot keep 8 units from the eyes/rim at this size and are omitted;
the philtrum's round cap stands in for the nose. Mirror-symmetric about x=24.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6ecc644a-3a00-4527-b255-62f6624f6734"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__smiling-doraemon-face/20260928T042745Z-thuan-mac-1/reference/robot cat blue doraemon_6ecc644a-3a00-4527-b255-62f6624f6734.svg"
AUTHOR = "claude-opus-5-5"


class SmilingDoraemonFace(Solo48):
    icon_id = "smiling-doraemon-face"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('doraemon', 'robot cat')
    keywords = ('doraemon', 'robot', 'cat', 'blue', 'face', 'smile', 'anime')

    def path(self, name, start, steps, closed=False):
        here, members = start, []
        for j, (kind, end, *args) in enumerate(steps):
            member = f"{name}-{j}"
            if kind == "L":
                self.add_line(member, here, end)
            elif kind == "A":
                self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                             large_arc=args[3] if len(args) > 3 else False)
            else:
                self.add_bezier(member, here, (args[0], args[1], end))
            here = end
            members.append(member)
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        pts = [(cx - r, cy), (cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        self.path(name, pts[0], [("A", p, r, r, True) for p in pts[1:]], closed=True)

    def figure(self, fid, cx, head_y, hr, arm_half, hip_y, foot_y, foot_half):
        """Shared stick figure (icon_set/references/human_ref/full_body_ref.png, T-pose):
        cardinal-arc head, a 2-unit neck run exactly 8 below the head, arms branching at the
        neck's lower end, a torso-lean to the hip and a V of legs."""
        neck_top = head_y + hr + 8
        self.circle(f"{fid}-head", cx, head_y, hr)
        self.add_line(f"{fid}-torso", (cx, neck_top), (cx, neck_top + 2))
        y = neck_top + 2
        self.add_line(f"{fid}-arm-l", (cx - arm_half, y), (cx, y))
        self.add_line(f"{fid}-arm-r", (cx, y), (cx + arm_half, y))
        self.add_line(f"{fid}-torso-lean", (cx, y), (cx, hip_y))
        self.add_polyline(f"{fid}-legs", (cx - foot_half, foot_y), (cx, hip_y), (cx + foot_half, foot_y))
        for a, b in ((f"{fid}-torso", f"{fid}-arm-l"), (f"{fid}-torso", f"{fid}-arm-r"),
                     (f"{fid}-torso", f"{fid}-torso-lean"), (f"{fid}-arm-l", f"{fid}-arm-r"),
                     (f"{fid}-arm-l", f"{fid}-torso-lean"), (f"{fid}-arm-r", f"{fid}-torso-lean"),
                     (f"{fid}-torso-lean", f"{fid}-legs")):
            self.relate("connect", a, b)
        self.mark_human_figure(fid, head=f"{fid}-head", torso=f"{fid}-torso", torso_junction="start")

    def build(self) -> None:

        self.circle("head", 24, 24, 20)
        self.circle("eye-l", 20, 18, 4)
        self.circle("eye-r", 28, 18, 4)
        for a in ("eye-l-1", "eye-l-2"):
            for b in ("eye-r-0", "eye-r-3"):
                self.relate("connect", a, b)
        self.add_line("philtrum", (24, 30), (24, 35))
        self.add_arc("smile-l", (16, 31), (24, 35), radius_x=10, sweep=False)
        self.add_arc("smile-r", (24, 35), (32, 31), radius_x=10, sweep=False)
        self.add_contour("smile", "smile-l", "smile-r")
        self.relate("connect", "philtrum", "smile")
