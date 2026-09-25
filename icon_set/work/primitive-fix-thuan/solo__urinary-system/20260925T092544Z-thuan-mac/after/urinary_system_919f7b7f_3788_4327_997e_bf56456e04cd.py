"""Urinary system: two bean-shaped kidneys, ureters descending to a rounded
bladder, and a short urethra.

Symbol plan: one kidney contour and one ureter authored on the left and
mirrored about x=24; the ureters end on the bladder's two top corners (shared
endpoints, declared connections); the urethra leaves the bladder's lowest point.
Keyshape SQUARE: kidney outer bulges x=6/42, kidney tops y=6, urethra end y=42.
Lucide construction: bean / kidney-like smooth closed cubics with a concave
hilum notch; no direct anatomical match.
Revision of the rejected drawing ("Bad stroke drawn"): the old drawing merged
the kidneys into the ureters as lumpy loops; here each organ is a smooth
separate shape.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "919f7b7f-3788-4327-997e-bf56456e04cd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__urinary-system/20260925T092544Z-thuan-mac/reference/urinary system_919f7b7f-3788-4327-997e-bf56456e04cd.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
BLADDER_TOP = 28


def m(point):
    """Mirror a point about the vertical axis."""
    return (2 * AXIS - point[0], point[1])


class UrinarySystem(Solo48):
    icon_id = "urinary-system"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("kidneys-and-bladder",)
    keywords = ("urinary", "system", "kidney", "bladder", "ureter", "urology", "anatomy")

    def path(self, name, start, steps, closed=False, mirror=False):
        f = m if mirror else (lambda p: p)
        members = []
        start = f(start)
        for index, (kind, *args) in enumerate(steps):
            tag = f"{name}-{index + 1}"
            if kind == "L":
                end = f(args[0])
                self.add_line(tag, start, end)
            else:
                c1, c2, end = (f(p) for p in args)
                self.add_bezier(tag, start, (c1, c2, end))
            start = end
            members.append(tag)
        self.add_contour(name, *members, closed=closed)

    def build(self) -> None:
        kidney = [
            ("C", (16, 6), (18, 8), (18, 11)),          # upper pole to inner upper lobe
            ("C", (18, 12.5), (16, 12.5), (16, 14)),    # shallow hilum notch
            ("C", (16, 15.5), (18, 15.5), (18, 17)),    # inner lower lobe
            ("C", (18, 18.5), (17.2, 19.4), (16, 20)),  # to the ureter exit
            ("C", (15, 20.8), (13.6, 22), (12, 22)),    # lower pole
            ("C", (8, 22), (6, 18), (6, 14)),           # outer bulge
            ("C", (6, 9), (8, 6), (12, 6)),             # back to the top
        ]
        ureter = [("C", (18, 21.5), (20, 23), (20, 25)), ("L", (20, BLADDER_TOP))]
        for side, mirror in (("left", False), ("right", True)):
            self.path(f"kidney-{side}", (12, 6), kidney, closed=True, mirror=mirror)
            self.path(f"ureter-{side}", (16, 20), ureter, mirror=mirror)
            self.relate("connect", f"kidney-{side}", f"ureter-{side}")
            self.relate("connect", f"ureter-{side}", "bladder")
        self.path("bladder", (20, BLADDER_TOP), [
            ("L", m((20, BLADDER_TOP))),
            ("C", (31, 28), (33, 30), (33, 33)),
            ("C", (33, 36.5), (27, 38), (24, 40)),      # taper into the neck
            ("C", (21, 38), (15, 36.5), (15, 33)),
            ("C", (15, 30), (17, 28), (20, BLADDER_TOP)),
        ], closed=True)
        self.add_line("urethra", (AXIS, 40), (AXIS, 42))
        self.relate("connect", "bladder", "urethra")
