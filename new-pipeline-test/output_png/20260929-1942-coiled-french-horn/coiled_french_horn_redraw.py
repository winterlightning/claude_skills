"""coiled-french-horn (redraw of the new-pipeline traced SVG).

Subject: a french horn seen side-on -- a round coil of tubing with an open
centre, a flared bell rising to the upper right and a short mouthpiece pipe
off the upper left.

Plan (HRECT_L, centerline box (4,8)-(44,40)):
- Coil: one axis C=(19,25). Outer tube wall R=15 (integer split points
  C+(-9,-12) and C+(12,-9)), inner closed circle r=6. The walls sit 9 apart,
  so the open centre stays wide and the pair is not an exact-8 curve pair.
- Outer outline is one closed contour: coil arc from the bell throat J over
  the top, down the left to the bottom, then the bell's outer wall sweeps out
  round the lower right and up to the rim tip (44,8), the flat rim runs left,
  and the bell's inner wall drops back to J.
- Mouthpiece: a radial stub from the coil at C+(-9,-12) along (-3,-4), so it
  leaves the coil at 90 degrees.
- Extremes: left = coil (4,25), bottom = coil (19,40), top = rim y=8,
  right = rim tip (44,8).

Keyshape: the metrics suggested HRECT_M (28 tall). A coil whose two walls are
at least 8 apart plus a rim above needs 32, so HRECT_L (fit score 0.90, fills
x exactly) is used instead.

Metric issues:
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (warn): fixed; all four extremes sit on the HRECT_L box.
- clearance e0/e2, e0/e3, e2/e3 (error): the double-walled mouthpiece is now
  one radial stroke, so its two walls and its crowding of the coil are gone.
- clearance e0/e4 (error): inner circle and outer coil wall are concentric,
  9 apart.
- clearance e1/e4, e2/e4 (error): the mouthpiece cup is dropped and the stub
  leaves the coil radially, well clear of the rest of the outline.
- narrow-join e2/e4 (warn): mouthpiece meets the coil at 90 degrees.
- narrow-join e4/e0 (warn): the inner circle no longer touches the outline;
  the bell's inner wall meets the coil at J at about 60 degrees.
- hole at (34.7,14.1) (error): the tiny pocket at the rim is gone; the bell
  mouth is open into the coil's tube space.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e0e5259b-1f4e-49b1-b4fe-796abc5994f0"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1942-coiled-french-horn/coiled-french-horn_raw.svg"
AUTHOR = "claude-opus-5-5"

CX, CY = 19, 25          # coil axis
R_OUT, R_IN = 15, 6      # outer tube wall, inner loop
THROAT = (CX + 12, CY - 9)       # J: bell inner wall leaves the coil
TOP = (CX, CY - R_OUT)
MOUTH_ROOT = (CX - 9, CY - 12)
LEFT = (CX - R_OUT, CY)
BOTTOM = (CX, CY + R_OUT)
MOUTH_TIP = (MOUTH_ROOT[0] - 3, MOUTH_ROOT[1] - 4)
RIM_Y = 8
RIM_LEFT = (35, RIM_Y)
RIM_RIGHT = (44, RIM_Y)
BELL_MID = (39, 24)


class CoiledFrenchHornRedraw(Solo48):
    icon_id = "coiled-french-horn-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ("french horn", "horn")
    keywords = ("french", "horn", "brass", "instrument", "music", "orchestra", "coil")

    def build(self) -> None:
        arc = dict(radius_x=R_OUT, sweep=False)
        self.add_arc("coil-top-right", THROAT, TOP, **arc)
        self.add_arc("coil-top-left", TOP, MOUTH_ROOT, **arc)
        self.add_arc("coil-left", MOUTH_ROOT, LEFT, **arc)
        self.add_arc("coil-bottom", LEFT, BOTTOM, **arc)
        self.add_bezier("bell-outer", BOTTOM,
                        ((28, 40), (37, 34), BELL_MID),
                        ((40, 20), (42, 12), RIM_RIGHT))
        self.add_line("rim", RIM_RIGHT, RIM_LEFT)
        self.add_line("bell-inner", RIM_LEFT, THROAT)
        self.add_contour("horn", "coil-top-right", "coil-top-left", "coil-left",
                         "coil-bottom", "bell-outer", "rim", "bell-inner", closed=True)

        r = dict(radius_x=R_IN)
        self.add_arc("loop-top", (CX - R_IN, CY), (CX, CY - R_IN), **r)
        self.add_arc("loop-right", (CX, CY - R_IN), (CX + R_IN, CY), **r)
        self.add_arc("loop-bottom", (CX + R_IN, CY), (CX, CY + R_IN), **r)
        self.add_arc("loop-left", (CX, CY + R_IN), (CX - R_IN, CY), **r)
        self.add_contour("loop", "loop-top", "loop-right", "loop-bottom", "loop-left", closed=True)

        self.add_line("mouthpiece", MOUTH_ROOT, MOUTH_TIP)
        self.relate("connect", "mouthpiece", "horn")
