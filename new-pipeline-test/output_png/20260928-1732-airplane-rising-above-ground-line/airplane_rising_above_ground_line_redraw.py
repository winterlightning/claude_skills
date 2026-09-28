"""airplane rising above ground line (redraw of the new-pipeline traced SVG).

Plan: side view of a jet climbing to the right over a runway line, on HRECT_L
(centerline box (4,8)-(44,40)).
- ground: one straight line (4,40)-(44,40) - the x=4 / x=44 and y=40 extremes.
- plane: one closed outline. The fuselage top runs on a single 1:2 climb line
  y = 10 + (34 - x) / 2 from the tail fin base (12,21) to the nose (34,10); the
  swept wing and the fin are spikes cut into that line. The nose is a smooth
  three-cubic cap whose apex knot (40,8) has a horizontal tangent (the y=8
  extreme) and whose last control lies on the belly direction, so the belly
  (38,20)-(8,31) joins it tangent-continuously and tapers toward the tail.
- wing: trailing edge at 45 deg from (20,17), leading edge from (28,13), short
  tip edge (12,9)-(16,8); fin: 45 deg front edge from (12,21), tip (4,18)-(8,17),
  rear edge down to the tail (8,31).
Clearances: wing trailing edge to fin tip 8.5, wing tip to fin tip 8.9, plane
bottom (8,31) to ground 9.
Keyshape: HRECT_L instead of the suggested HRECT_M. At stroke 4 the fuselage
needs about 10 units of centerline thickness to keep its 6-wide hole, and the
wing and fin rise above it; with the 8 gap to the ground the HRECT_M box leaves
only 20 units for the plane, so the climb would have to flatten to a near-level
plane with no wing. HRECT_L gives 24 units (Lucide plane-takeoff proportions).
Metric issues fixed:
- hole at (23.8,20) 1.9 wide, (19.4,22.9) 0.45 wide, (11.3,24.2) 0.72 wide:
  the wing's crossing lower edge and the tail's inner corner that cut those
  slivers are gone; the wing and fin are open to the fuselage, so the plane is
  one hole, 10.7 units across on centerlines at the nose.
- keyshape short axis (84% y fill): the nose apex reaches y=8 and the ground
  y=40, so every extreme sits on the box.
- stroke width 2.62: drawn at stroke 4 with every gap sized for it.
Lucide plane-takeoff informed the construction (single outline with the wing as
a spike, runway line below); the fin-up tail and swept wing follow the
generated image. Deliberately asymmetric: a climbing plane is directional.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "28bc625b-2596-540d-91c3-fb5e36336a56"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1732-airplane-rising-above-ground-line/airplane-rising-above-ground-line_raw.svg"
AUTHOR = "claude-opus-5-5"

GROUND_Y = 40
TB = (8, 31)
FT1, FT2 = (4, 18), (8, 17)
TF = (12, 21)
WR, WTR, WTF, WF = (20, 17), (12, 9), (16, 8), (28, 13)
NT = (34, 10)
NB = (38, 20)
NOSE = (((36, 9), (38, 8), (40, 8)),
        ((42, 8), (43, 9), (43, 11)),
        ((43, 15), (41, 18.9), NB))


class AirplaneRisingAboveGroundLineRedraw(Solo48):
    icon_id = "airplane-rising-above-ground-line-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/air"
    aliases = ("plane takeoff", "departure", "airplane taking off")
    keywords = ("airplane", "plane", "takeoff", "departure", "flight", "airport", "travel", "ground")

    def build(self) -> None:
        self.add_line("ground", (4, GROUND_Y), (44, GROUND_Y))
        pts = [TB, FT1, FT2, TF, WR, WTR, WTF, WF, NT]
        ids = []
        for i in range(len(pts) - 1):
            self.add_line(f"body-{i+1}", pts[i], pts[i + 1]); ids.append(f"body-{i+1}")
        self.add_bezier("nose", NT, *NOSE); ids.append("nose")
        self.add_line("belly", NB, TB); ids.append("belly")
        self.add_contour("plane", *ids, closed=True)
