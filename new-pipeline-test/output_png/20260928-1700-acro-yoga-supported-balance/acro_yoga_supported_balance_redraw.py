"""acro-yoga-supported-balance (redraw of the new-pipeline traced SVG).

Plan (HRECT_M, centerline box (4,10)-(44,38), the suggested keyshape):
- Flyer on top, held level: r4 head at (8,14) beside a horizontal torso run
  (neck at x=20, exact 8 centerline gap), torso to the hip at x=34, legs
  rising to the foot tip (44,10). The head sets the left/top extremes and the
  foot sets the right one.
- Base below, lying on the floor: straight torso from the hip (18,34) to the
  neck (28,34) and an r4 head at (40,34) whose outline sets the bottom extreme.
  One straight raised leg goes to a shared node under the flyer's belly (26,14).
  That is the only real contact, and it is declared with connect.
- Both heads follow the shared human reference: circular outlined heads,
  detached, level beside an axis-aligned torso tangent so the 4u ink gap
  certifies. Both figures are flagged with mark_human_figure.

Metric issues:
- clearance e0/e1 (flyer head on its body, 1.86): fixed. The head is exactly
  8 from the neck on centerlines (4u ink gap).
- clearance e1/e2 (flyer body vs base legs, 1.65): fixed. The base foot now
  really supports the flyer at a shared, connected node.
- clearance e2/e3 (base body vs base head, 4.54): fixed. The base head is
  exactly 8 from its neck, and the trace's head speck (e3) is redrawn as a
  real r4 head.
- hole 0.8 wide at the flyer head: fixed, because the head is a clean r4 ring.
- no-head: fixed. Both heads are circular outlines.
- keyshape-short-axis (x fills 97%): fixed. The extremes are exact:
  x=4 (flyer head), x=44 (flyer foot), y=10 (flyer head top) and y=38
  (base head bottom).
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
Deliberate departures from the trace:
- The base lies head-right, so the heads sit in opposite corners. With both
  heads on the left, the two stacked rings read as a colon at 48 px.
- The flyer's forward arms are dropped. A forward arm either passes within 8
  of the level head or reads as a "pi" sign, and hand-holds closed the
  figures into a pentagon.
- The trace's doubled base legs become a single leg, because two parallel
  legs would sit less than 8 apart. A bent knee was also tried; it read as
  a "2", so the leg stays straight.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5240dbe0-19a2-54d5-b0f7-5cc3089e49e4"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1700-acro-yoga-supported-balance/"
    "acro-yoga-supported-balance_raw.svg"
)
AUTHOR = "claude-opus-5-5"

HEAD_R = 4
GAP = 8

FLYER_Y = 14
FLYER_NECK = (20, FLYER_Y)
FLYER_HIP = (34, FLYER_Y)
FLYER_FOOT = (44, 10)
SUPPORT = (26, FLYER_Y)  # base foot under the flyer's belly

BASE_Y = 34
BASE_NECK = (28, BASE_Y)  # base lies head-right, under the flyer's legs
BASE_HIP = (18, BASE_Y)


def head_beside(neck, side):
    return (neck[0] + side * (GAP + HEAD_R), neck[1])


class AcroYogaSupportedBalanceRedraw(Solo48):
    icon_id = "acro-yoga-supported-balance-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("front bird pose", "acro yoga bird", "partner balance")
    keywords = ("acro yoga", "yoga", "balance", "partner", "flyer", "base", "bird pose")

    def _head(self, name, centre):
        cx, cy = centre
        r = HEAD_R
        self.add_arc(f"{name}-1", (cx, cy - r), (cx + r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-2", (cx + r, cy), (cx, cy + r), radius_x=r, sweep=True)
        self.add_arc(f"{name}-3", (cx, cy + r), (cx - r, cy), radius_x=r, sweep=True)
        self.add_arc(f"{name}-4", (cx - r, cy), (cx, cy - r), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-1", f"{name}-2", f"{name}-3", f"{name}-4", closed=True)

    def build(self) -> None:
        # Flyer, held level on the base's foot
        self.add_line("flyer-chest", FLYER_NECK, SUPPORT)
        self.add_line("flyer-belly", SUPPORT, FLYER_HIP)
        self.add_line("flyer-legs", FLYER_HIP, FLYER_FOOT)
        self._head("flyer-head", head_beside(FLYER_NECK, -1))
        self.mark_human_figure("flyer", head="flyer-head", torso="flyer-chest", torso_junction="start")
        # Base, lying on the floor with the leg raised to the flyer
        self.add_line("base-torso", BASE_NECK, BASE_HIP)
        self.add_line("base-leg", BASE_HIP, SUPPORT)
        self._head("base-head", head_beside(BASE_NECK, 1))
        self.mark_human_figure("base", head="base-head", torso="base-torso", torso_junction="start")

        for a, b in (
            ("flyer-chest", "flyer-belly"), ("flyer-belly", "flyer-legs"),
            ("base-torso", "base-leg"),
            ("base-leg", "flyer-chest"), ("base-leg", "flyer-belly"),
        ):
            self.relate("connect", a, b)
