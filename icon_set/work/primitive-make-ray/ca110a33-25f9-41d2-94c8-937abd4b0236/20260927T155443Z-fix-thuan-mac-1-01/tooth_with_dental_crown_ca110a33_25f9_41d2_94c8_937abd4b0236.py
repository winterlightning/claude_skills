from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ca110a33-25f9-41d2-94c8-937abd4b0236"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tooth-with-dental-crown/20260927T155443Z-thuan-mac-1/reference/dental crown_ca110a33-25f9-41d2-94c8-937abd4b0236.svg"
AUTHOR = "claude-fable-5-1"


def path(s, name, start, commands, closed=False):
    """Chain of L/A/C commands into one contour. A: (end, rx, ry, sweep[, large])."""
    here = start
    members = []
    for i, (kind, end, *args) in enumerate(commands):
        k = f"{name}-{i}"
        if kind == "L":
            s.add_line(k, here, end)
        elif kind == "A":
            s.add_arc(k, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                      large_arc=args[3] if len(args) > 3 else False)
        elif kind == "C":
            s.add_bezier(k, here, (args[0], args[1], end))
        members.append(k)
        here = end
    s.add_contour(name, *members, closed=closed)
    return name


def join(s, a, b):
    s.relate("connect", a, b)
PLAN = "Molar outline (two cusps, straight walls, two rounded roots) with a stepped crown seam that rises in the middle, as in the reference cap."
CONSTRUCTION_REFERENCES = "No Lucide tooth; mirrored about x=24 with r6 shoulder arcs, r4 root tips and an r5 cleft."
OMISSIONS = "None."


class Drawing(Solo48):
    icon_id = "tooth-with-dental-crown"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("dental-crown", "capped-tooth")
    keywords = ("tooth", "dental", "crown", "cap", "molar", "dentist")

    def build(self):
        path(self, "tooth", (8, 10), [
            ("A", (14, 4), 6, 6, True), ("A", (34, 4), 10, 2, False), ("A", (40, 10), 6, 6, True),
            ("L", (40, 22)), ("L", (40, 30)), ("L", (39, 40)), ("A", (31, 40), 4, 4, True), ("L", (29, 36)),
            ("A", (19, 36), 5, 5, False), ("L", (17, 40)), ("A", (9, 40), 4, 4, True), ("L", (8, 30)),
            ("L", (8, 22)), ("L", (8, 10))], closed=True)
        path(self, "seam", (8, 22), [("L", (16, 22)), ("L", (16, 15)), ("L", (32, 15)), ("L", (32, 22)), ("L", (40, 22))])
        join(self, "seam", "tooth")
