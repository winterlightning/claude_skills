from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b1a71762-cfed-4c31-8dc5-4cfaea8d5909"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__six-dot-drag-handle/20260927T155443Z-thuan-mac-1/reference/mark circle_b1a71762-cfed-4c31-8dc5-4cfaea8d5909.svg"
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

PLAN = "Six short horizontal dashes in a 3x2 grid, as in the reference (dashes, not dots)."
CONSTRUCTION_REFERENCES = "Lucide grip-horizontal: even 3x2 grid; marks redrawn as the reference's dashes."
OMISSIONS = "None."


class Drawing(Solo48):
    icon_id = "six-dot-drag-handle"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "other"
    aliases = ("mark-circle", "grip-dashes")
    keywords = ("drag", "handle", "grip", "dashes", "marks")

    def build(self):
        for r, y in enumerate((10, 38)):
            for c, x in enumerate((4, 21, 38)):
                self.add_line(f"dash-{r}-{c}", (x, y), (x + 6, y))
