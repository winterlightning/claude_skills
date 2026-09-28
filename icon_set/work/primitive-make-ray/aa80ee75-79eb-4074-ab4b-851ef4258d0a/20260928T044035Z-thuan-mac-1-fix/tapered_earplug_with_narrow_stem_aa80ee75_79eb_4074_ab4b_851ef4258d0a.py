"""Tapered foam earplug with a narrow stem, on a 45-degree axis.

Plan: SQUARE. Cap tube along (1,-1): r10 end arc about (32,16) with 6-8-10 endpoints
(26,8) and (40,22) (top y=6, right x=42 exact), side lines x+y=34 and x+y=62 down to
the flat base (16,18)-(30,32). A single-stroke stem runs from the base centre (23,25)
to (6,42) on x+y=48, 9.9 from each cap side.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "aa80ee75-79eb-4074-ab4b-851ef4258d0a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tapered-earplug-with-narrow-stem/20260928T042745Z-thuan-mac-1/reference/earplug_aa80ee75-79eb-4074-ab4b-851ef4258d0a.svg"
AUTHOR = "claude-opus-5-5"


class TaperedEarplugWithNarrowStem(Solo48):
    icon_id = "tapered-earplug-with-narrow-stem"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('ear plug', 'foam earplug')
    keywords = ('earplug', 'ear', 'hearing', 'noise', 'sleep', 'protection')

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

        self.path("cap", (26, 8), [
            ("A", (40, 22), 10, 10, True, False),
            ("L", (30, 32)), ("L", (23, 25)), ("L", (16, 18)), ("L", (26, 8)),
        ], closed=True)
        self.add_line("stem", (23, 25), (6, 42))
        self.relate("connect", "stem", "cap")
