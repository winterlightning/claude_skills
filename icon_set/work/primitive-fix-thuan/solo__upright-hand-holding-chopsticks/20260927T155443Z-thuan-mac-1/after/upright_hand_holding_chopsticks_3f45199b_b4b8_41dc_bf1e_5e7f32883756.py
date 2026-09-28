from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3f45199b-b4b8-41dc-bf1e-5e7f32883756"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__upright-hand-holding-chopsticks/20260927T155443Z-thuan-mac-1/reference/chopstick_3f45199b-b4b8-41dc-bf1e-5e7f32883756.svg"
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
PLAN = "Side-view fist: top edge, left wall and rounded heel as an open C, with four finger strokes (top edge, two inner strokes, bottom edge) ending in round tips on the right; two parallel chopsticks on the 45-degree diagonal pass behind it, entering at the top-left corner and left wall and leaving from the bottom edge and bottom-right corner."
CONSTRUCTION_REFERENCES = "Lucide hand-grab principle (compact fist, finger creases); sticks on x-y=0 and x-y=-12 so they sit 8.5 apart and end on box nodes."
OMISSIONS = "Thumb bump and wrist dropped: no 8-unit room on the 24-unit fist edge; right wall left open so the finger tips read."


class Drawing(Solo48):
    icon_id = "upright-hand-holding-chopsticks"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("hand-with-chopsticks", "chopstick-grip")
    keywords = ("hand", "holding", "chopsticks", "grip", "fist", "asian food", "eating")

    def build(self):
        # fist: top edge, left wall, rounded heel, bottom edge; open on the right where the finger strokes end
        self.add_line("fist-top", (38, 14), (14, 14))
        self.add_line("fist-left-a", (14, 14), (14, 26))
        self.add_line("fist-left-b", (14, 26), (14, 32))
        self.add_arc("fist-heel", (14, 32), (20, 38), radius_x=6, sweep=False)
        self.add_line("fist-bottom-a", (20, 38), (26, 38))
        self.add_line("fist-bottom-b", (26, 38), (38, 38))
        chain = ["fist-top", "fist-left-a", "fist-left-b", "fist-heel", "fist-bottom-a", "fist-bottom-b"]
        for a, b in zip(chain, chain[1:]):
            join(self, a, b)
        for y in (22, 30):
            self.add_line(f"finger-{y}", (22, y), (38, y))
        self.add_line("stick-a-top", (6, 6), (14, 14)); join(self, "stick-a-top", "fist-top"); join(self, "stick-a-top", "fist-left-a")
        self.add_line("stick-a-bottom", (38, 38), (42, 42)); join(self, "stick-a-bottom", "fist-bottom-b")
        self.add_line("stick-b-top", (6, 18), (14, 26)); join(self, "stick-b-top", "fist-left-a"); join(self, "stick-b-top", "fist-left-b")
        self.add_line("stick-b-bottom", (26, 38), (30, 42)); join(self, "stick-b-bottom", "fist-bottom-a"); join(self, "stick-b-bottom", "fist-bottom-b")
