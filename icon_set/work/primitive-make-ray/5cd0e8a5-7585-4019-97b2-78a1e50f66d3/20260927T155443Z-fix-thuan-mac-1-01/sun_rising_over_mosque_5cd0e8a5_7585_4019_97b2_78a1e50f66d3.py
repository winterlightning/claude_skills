from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5cd0e8a5-7585-4019-97b2-78a1e50f66d3"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__sun-rising-over-mosque/20260927T155443Z-thuan-mac-1/reference/islamic new year_5cd0e8a5-7585-4019-97b2-78a1e50f66d3.svg"
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
PLAN = "Sun half-disc with two side rays above an onion dome on straight walls, an S-curved minaret at each side, all on a ground line."
CONSTRUCTION_REFERENCES = "Lucide sunrise: open solar arc with detached rays on the horizon line; dome authored as two mirrored arcs meeting at a point."
OMISSIONS = "Diagonal rays and dome window dropped for clearance."


class Drawing(Solo48):
    icon_id = "sun-rising-over-mosque"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("islamic-new-year", "mosque-sunrise")
    keywords = ("sun", "rising", "mosque", "dome", "minaret", "islamic", "new year")

    def build(self):
        self.add_arc("sun", (18, 12), (30, 12), radius_x=6)
        self.add_line("ray-left", (6, 12), (9, 12))
        self.add_line("ray-right", (39, 12), (42, 12))
        path(self, "dome", (17, 42), [("L", (17, 34)), ("A", (24, 22), 10, 10, True), ("A", (31, 34), 10, 10, True), ("L", (31, 42))])
        path(self, "ground", (6, 42), [("L", (17, 42)), ("L", (31, 42)), ("L", (42, 42))])
        join(self, "dome", "ground")
        self.add_bezier("minaret-left", (6, 42), ((6, 38), (8, 36), (8, 32)), ((8, 29), (6, 29), (6, 27)))
        self.add_bezier("minaret-right", (42, 42), ((42, 38), (40, 36), (40, 32)), ((40, 29), (42, 29), (42, 27)))
        join(self, "ground", "minaret-left"); join(self, "ground", "minaret-right")
