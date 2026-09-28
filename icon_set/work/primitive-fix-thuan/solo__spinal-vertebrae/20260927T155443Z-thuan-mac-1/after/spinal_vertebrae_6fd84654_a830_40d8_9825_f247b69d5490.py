from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6fd84654-a830-40d8-9825-f247b69d5490"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__spinal-vertebrae/20260927T155443Z-thuan-mac-1/reference/specialty vertebra_6fd84654-a830-40d8-9825-f247b69d5490.svg"
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

PLAN = "Two stacked vertebrae: each a wide winged body with a small process on top and a broad lower bulge, mirrored about x=24; identical 25-unit repeat."
CONSTRUCTION_REFERENCES = "No useful Lucide anatomy match; stadium body with a tangent r5 bump, mirrored about x=24."
OMISSIONS = "Third vertebra and lower processes dropped: three open bodies cannot stack in 40 units with 8-unit gaps."


class Drawing(Solo48):
    icon_id = "spinal-vertebrae"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("vertebra", "spine-segment")
    keywords = ("spinal", "vertebrae", "spine", "bone", "back")

    def build(self):
        for i, t in enumerate((4, 29)):
            path(self, f"vertebra-{i}", (12, t + 5), [
                ("L", (19, t + 5)), ("A", (29, t + 5), 5, 5, True), ("L", (36, t + 5)),
                ("A", (40, t + 9), 4, 4, True), ("A", (36, t + 13), 4, 4, True), ("L", (31, t + 13)),
                ("A", (17, t + 13), 7, 2, True), ("L", (12, t + 13)),
                ("A", (8, t + 9), 4, 4, True), ("A", (12, t + 5), 4, 4, True)], closed=True)
