"""Teacher presenting at a whiteboard.

Plan: SQUARE. Bust-with-body figure on the left (human_ref/user.svg shoulders): head r4
at (12,11), shoulder arch of two r6 arcs about (12,30) with its top (12,24) 9 below the
head, straight sides down to y=42. Whiteboard: rounded rectangle (27,6)-(42,34), r3
corners, 9 clear of the shoulder. The reference has no pointing arm; none is drawn.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f091c14d-74b4-4dd3-a7fb-33b15684ee95"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__teacher-presenting-at-whiteboard-batch-003/20260928T042745Z-thuan-mac-1/reference/teacher shool_f091c14d-74b4-4dd3-a7fb-33b15684ee95.svg"
AUTHOR = "claude-fable-5-1"


class TeacherPresentingAtWhiteboardBatch003(Solo48):
    icon_id = "teacher-presenting-at-whiteboard-batch-003"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('lecturer', 'presenter')
    keywords = ('teacher', 'school', 'whiteboard', 'presentation', 'lesson', 'class')

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

        self.circle("head", 12, 11, 4)
        self.path("body", (6, 42), [("L", (6, 30)), ("A", (12, 24), 6, 6, True), ("A", (18, 30), 6, 6, True), ("L", (18, 42))])
        r = 3
        self.path("board", (30, 6), [("L", (39, 6)), ("A", (42, 9), r, r, True), ("L", (42, 31)), ("A", (39, 34), r, r, True),
                                     ("L", (30, 34)), ("A", (27, 31), r, r, True), ("L", (27, 9)), ("A", (30, 6), r, r, True)], closed=True)
