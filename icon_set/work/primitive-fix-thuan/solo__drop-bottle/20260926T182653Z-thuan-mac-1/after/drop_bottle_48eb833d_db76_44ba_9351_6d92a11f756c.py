"""Drop bottle: a feeding / dropper bottle -- a rounded teat on top, flaring
shoulders into a screw collar, and a tall round-cornered body below.

Revision (disapproved, reason not recorded): the rejected drawing was a squat jug
with a narrow square spout, so the rounded teat, the collar ring and the tall
body of the original were lost. The teat, collar and tall body are restored.

Symbol plan: mirror axis x=24. Teat: radius-5 dome about (24,9) (top 4) on a
10-wide neck (x 19/29) down to y=12. Shoulders: cubics flaring from the neck to
the collar (12,18)/(36,18). Collar: straight sides to y=26, closed by the collar
line (12,26)-(36,26), 8 below the shoulders; the body steps out 2 to x=10/38
there and runs
down to radius-4 corners at the base y=44.
Omissions: the teat's hole and the graduation marks (no 8-unit room).
Lucide construction: 'milk' bottle outline; rounded-rectangle corners.
Keyshape VRECT_M: centerline x 10..38 (body), y 4 (teat) .. 44 (base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "48eb833d-db76-44ba-9351-6d92a11f756c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__drop-bottle/20260926T182653Z-thuan-mac-1/reference/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.svg"
AUTHOR = "claude-opus-5-5"


def mirror(p):
    return (48 - p[0], p[1])


class DropBottle(Solo48):
    icon_id = "drop-bottle"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/containers"
    aliases = ("baby-bottle", "dropper-bottle", "feeding-bottle")
    keywords = ("bottle", "drop", "dropper", "baby", "feeding", "teat", "milk")

    def build(self) -> None:
        # Left half, top to bottom; the right half is its mirror, traced back up.
        left = [("line", (19, 9), (19, 12)),
                ("bezier", (19, 12), ((19, 15), (12, 15), (12, 18))),
                ("line", (12, 18), (12, 26)),
                ("line", (12, 26), (10, 26)),
                ("line", (10, 26), (10, 40)),
                ("arc", (10, 40), (14, 44)),
                ("line", (14, 44), (24, 44))]
        names = []
        self.add_arc("teat-left", (24, 4), (19, 9), radius_x=5, sweep=False)
        names.append("teat-left")
        for i, (kind, a, b) in enumerate(left):
            n = f"left-{i}"
            if kind == "line":
                self.add_line(n, a, b)
            elif kind == "arc":
                self.add_arc(n, a, b, radius_x=4, sweep=False)
            else:
                self.add_bezier(n, a, b)
            names.append(n)
        for i, (kind, a, b) in reversed(list(enumerate(left))):
            n = f"right-{i}"
            if kind == "line":
                self.add_line(n, mirror(b), mirror(a))
            elif kind == "arc":
                self.add_arc(n, mirror(b), mirror(a), radius_x=4, sweep=False)
            else:
                c1, c2, end = b
                self.add_bezier(n, mirror(end), (mirror(c2), mirror(c1), mirror(a)))
            names.append(n)
        self.add_arc("teat-right", (29, 9), (24, 4), radius_x=5, sweep=False)
        names.append("teat-right")
        self.add_contour("bottle", *names, closed=True)
        self.add_line("collar-line", (12, 26), (36, 26))
        self.relate("connect", "bottle", "collar-line")
