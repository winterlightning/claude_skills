from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f0c28f5a-8618-48b9-aa2f-5160d2226c1b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__sliding-door-open-left-solo-b002-05/20260927T155443Z-thuan-mac-1/reference/door sliding left hand open_f0c28f5a-8618-48b9-aa2f-5160d2226c1b.svg"
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

PLAN = "Square frame, sliding panel band with a centred vertical handle, as in the reference."
CONSTRUCTION_REFERENCES = "Lucide door-closed: outer frame with an interior handle mark; square corners so every gap is straight-to-straight."
OMISSIONS = "None."


class Drawing(Solo48):
    icon_id = "sliding-door-open-left-solo-b002-05"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "building"
    aliases = ("sliding-door",)
    keywords = ("sliding", "door", "open", "left", "panel", "handle")

    def build(self):
        path(self, "frame", (6, 6), [("L", (18, 6)), ("L", (34, 6)), ("L", (42, 6)), ("L", (42, 42)),
                                     ("L", (34, 42)), ("L", (18, 42)), ("L", (6, 42)), ("L", (6, 6))], closed=True)
        for x in (18, 34):
            self.add_line(f"panel-{x}", (x, 6), (x, 42)); join(self, "frame", f"panel-{x}")
        self.add_line("handle", (26, 20), (26, 28))
