from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "69d37e4e-d972-4edd-9487-a2d5344250c0"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__treehouse-with-ladder-batch-018-01/20260927T155443Z-thuan-mac-1/reference/family outdoors tree house_69d37e4e-d972-4edd-9487-a2d5344250c0.svg"
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
PLAN = "Round r7-crowned tree with trunk and side branch on the left; a pentagon treehouse on the right whose walls continue down as a two-rung ladder."
CONSTRUCTION_REFERENCES = "Lucide tree-deciduous principle (one crown mass on a trunk, here a circle since a lobed crown reads as a keyhole at this size) and home (pentagon); ladder rungs share nodes with the rails."
OMISSIONS = "Arched door dropped: a 10-wide arch cannot keep 8 from the 12-wide house walls."


class Drawing(Solo48):
    icon_id = "treehouse-with-ladder-batch-018-01"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    aliases = ("treehouse", "tree-house")
    keywords = ("treehouse", "tree", "ladder", "house", "play", "outdoors", "childhood", "shelter")

    def build(self):
        path(self, "crown", (13, 6), [("A", (20, 13), 7, 7, True), ("A", (13, 20), 7, 7, True), ("A", (6, 13), 7, 7, True), ("A", (13, 6), 7, 7, True)], closed=True)
        path(self, "trunk", (13, 20), [("L", (13, 34)), ("L", (13, 42))]); join(self, "trunk", "crown")
        self.add_line("branch", (13, 34), (6, 30)); join(self, "branch", "trunk")
        path(self, "house", (30, 14), [("L", (36, 8)), ("L", (42, 14)), ("L", (42, 26)), ("L", (30, 26)), ("L", (30, 14))], closed=True)
        for x in (30, 42):
            path(self, f"rail-{x}", (x, 26), [("L", (x, 34)), ("L", (x, 42))]); join(self, f"rail-{x}", "house")
        for y in (34, 42):
            self.add_line(f"rung-{y}", (30, y), (42, y)); join(self, f"rung-{y}", "rail-30"); join(self, f"rung-{y}", "rail-42")
