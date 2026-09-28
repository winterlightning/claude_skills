from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "67dfb976-0aa9-5cc7-9624-2dcd7cf3a60c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tooth-with-dental-floss/20260927T155443Z-thuan-mac-1/reference/dental floss tooth_67dfb976-0aa9-5cc7-9624-2dcd7cf3a60c.svg"
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
PLAN = "Molar (two cusps, straight walls, two rounded root lobes) with a floss strand through its middle whose ends leave the walls tangentially and curl down on both sides."
CONSTRUCTION_REFERENCES = "No Lucide tooth; mirrored about x=24, r5 shoulders, r4 root tips meeting an r5 cleft; strand splits both walls."
OMISSIONS = "Roots shortened to lobes so the strand clears the cleft; the ends curl symmetrically instead of the reference's uneven curls."


class Drawing(Solo48):
    icon_id = "tooth-with-dental-floss"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("dental-floss-tooth", "flossing")
    keywords = ("tooth", "dental", "floss", "flossing", "molar", "hygiene")

    def build(self):
        path(self, "tooth", (11, 13), [
            ("A", (16, 8), 5, 5, True), ("A", (32, 8), 8, 2, False), ("A", (37, 13), 5, 5, True),
            ("L", (37, 22)), ("L", (37, 36)), ("A", (29, 36), 4, 4, True), ("A", (19, 36), 5, 5, False),
            ("A", (11, 36), 4, 4, True), ("L", (11, 22)), ("L", (11, 13))], closed=True)
        path(self, "floss", (4, 29), [("A", (11, 22), 7, 7, True), ("L", (37, 22)), ("A", (44, 29), 7, 7, True)])
        join(self, "floss", "tooth")
