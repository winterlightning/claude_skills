"""birdwatching-telescope-beneath-three-birds-solo (redraw of the new-pipeline traced SVG).

Plan: a tapered telescope aimed up to the right on a three-leg tripod, with
three gull-shaped birds above it, on SQUARE (centerline box (6,6)-(42,42)).
- birds: one repeated gull definition, 8 wide, drawn as one smooth bezier
  run: tip (cx-4, a+1) -> wing peak (cx-2, a) -> V (cx, a+3), mirrored. The
  wing handles are level at the integer peaks, so each peak is an exact
  extreme and the wing runs on smoothly; the V stays a sharp cusp. Middle
  bird cx=24 at a=6 (the top edge); side birds cx=10 / 38 at a=12, tips at
  x=6 and x=42 (the side edges). With 6-unit horizontal gaps and a 6-unit
  drop, the tips are 8.5 apart.
- tube: one closed contour. Top edge (10,27)->(34,23) on a 1:6 line; bottom
  edge (12,35)->(36,33) on a 1:12 line with an integer node (24,34) at the
  centre for the tripod. The tube tapers from 8 at the eyepiece end to 10 at
  the objective end, so the tube opening is wider than 6. The objective end is an
  outward arc (r8), which stands in for the round lens.
- eyepiece: a short stub on the tube axis leaving the middle of the narrow
  end, (11,31)->(7,32).
- tripod: apex (24,34) on the tube's bottom edge, feet at (17,42), (24,42) and
  (31,42). The outer feet sit 17/31 so the left leg clears the tube's lower
  corner (12,35) by 8.4.
Lucide `telescope`: only the tapered tube, the tripod and the eyepiece stub.
Its lens band and knob are dropped because they need more than 36 units at
stroke 4.

Metric issues (birdwatching-telescope-beneath-three-birds-solo_metrics.json):
- clearance e0/e1, e0/e2 (birds 6.3 apart): fixed. Birds are 8 wide with
  6-unit gaps, and the side birds sit 6 lower, so tips are 8.5 apart.
- clearance e2/e8, e2/e9 (right bird on the objective rim): fixed. The
  objective top (34,23) is 9 below the right bird's tip (34,13). At 8, a
  curve pair comes back `review`.
- clearance e3/e7, e4/e7 and the other tripod/eyepiece clashes: fixed. The
  eyepiece is a single stub on the axis, and the left leg clears the tube
  corner by 8.4.
- hole 2.34 inscribed (the lens ellipse inside the objective): fixed. The
  ellipse is replaced by the arc cap, and the only opening is the tube
  interior, which is more than 6 across.
- keyshape-short-axis (y 99%): fixed. The middle bird's peak is at y=6, the
  feet at y=42 and the bird tips at x=6/42.
- stroke-count 10 vs 6: reduced to 7, not 6. The strokes are 3 birds, the
  tube, the eyepiece, the outer-leg V and the centre leg. Merging the
  eyepiece into the tube outline would put a spur on the closed contour.
- stroke-width (trace 2.75): redrawn at stroke 4.
Not kept: the birds' larger size and small vertical stagger from the PNG. At
stroke 4, three 10-wide birds need a drop of 8, and that pushes the telescope
off the bottom of the box. The birds are now 8 wide with a drop of 6.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "16ec9c7e-624d-4955-83bd-4f0d8fbcba1f"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1843-birdwatching-telescope-beneath-three-birds-solo/birdwatching-telescope-beneath-three-birds-solo_raw.svg"
AUTHOR = "claude-opus-5-5"

BIRDS = (("bird-left", 10, 12), ("bird-middle", 24, 6), ("bird-right", 38, 12))
TIP_DROP, V_DROP = 1, 3                     # tip and V below the wing peaks
TIP_H, PEAK_H, V_H = (0.8, 0.6), 1.2, (0.9, 0.6)   # bezier handles

TUBE_TOP_N, TUBE_TOP_W = (10, 27), (34, 23)
TUBE_BOT_N, TUBE_BOT_W = (12, 35), (36, 33)
APEX = (24, 34)                             # on the 1:12 bottom edge
EYE_BASE, EYE_END = (11, 31), (7, 32)       # middle of the narrow end, on axis
LENS_R = 8
FEET = ((17, 42), (24, 42), (31, 42))


class BirdwatchingTelescopeBeneathThreeBirdsSoloRedraw(Solo48):
    icon_id = "birdwatching-telescope-beneath-three-birds-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/optics"
    aliases = ("birdwatching", "bird watching", "spotting scope")
    keywords = ("telescope", "tripod", "birds", "birdwatching", "birding", "nature", "observe", "sky")

    def _bird(self, name: str, cx: int, a: int) -> None:
        tip, v = TIP_DROP, V_DROP
        self.add_bezier(
            name, (cx - 4, a + tip),
            ((cx - 4 + TIP_H[0], a + tip - TIP_H[1]), (cx - 2 - PEAK_H, a), (cx - 2, a)),
            ((cx - 2 + PEAK_H, a), (cx - V_H[0], a + v - V_H[1]), (cx, a + v)),
            ((cx + V_H[0], a + v - V_H[1]), (cx + 2 - PEAK_H, a), (cx + 2, a)),
            ((cx + 2 + PEAK_H, a), (cx + 4 - TIP_H[0], a + tip - TIP_H[1]), (cx + 4, a + tip)),
        )

    def build(self) -> None:
        for name, cx, a in BIRDS:
            self._bird(name, cx, a)

        # Tapered tube, clockwise from the eyepiece end; the objective end is a lens arc.
        self.add_line("tube-top", TUBE_TOP_N, TUBE_TOP_W)
        self.add_arc("tube-lens", TUBE_TOP_W, TUBE_BOT_W, radius_x=LENS_R, sweep=True)
        self.add_line("tube-bottom-right", TUBE_BOT_W, APEX)
        self.add_line("tube-bottom-left", APEX, TUBE_BOT_N)
        self.add_line("tube-end-low", TUBE_BOT_N, EYE_BASE)
        self.add_line("tube-end-high", EYE_BASE, TUBE_TOP_N)
        self.add_contour("tube", "tube-top", "tube-lens", "tube-bottom-right",
                         "tube-bottom-left", "tube-end-low", "tube-end-high", closed=True)

        self.add_line("eyepiece", EYE_BASE, EYE_END)
        self.relate("connect", "eyepiece", "tube")

        # Tripod: outer legs as one inverted V, centre leg straight down.
        self.add_polyline("tripod", FEET[0], APEX, FEET[2])
        self.add_line("tripod-centre", APEX, FEET[1])
        self.relate("connect", "tripod", "tube")
        self.relate("connect", "tripod-centre", "tube")
        self.relate("connect", "tripod-centre", "tripod")
