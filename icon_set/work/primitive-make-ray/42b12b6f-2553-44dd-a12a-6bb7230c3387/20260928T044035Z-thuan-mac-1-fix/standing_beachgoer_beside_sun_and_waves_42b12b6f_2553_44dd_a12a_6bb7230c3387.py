"""Beachgoer standing beside a sun and a wave.

Plan: SQUARE. Stick figure (full_body_ref.png T-pose) at x=10 with 4-unit arms so the
sun's rays clear it. Sun: r3 ring at (32,16) with four diagonal rays from radius 11.3
to 14.1 (tips at the keyshape corners (42,6),(42,26),(22,6),(22,26)). One wave of two
tangent cubics along y=39 (crest 36, trough 42) under the sun. The reference's second
wave and the sun's cardinal rays do not fit at 8-unit spacing and are omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "42b12b6f-2553-44dd-a12a-6bb7230c3387"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__standing-beachgoer-beside-sun-and-waves/20260928T042745Z-thuan-mac-1/reference/beach activitiies_42b12b6f-2553-44dd-a12a-6bb7230c3387.svg"
AUTHOR = "claude-opus-5-5"


class StandingBeachgoerBesideSunAndWaves(Solo48):
    icon_id = "standing-beachgoer-beside-sun-and-waves"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('beach', 'sunbather')
    keywords = ('beach', 'sun', 'waves', 'sea', 'holiday', 'summer', 'person')

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

        self.figure("person", 10, 10, 4, 4, 32, 42, 4)
        self.circle("sun", 32, 16, 3)
        for i, (sx, sy) in enumerate(((1, -1), (1, 1), (-1, -1), (-1, 1))):
            self.add_line(f"ray-{i}", (32 + 8 * sx, 16 + 8 * sy), (32 + 10 * sx, 16 + 10 * sy))
        self.path("wave", (22, 39), [("C", (32, 39), (25, 35), (29, 35)), ("C", (42, 39), (35, 43), (39, 43))])
