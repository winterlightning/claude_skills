from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "56f53c2f-3889-5760-878c-9f76de3d1136"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__towel-on-clothes-hanger/20260927T155443Z-thuan-mac-1/reference/bathroom hanger_56f53c2f-3889-5760-878c-9f76de3d1136.svg"
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
PLAN = "Open r6 hook arc over a tall triangular hanger; a towel rectangle hangs over the bar, split by a fold line, with the bar visible only outside it."
CONSTRUCTION_REFERENCES = "Lucide shirt/hanger conventions: open hook to the left (deliberately asymmetric, as the reference), mirrored arms on an (8,9) slope so the towel clears them by 8.2."
OMISSIONS = "Towel narrowed to 10 units so its corners keep clearance from the hanger arms."


class Drawing(Solo48):
    icon_id = "towel-on-clothes-hanger"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hotels"
    aliases = ("bathroom-hanger", "towel-hanger")
    keywords = ("towel", "clothes", "hanger", "bathroom", "hotel", "hook")

    def build(self):
        self.add_arc("hook", (24, 10), (12, 10), radius_x=6, sweep=False)
        path(self, "hanger", (8, 28), [("L", (24, 10)), ("L", (40, 28)), ("L", (29, 28))])
        self.add_line("bar-left", (8, 28), (19, 28)); join(self, "bar-left", "hanger")
        join(self, "hook", "hanger")
        path(self, "towel", (19, 28), [("L", (29, 28)), ("L", (29, 36)), ("L", (29, 44)), ("L", (19, 44)), ("L", (19, 36)), ("L", (19, 28))], closed=True)
        join(self, "towel", "hanger"); join(self, "towel", "bar-left")
        self.add_line("fold", (19, 36), (29, 36)); join(self, "fold", "towel")
