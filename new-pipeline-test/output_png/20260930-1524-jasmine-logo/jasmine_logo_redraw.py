"""jasmine-logo: a five-petal jasmine flower inside a round logo ring
(redraw of the new-pipeline traced SVG).

Plan: CIRCLE as suggested (centerline radius 20 about (24,24)), mirrored
about x=24.
- ring: two semicircle arcs r=20 closed into one contour; its ink reaches
  radius 22, the CIRCLE extreme.
- blossom: one closed contour of five round petals, one pointing up.
  Five integer valleys (19,18), (29,18), (32,26), (24,32), (16,26) sit about
  8 from the centre (adjacent valleys 8.5..10 apart). Each petal is one
  cubic bump between two valleys whose controls stand off the chord along
  its outward normal, sized so every apex lands PETAL_REACH = 11.5 from
  the centre: 8.5 on centerlines inside the ring (a curved pair exactly on
  8 is not certified).
Traced shape: jasmine-logo_raw.svg, read for the subject only; no trace
coordinates reused.

Metric issues fixed by the rebuild:
- clearance e0/e1, e0/e2, e0/e3 (petal tips 2.9..3.3 from the ring): every
  petal apex is 8.5 inside the ring.
- clearance e1/e2, e1/e3, e2/e3 (3.5..6.2, petals crowding each other) and
  narrow-join e2/e1, e3/e1 (21..32 deg wedges at the centre): the five
  petals are one contour meeting only at valleys, no overlapping loops and
  no wedge joins.
- hole at (23.9,15.1), (14.9,22.0), (33.1,22.0), (18.8,31.6),
  (29.3,31.6) (3.1..3.9 wide, the slivers between overlapping petal
  loops): the blossom interior is one open cell (about 10 across).
- stroke-width (2.67): drawn at the profile stroke 4 and gaps budgeted
  for it.
Not kept, with reason:
- five separate hollow, pointed petals meeting at the centre: inside the
  ring they must stay within radius 12, where five lens loops with a 6-wide
  hole each would need about 50 of circumference at mid-petal and only
  about 35 exists. A pointed-star outline was tried: its valleys are too
  shallow and it read as a lumpy star at 48 px. The round-lobed blossom
  keeps five equal petals, one pointing up, with the clear gap to the
  ring.
Lucide: `flower-2` (a lobed blossom outline built from equal bumps) and
`circle` informed the construction; no Lucide jasmine or flower-in-ring
exists.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "99aca13e-621b-4224-a7d5-50e282c5a5ba"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1524-jasmine-logo/jasmine-logo_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 24
RING_R = 20
PETAL_REACH = 11.5   # petal apex distance from the centre: 8.5 inside the ring
# Petal valleys, clockwise from the top-right one; mirrored about x=24.
V_TOP = (29, 18)
V_SIDE = (32, 26)
V_BOTTOM = (CX, 32)


def mirror(p: tuple[int, int]) -> tuple[int, int]:
    return (2 * CX - p[0], p[1])


VALLEYS = (V_TOP, V_SIDE, V_BOTTOM, mirror(V_SIDE), mirror(V_TOP))


def petal_controls(a, b):
    """Controls of a round petal bump from valley a to valley b.

    Both controls stand off the chord along its outward normal; a cubic
    with equal standoff k peaks at 0.75 k, so k is set for the apex to land
    on PETAL_REACH from the centre.
    """
    mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
    dx, dy = b[0] - a[0], b[1] - a[1]
    n = (dx * dx + dy * dy) ** 0.5
    nx, ny = dy / n, -dx / n                     # outward for a clockwise loop
    mid_r = ((mx - CX) ** 2 + (my - CX) ** 2) ** 0.5
    k = (PETAL_REACH - mid_r) / 0.75
    return (a[0] + k * nx, a[1] + k * ny), (b[0] + k * nx, b[1] + k * ny)


class JasmineLogoRedraw(Solo48):
    icon_id = "jasmine-logo-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ("jasmine-flower-emblem",)
    keywords = ("jasmine", "logo", "flower", "blossom", "petals", "brand", "emblem")

    def build(self) -> None:
        self.add_arc("ring-r", (CX, CX - RING_R), (CX, CX + RING_R), radius_x=RING_R, sweep=True)
        self.add_arc("ring-l", (CX, CX + RING_R), (CX, CX - RING_R), radius_x=RING_R, sweep=True)
        self.add_contour("ring", "ring-r", "ring-l", closed=True)

        # Five petals clockwise from the top one, each a round bump between
        # two valleys.
        names = []
        for i in range(5):
            a, b = VALLEYS[i - 1], VALLEYS[i]
            name = f"petal-{i + 1}"
            self.add_bezier(name, a, (*petal_controls(a, b), b))
            names.append(name)
        self.add_contour("blossom", *names, closed=True)
