"""Tall fashion boot with a block heel.

Plan: VRECT_L (8..40 x 4..44). One closed outline: shaft top (10,4)-(28,4), front wall
down to (28,24), instep cubic to the toe (40,38) (tangents vertical at both ends), r6
toe arc to the sole (34,44), sole to (24,44), heel notch 8 wide and 6 deep
((24,38)-(16,38)), heel block to (8,44), back wall up to (8,38) then leaning to (10,4).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ddcdb18c-a117-4e56-9306-9336b686e788"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tall-fashion-boot/20260928T042745Z-thuan-mac-1/reference/footwear boots female_ddcdb18c-a117-4e56-9306-9336b686e788.svg"
AUTHOR = "claude-fable-5-1"


class TallFashionBoot(Solo48):
    icon_id = "tall-fashion-boot"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('knee boot', "women's boot")
    keywords = ('footwear', 'boots', 'female', 'fashion', 'shoe', 'heel')

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

        self.path("boot", (10, 4), [
            ("L", (28, 4)), ("L", (28, 24)),
            ("C", (40, 38), (28, 30), (40, 30)),
            ("A", (34, 44), 6, 6, True),
            ("L", (24, 44)), ("L", (24, 38)), ("L", (16, 38)), ("L", (16, 44)),
            ("L", (8, 44)), ("L", (8, 38)), ("L", (10, 4)),
        ], closed=True)
