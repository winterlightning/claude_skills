from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "638d5134-5ea9-476e-996b-afb066e33fd9"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tooth-with-trailing-floss/20260927T155443Z-thuan-mac-1/reference/tooth_638d5134-5ea9-476e-996b-afb066e33fd9.svg"
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
PLAN = "Tall molar on the left (two cusps, straight walls, two rounded root lobes with a cleft); a floss strand leaves the right shoulder in a quarter arc and trails straight down the right edge."
CONSTRUCTION_REFERENCES = "No Lucide tooth; strand is an r10 quarter arc centred (32,26) leaving the wall perpendicular, then a vertical run."
OMISSIONS = "End curl of the strand dropped: it cannot clear the right root lobe."


class Drawing(Solo48):
    icon_id = "tooth-with-trailing-floss"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("tooth-floss-strand",)
    keywords = ("tooth", "floss", "strand", "dental", "molar", "hygiene")

    def build(self):
        path(self, "tooth", (6, 12), [
            ("A", (12, 6), 6, 6, True), ("A", (26, 6), 7, 2, False), ("A", (32, 12), 6, 6, True),
            ("L", (32, 16)), ("L", (32, 30)), ("L", (32, 38)), ("A", (24, 38), 4, 4, True), ("A", (14, 38), 5, 5, False),
            ("A", (6, 38), 4, 4, True), ("L", (6, 12))], closed=True)
        path(self, "floss", (32, 16), [("A", (42, 26), 10, 10, True), ("L", (42, 42))])
        join(self, "floss", "tooth")
