from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "daebb644-0ba7-42d0-83a7-0593009cd417"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__smart-toothbrush-and-phone/20260927T155443Z-thuan-mac-1/reference/smart ultra sonic tooth brush_daebb644-0ba7-42d0-83a7-0593009cd417.svg"
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

PLAN = "Electric toothbrush (small head, neck, tall handle) on the left, phone with a bottom bar on the right, one signal arc above the phone."
CONSTRUCTION_REFERENCES = "Lucide smartphone: rounded rectangle with a bottom mark; brush built as two rounded boxes joined by a neck."
OMISSIONS = "Second concentric signal arc dropped: no room above the phone within the envelope."


def box(s, n, l, t, r, b, k):
    path(s, n, (l + k, t), [("L", (r - k, t)), ("A", (r, t + k), k, k, True), ("L", (r, b - k)),
                            ("A", (r - k, b), k, k, True), ("L", (l + k, b)), ("A", (l, b - k), k, k, True),
                            ("L", (l, t + k)), ("A", (l + k, t), k, k, True)], closed=True)


class Drawing(Solo48):
    icon_id = "smart-toothbrush-and-phone"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    aliases = ("electric-toothbrush-app",)
    keywords = ("toothbrush", "electric", "ultrasonic", "phone", "smart", "wireless", "dental")

    def build(self):
        # brush head, bottom edge split at the neck
        path(self, "head", (13, 6), [("L", (17, 6)), ("A", (20, 9), 3, 3, True), ("L", (20, 13)), ("A", (17, 16), 3, 3, True), ("L", (12, 16)), ("A", (10, 14), 2, 2, True), ("L", (10, 9)), ("A", (13, 6), 3, 3, True)], closed=True)
        self.add_line("neck", (12, 16), (12, 24)); join(self, "head", "neck")
        path(self, "handle", (9, 24), [("L", (12, 24)), ("L", (13, 24)), ("A", (16, 27), 3, 3, True), ("L", (16, 39)), ("A", (13, 42), 3, 3, True),
                                      ("L", (9, 42)), ("A", (6, 39), 3, 3, True), ("L", (6, 27)), ("A", (9, 24), 3, 3, True)], closed=True)
        join(self, "neck", "handle")
        path(self, "phone", (28, 19), [("L", (40, 19)), ("A", (42, 21), 2, 2, True), ("L", (42, 30)), ("L", (42, 40)), ("A", (40, 42), 2, 2, True),
                                      ("L", (28, 42)), ("A", (26, 40), 2, 2, True), ("L", (26, 30)), ("L", (26, 21)), ("A", (28, 19), 2, 2, True)], closed=True)
        self.add_line("bar", (26, 30), (42, 30)); join(self, "phone", "bar")
        self.add_arc("signal", (30, 10), (38, 10), radius_x=4)
