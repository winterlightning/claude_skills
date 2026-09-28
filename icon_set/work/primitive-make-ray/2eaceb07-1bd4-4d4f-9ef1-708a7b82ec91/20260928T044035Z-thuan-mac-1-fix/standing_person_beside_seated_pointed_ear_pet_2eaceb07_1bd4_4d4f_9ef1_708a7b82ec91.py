"""Person standing beside a seated pointed-ear pet (cat).

Plan: SQUARE. Stick figure (full_body_ref.png T-pose) at x=12. The cat is one closed
silhouette mirrored about x=34: ear tips at the top corners (26,6),(42,6) with the
notch at (34,13), cheeks tapering to a 10-wide neck at y=22, then the seated body
flaring to the feet (26,42),(42,42). The reference's two leg lines inside the body
cannot keep 8 units from the sides and are omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2eaceb07-1bd4-4d4f-9ef1-708a7b82ec91"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__standing-person-beside-seated-pointed-ear-pet/20260928T042745Z-thuan-mac-1/reference/dog sit trainer side_2eaceb07-1bd4-4d4f-9ef1-708a7b82ec91.svg"
AUTHOR = "claude-opus-5-5"


class StandingPersonBesideSeatedPointedEarPet(Solo48):
    icon_id = "standing-person-beside-seated-pointed-ear-pet"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('dog trainer', 'person with cat')
    keywords = ('pet', 'cat', 'dog', 'sit', 'trainer', 'owner', 'person')

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

        self.figure("person", 12, 10, 4, 6, 32, 42, 6)
        self.add_polyline("cat", (26, 6), (34, 13), (42, 6), (39, 22), (42, 42), (26, 42), (29, 22), closed=True)
