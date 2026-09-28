from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b1ca9299-f064-4596-bd7a-279b553da82b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__spiral-protein-ribbon/20260927T155443Z-thuan-mac-1/reference/protein strand_b1ca9299-f064-4596-bd7a-279b553da82b.svg"
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

PLAN = "Zigzag ribbon band: two parallel W polylines 21 apart joined by vertical ends, so the strand has visible width like the folded reference ribbon."
CONSTRUCTION_REFERENCES = "No Lucide match; band offset chosen so the 9:15 diagonals sit 10.8 apart on centerlines (hole 6.8 ink)."
OMISSIONS = "Perspective shading edges of the folds dropped."


class Drawing(Solo48):
    icon_id = "spiral-protein-ribbon"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("protein-strand", "helix-ribbon")
    keywords = ("spiral", "protein", "ribbon", "strand", "helix", "zigzag")

    def build(self):
        top = [(6, 6), (15, 21), (24, 6), (33, 21), (42, 6)]
        bot = [(x, y + 21) for x, y in top]
        cmds = [("L", p) for p in top[1:]] + [("L", bot[-1])] + [("L", p) for p in reversed(bot[:-1])] + [("L", top[0])]
        path(self, "ribbon", top[0], cmds, closed=True)
