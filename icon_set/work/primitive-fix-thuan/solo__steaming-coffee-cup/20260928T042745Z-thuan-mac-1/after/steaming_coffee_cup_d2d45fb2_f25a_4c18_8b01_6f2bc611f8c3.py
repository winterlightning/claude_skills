"""Steaming coffee cup on a saucer (Java logo reference).

Plan: VRECT_L (8..40 x 4..44). Cup: rim (10,23)-(32,23), walls to y=33, r2 bottom
corners, floor y=35; a half-ellipse handle rx6 ry5 on the right wall from (32,23) to
(32,33). Saucer line y=44 spans the keyshape width. Two S-shaped steam wisps at
x=15 and x=27 from y=14 up to y=4, 9 above the rim. Reference cup was a bowl; the
straight-walled cup keeps two handle attachment points 10 apart.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d2d45fb2-f25a-4c18-8b01-6f2bc611f8c3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__steaming-coffee-cup/20260928T042745Z-thuan-mac-1/reference/java logo_d2d45fb2-f25a-4c18-8b01-6f2bc611f8c3.svg"
AUTHOR = "claude-opus-5-5"


class SteamingCoffeeCup(Solo48):
    icon_id = "steaming-coffee-cup"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('java', 'coffee', 'hot drink')
    keywords = ('java', 'coffee', 'cup', 'steam', 'saucer', 'cafe', 'hot')

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

        self.path("cup", (10, 23), [("L", (32, 23)), ("L", (32, 33)), ("A", (30, 35), 2, 2, True),
                                    ("L", (12, 35)), ("A", (10, 33), 2, 2, True), ("L", (10, 23))], closed=True)
        self.add_arc("handle", (32, 23), (32, 33), radius_x=6, radius_y=5, sweep=True)
        self.relate("connect", "handle", "cup")
        self.add_line("saucer", (8, 44), (40, 44))
        for i, x in enumerate((15, 27)):
            self.add_bezier(f"steam-{i}", (x, 14), ((x + 5, 11), (x - 5, 7), (x, 4)))
