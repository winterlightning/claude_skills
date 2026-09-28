"""Archer standing beside a strung bow.

Plan: SQUARE. Stick figure (full_body_ref.png T-pose) on the left, head r4 at (14,10),
neck run 8 below the head, arms at y=24, hip 32, feet 42. The bow is a r17 arc about
(25,24) from (33,9) to (33,39) reaching x=42, with its string as the chord; the string
stays 11 from the arm tip. The reference bow had no visible string; one is added so
the arc reads as a bow rather than a bracket.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "291a797f-930c-4cb5-8b07-bb037ee2bfae"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__standing-archer-beside-a-bow/20260928T042745Z-thuan-mac-1/reference/archery person_291a797f-930c-4cb5-8b07-bb037ee2bfae.svg"
AUTHOR = "claude-opus-5-5"


class StandingArcherBesideABow(Solo48):
    icon_id = "standing-archer-beside-a-bow"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('archery', 'bowman')
    keywords = ('archery', 'archer', 'bow', 'person', 'sport', 'target')

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

        self.figure("person", 14, 10, 4, 8, 32, 42, 6)
        self.add_arc("bow-limb", (33, 9), (33, 39), radius_x=17, sweep=True)
        self.add_line("bow-string", (33, 39), (33, 9))
        self.add_contour("bow", "bow-limb", "bow-string", closed=True)
