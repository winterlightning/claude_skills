"""Tall crescent moon with three sparkles.

Plan: SQUARE. Crescent = two cubics with tips (18,6),(18,42): outer controls (2,6),(2,42)
give the exact extreme x=6; inner controls (11,42),(11,6) reach x=12.75 (6.75 thick).
Two 14-wide four-point sparkles at (35,13) and (35,35): 7-unit arms with gently concave
cubic sides (large_four_point_sparkle construction) and a 6-unit facing arm so their
tips stay 10 apart. The small middle sparkle is a dot at (24,24): a 4-point star under
12 units cannot hold a 6-unit hole, and a 12-unit one cannot clear the moon's hollow.
Mirror-symmetric about y=24.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "918bf38d-d107-4261-bb49-0141b95866e7"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tall-crescent-with-three-sparkles/20260928T042745Z-thuan-mac-1/reference/astronomy moon_918bf38d-d107-4261-bb49-0141b95866e7.svg"
AUTHOR = "claude-opus-5-5"


class TallCrescentWithThreeSparkles(Solo48):
    icon_id = "tall-crescent-with-three-sparkles"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('moon and stars', 'night sky')
    keywords = ('astronomy', 'moon', 'crescent', 'sparkle', 'star', 'night')

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

        self.path("moon", (18, 6), [("C", (18, 42), (2, 6), (2, 42)), ("C", (18, 6), (11, 42), (11, 6))], closed=True)

        def sparkle(name, cx, cy, arms):
            # arms: (up, right, down, left); each side is a cubic whose controls sit at the
            # 2/4 marks of the arm lengths, pulled about half a unit toward the centre.
            up, right, down, left = arms
            tips = [(cx, cy - up), (cx + right, cy), (cx, cy + down), (cx - left, cy)]
            steps = []
            for j in range(4):
                a, b = tips[j], tips[(j + 1) % 4]
                ax, ay = a[0] - cx, a[1] - cy
                bx, by = b[0] - cx, b[1] - cy
                sx = 2 if ax == 0 else (2 if ax > 0 else -2)
                # control 1: two units from tip a along its axis, four toward b
                def u(v): return 0 if v == 0 else (1 if v > 0 else -1)
                c1 = (cx + u(ax) * 2 + u(bx) * 4, cy + u(ay) * 2 + u(by) * 4)
                c2 = (cx + u(ax) * 4 + u(bx) * 2, cy + u(ay) * 4 + u(by) * 2)
                steps.append(("C", b, c1, c2))
            self.path(name, tips[0], steps, closed=True)

        sparkle("sparkle-top", 35, 13, (7, 7, 6, 7))
        sparkle("sparkle-bottom", 35, 35, (6, 7, 7, 7))
        self.add_dot("sparkle-mid", (24, 24))
