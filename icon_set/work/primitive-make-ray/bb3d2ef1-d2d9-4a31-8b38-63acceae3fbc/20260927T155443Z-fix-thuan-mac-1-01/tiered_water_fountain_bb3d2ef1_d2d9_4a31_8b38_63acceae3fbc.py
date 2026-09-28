from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bb3d2ef1-d2d9-4a31-8b38-63acceae3fbc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__tiered-water-fountain/20260927T155443Z-thuan-mac-1/reference/park fonutain_bb3d2ef1-d2d9-4a31-8b38-63acceae3fbc.svg"
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
PLAN = "Central jet with two spray drops over a small closed upper bowl, a stem, and a wide flat-bottomed lower basin; mirrored about x=24."
CONSTRUCTION_REFERENCES = "No Lucide fountain; bowls are cardinal half-ellipses closed by their rims so the tiers read as basins, not arcs."
OMISSIONS = "Curling side jets replaced by two drops (curls landing on the rim leave holes too small); pedestal merged into a flat-bottomed basin so the lower tier keeps a valid hole."


class Drawing(Solo48):
    icon_id = "tiered-water-fountain"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ("park-fountain",)
    keywords = ("fountain", "water", "park", "plaza", "jet", "basin", "garden", "landmark")

    def build(self):
        self.add_line("jet", (24, 6), (24, 13))
        self.add_dot("drop-left", (10, 6)); self.add_dot("drop-right", (38, 6))
        path(self, "upper", (14, 13), [("L", (24, 13)), ("L", (34, 13)), ("A", (14, 13), 10, 6, True)], closed=True)
        join(self, "jet", "upper")
        self.add_line("stem", (24, 19), (24, 28)); join(self, "stem", "upper")
        path(self, "basin", (6, 28), [("L", (24, 28)), ("L", (42, 28)), ("L", (36, 42)), ("L", (12, 42)), ("L", (6, 28))], closed=True)
        join(self, "stem", "basin")
