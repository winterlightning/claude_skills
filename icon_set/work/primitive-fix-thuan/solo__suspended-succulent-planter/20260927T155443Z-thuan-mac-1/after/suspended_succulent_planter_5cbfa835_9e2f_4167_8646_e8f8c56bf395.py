from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5cbfa835-9e2f-4167-8646-e8f8c56bf395"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__suspended-succulent-planter/20260927T155443Z-thuan-mac-1/reference/hanging plant 2_5cbfa835-9e2f-4167-8646-e8f8c56bf395.svg"
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
PLAN = "Cord from the top into a pointed glass planter (pentagon top, tapered base) with a rim line; a three-stroke sprout rises from the rim."
CONSTRUCTION_REFERENCES = "No Lucide match; planter is a mirrored polygon about x=24, leaves are r8 arcs from a shared base node."
OMISSIONS = "Lotus leaf outlines reduced to three strokes: outlined leaves cannot keep 8-unit clearance from the converging glass walls."


class Drawing(Solo48):
    icon_id = "suspended-succulent-planter"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "decoration"
    aliases = ("hanging-plant", "hanging-terrarium")
    keywords = ("planter", "hanging", "succulent", "leaves", "cord", "terrarium", "plant")

    def build(self):
        self.add_line("cord", (24, 6), (24, 12))
        path(self, "glass", (24, 12), [("L", (42, 24)), ("L", (42, 32)), ("L", (36, 42)), ("L", (12, 42)), ("L", (6, 32)), ("L", (6, 24)), ("L", (24, 12))], closed=True)
        join(self, "cord", "glass")
        path(self, "rim", (6, 32), [("L", (24, 32)), ("L", (42, 32))]); join(self, "rim", "glass")
        self.add_line("leaf-mid", (24, 32), (24, 22)); join(self, "leaf-mid", "rim")
        self.add_arc("leaf-left", (24, 32), (17, 27), radius_x=8, sweep=True); join(self, "leaf-left", "rim")
        self.add_arc("leaf-right", (24, 32), (31, 27), radius_x=8, sweep=False); join(self, "leaf-right", "rim")
