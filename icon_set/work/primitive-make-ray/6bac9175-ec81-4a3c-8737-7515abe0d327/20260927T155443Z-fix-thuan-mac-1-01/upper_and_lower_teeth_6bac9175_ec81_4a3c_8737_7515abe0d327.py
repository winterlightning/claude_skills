from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6bac9175-ec81-4a3c-8737-7515abe0d327"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__upper-and-lower-teeth/20260927T155443Z-thuan-mac-1/reference/dentistry tooth jaws_6bac9175-ec81-4a3c-8737-7515abe0d327.svg"
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
PLAN = "Upper and lower rows of four teeth: each row a gum band with a scalloped edge (r6 arcs on 10-unit chords) and seams between teeth, mirrored top to bottom about y=24."
CONSTRUCTION_REFERENCES = "No Lucide match; scallops as r6 arcs on 10-unit chords so adjacent teeth meet at a 68-degree notch instead of a cusp."
OMISSIONS = "Outer lip outline dropped; scallops made shallow so every tooth keeps a valid hole."


class Drawing(Solo48):
    icon_id = "upper-and-lower-teeth"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("jaws", "dentition", "teeth-rows")
    keywords = ("upper", "lower", "teeth", "jaw", "dentistry", "mouth", "bite")

    def build(self):
        xs = (4, 14, 24, 34, 44)
        # upper row: gum line y=8, scallops from y=16 bulging down
        cmds = [("L", (44, 8)), ("L", (44, 16))]
        for a, b in zip(reversed(xs[:-1]), reversed(xs[1:])):
            cmds.append(("A", (a, 16), 6, 6, True))
        cmds.append(("L", (4, 8)))
        path(self, "upper", (4, 8), cmds, closed=True)
        for x in xs[1:-1]:
            self.add_line(f"upper-seam-{x}", (x, 8), (x, 16)); join(self, "upper", f"upper-seam-{x}")
        # lower row: gum line y=40, scallops from y=32 bulging up
        cmds = [("L", (4, 40)), ("L", (4, 32))]
        for a, b in zip(xs[:-1], xs[1:]):
            cmds.append(("A", (b, 32), 6, 6, True))
        cmds.append(("L", (44, 40)))
        path(self, "lower", (44, 40), cmds, closed=True)
        for x in xs[1:-1]:
            self.add_line(f"lower-seam-{x}", (x, 32), (x, 40)); join(self, "lower", f"lower-seam-{x}")
