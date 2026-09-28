"""A bench press station seen end-on: a loaded barbell on two uprights over a bench.

Symbol plan: mirrored about x=24. Each weight plate is a rounded rectangle 8 wide and
14 tall (r3 corners) at the top corners; the bar joins the plates' inner sides. An upright
post drops from the bottom centre of each plate to the floor line. The bench between them
is a trapezoid seat (narrow rounded top, wide base) on two straight legs, 9 from each post.
Lucide construction: 'dumbbell' - rounded-rectangle plates joined by a straight bar.
Keyshape SQUARE: centerline x 6..42 (outer plate sides), y 6..42 (plate tops, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d455951e-056e-4788-9743-6d682c228f64"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bench-press-station/20260926T030905Z-thuan-mac/reference/sport bench press_d455951e-056e-4788-9743-6d682c228f64.svg"
AUTHOR = "claude-opus-5-5"


class BenchPressStation(Solo48):
    icon_id = "bench-press-station"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/fitness"
    aliases = ("sport-bench-press", "bench-press", "weight-bench")
    keywords = ("bench", "press", "barbell", "weights", "gym", "fitness", "workout", "strength", "lifting")

    def build(self) -> None:
        m = lambda p: (48 - p[0], p[1])
        x0, x1, y0, y1, bar = 6, 14, 6, 20, 13
        for side, f in (("left", lambda p: p), ("right", m)):
            pts = [(x0, y0 + 3), (x0 + 3, y0), (x1 - 3, y0), (x1, y0 + 3), (x1, bar), (x1, y1 - 3),
                   (x1 - 3, y1), (10, y1), (x0 + 3, y1), (x0, y1 - 3)]
            P = [f(p) for p in pts]
            sw = side == "left"
            self.add_arc(f"plate-{side}-1", P[0], P[1], radius_x=3, sweep=sw)
            self.add_line(f"plate-{side}-2", P[1], P[2])
            self.add_arc(f"plate-{side}-3", P[2], P[3], radius_x=3, sweep=sw)
            self.add_line(f"plate-{side}-4", P[3], P[4])
            self.add_line(f"plate-{side}-5", P[4], P[5])
            self.add_arc(f"plate-{side}-6", P[5], P[6], radius_x=3, sweep=sw)
            self.add_line(f"plate-{side}-7", P[6], P[7])
            self.add_line(f"plate-{side}-8", P[7], P[8])
            self.add_arc(f"plate-{side}-9", P[8], P[9], radius_x=3, sweep=sw)
            self.add_line(f"plate-{side}-10", P[9], P[0])
            self.add_contour(f"plate-{side}", *[f"plate-{side}-{i}" for i in range(1, 11)], closed=True)
            self.add_line(f"post-{side}", P[7], (P[7][0], 42))
            self.relate("connect", f"plate-{side}", f"post-{side}")
            self.relate("connect", f"plate-{side}", "bar")
        self.add_line("bar", (x1, bar), m((x1, bar)))
        # bench seat, end-on: slanted sides, cubic top corners, legs from the base corners
        self.add_line("seat-side-left", (19, 35), (20, 27))
        self.add_bezier("seat-corner-left", (20, 27), ((20.3, 25.2), (21.3, 24), (23, 24)))
        self.add_line("seat-top", (23, 24), (25, 24))
        self.add_bezier("seat-corner-right", (25, 24), ((26.7, 24), (27.7, 25.2), (28, 27)))
        self.add_line("seat-side-right", (28, 27), (29, 35))
        self.add_line("seat-base", (29, 35), (19, 35))
        self.add_contour("seat", "seat-side-left", "seat-corner-left", "seat-top", "seat-corner-right",
                         "seat-side-right", "seat-base", closed=True)
        self.add_line("leg-left", (19, 35), (19, 42))
        self.add_line("leg-right", (29, 35), (29, 42))
        self.relate("connect", "seat", "leg-left")
        self.relate("connect", "seat", "leg-right")
