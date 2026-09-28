from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "49d9fd72-8a7d-597e-816c-4096337fbbd2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tilted-champagne-bottle-in-flared-bucket/20260927T155443Z-thuan-mac-1/reference/champagne cooler_49d9fd72-8a7d-597e-816c-4096337fbbd2.svg"
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
PLAN = "Flared bucket (trapezoid) with a bottle leaning up-right out of it: body sides on a 1:2 diagonal, perpendicular shoulder, single-stroke neck with a foil cap bar."
CONSTRUCTION_REFERENCES = "Lucide wine bottle: shoulder narrowing to a neck; diagonal frame keeps every gap at 8.9 on centerlines."
OMISSIONS = "Bucket rim band dropped: an 8-unit band leaves no room for the base within the 14-unit bucket."


class Drawing(Solo48):
    icon_id = "tilted-champagne-bottle-in-flared-bucket"
    semantic_role = "MAIN"
    semantic_kind = "noun"
    keyshape = Keyshape.SQUARE
    category = "drinks"
    aliases = ("champagne-cooler", "ice-bucket-champagne")
    keywords = ("champagne", "bottle", "ice", "bucket", "cooler", "celebration")

    def build(self):
        path(self, "bucket", (6, 28), [("L", (12, 42)), ("L", (36, 42)), ("L", (42, 28)), ("L", (34, 28)), ("L", (6, 28))], closed=True)
        path(self, "bottle", (6, 28), [("L", (14, 12)), ("L", (22, 16)), ("L", (30, 20)), ("L", (34, 28))])
        join(self, "bucket", "bottle")
        path(self, "neck", (22, 16), [("L", (26, 8)), ("L", (27, 6))]); join(self, "neck", "bottle")
        path(self, "cap", (24, 7), [("L", (26, 8)), ("L", (28, 9))]); join(self, "cap", "neck")
