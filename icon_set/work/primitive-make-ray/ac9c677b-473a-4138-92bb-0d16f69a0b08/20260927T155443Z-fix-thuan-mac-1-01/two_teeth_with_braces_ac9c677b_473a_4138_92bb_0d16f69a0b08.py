from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ac9c677b-473a-4138-92bb-0d16f69a0b08"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__two-teeth-with-braces/20260927T155443Z-thuan-mac-1/reference/dental brace_ac9c677b-473a-4138-92bb-0d16f69a0b08.svg"
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
PLAN = "Two identical teeth (two cusps, straight walls, one tapered rounded root) joined by an archwire, each with a bracket bar crossing the wire."
CONSTRUCTION_REFERENCES = "No Lucide tooth; each tooth mirrored about its own axis, repeated with a 24-unit step; brackets as vertical bars centred on the wire."
OMISSIONS = "Square bracket outlines reduced to bars and two roots to one: a 16-wide tooth cannot hold a 10-wide hollow bracket or an r5 cleft."


class Drawing(Solo48):
    icon_id = "two-teeth-with-braces"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("dental-braces", "orthodontics")
    keywords = ("teeth", "braces", "dental", "orthodontic", "wire", "bracket")

    def build(self):
        for i in range(2):
            x = 4 + 24 * i
            path(self, f"tooth-{i}", (x, 12), [
                ("A", (x + 4, 8), 4, 4, True), ("A", (x + 12, 8), 4, 2, False), ("A", (x + 16, 12), 4, 4, True),
                ("L", (x + 16, 22)), ("L", (x + 16, 28)), ("L", (x + 12, 36)), ("A", (x + 4, 36), 4, 4, True),
                ("L", (x, 28)), ("L", (x, 22)), ("L", (x, 12))], closed=True)
            self.add_line(f"bracket-{i}", (x + 8, 19), (x + 8, 25))
        path(self, "wire", (4, 22), [("L", (12, 22)), ("L", (20, 22)), ("L", (28, 22)), ("L", (36, 22)), ("L", (44, 22))])
        for i in range(2):
            join(self, "wire", f"tooth-{i}"); join(self, "wire", f"bracket-{i}")
