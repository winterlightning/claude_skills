"""anklet (redraw of the new-pipeline traced SVG).

Plan: a flat oval ankle band with a drop connector and a hollow teardrop
charm, on HRECT_L (centerline box (4,8)-(44,40), ink (2,6)-(46,42)).
Everything is mirrored about x=24.
- band: one closed contour, an ellipse about (24,13) with rx=20, ry=5, so
  its extremes sit on x=4, x=44 and y=8. The bottom half is split at
  (24,18) where the connector attaches.
- connector: a vertical line (24,18)-(24,26), 8 long, so the charm tip is
  a full 8 from the band on centerlines and the drop still reads at 48 px.
- charm: one closed teardrop contour. Bowl: an r5 arc about (24,35) from
  (29,35) under the bottom (24,40) to (19,35). Flanks: one cubic per side
  from the bowl apex, leaving vertically (tangent-continuous with the bowl),
  up to the tip (24,26), the one deliberate corner, where the connector
  ends. Height budget: band 10 + connector 8 + teardrop 14 = 32.
Keyshape: the metrics suggested HRECT_M (28 tall). On HRECT_M the budget
only allowed a 4-long connector, which put the charm tip 4 from the band
(the metrics clearance check fails it) and vanished at 48 px; HRECT_L
(scored 0.92, x already 100%) gives the 4 extra units.
Traced shape: anklet_raw.svg (read for the subject only; nothing copied
from its coordinates).
Lucide: no anklet; the droplet construction (round bowl + two curved flanks
to a tip) informs the charm, redrawn on this grid.

Metric issues:
- hole (charm opening 3.74 wide, need 6): fixed, the bowl is r5 at
  stroke 4, so the opening is 6 across; the flanks narrow only above it.
  The band opening is also 6 (ry=5).
- keyshape-short-axis (HRECT_M x fills 95%): fixed by moving to HRECT_L;
  band ends on x=4 and x=44, top y=8, charm bottom y=40.
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "83499877-9f6d-4f70-975d-59ade9b78b2f"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1805-anklet/anklet_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24            # mirror axis
BAND_Y = 13        # band centre y
BAND_RX = 20
BAND_RY = 5
BAND_BOTTOM = (AX, BAND_Y + BAND_RY)
TIP = (AX, 26)     # connector end and teardrop tip
BOWL_Y = 35        # bowl centre y
BR = 5             # bowl radius
LEFT = (AX - BR, BOWL_Y)
RIGHT = (AX + BR, BOWL_Y)


def mirror(p):
    return (2 * AX - p[0], p[1])


class AnkletRedraw(Solo48):
    icon_id = "anklet-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "fashion/jewelry"
    aliases = ("ankle-bracelet", "ankle-chain")
    keywords = ("anklet", "ankle bracelet", "jewelry", "charm", "pendant",
                "accessory")

    def build(self) -> None:
        east, west = (AX + BAND_RX, BAND_Y), (AX - BAND_RX, BAND_Y)
        self.add_arc("band-top", east, west, radius_x=BAND_RX, radius_y=BAND_RY, sweep=False)
        self.add_arc("band-bottom-left", west, BAND_BOTTOM, radius_x=BAND_RX, radius_y=BAND_RY, sweep=False)
        self.add_arc("band-bottom-right", BAND_BOTTOM, east, radius_x=BAND_RX, radius_y=BAND_RY, sweep=False)
        self.add_contour("band", "band-top", "band-bottom-left", "band-bottom-right", closed=True)

        self.add_line("connector", BAND_BOTTOM, TIP)

        # Teardrop: tip -> right flank (arriving vertically) -> bowl -> left flank.
        c1, c2 = (AX + 2, 29), (AX + BR, 31)
        self.add_bezier("flank-right", TIP, (c1, c2, RIGHT))
        self.add_arc("bowl", RIGHT, LEFT, radius_x=BR, sweep=True)
        self.add_bezier("flank-left", LEFT, (mirror(c2), mirror(c1), TIP))
        self.add_contour("charm", "flank-right", "bowl", "flank-left", closed=True)

        self.relate("connect", "connector", "band-bottom-left")
        self.relate("connect", "connector", "band-bottom-right")
        self.relate("connect", "connector", "flank-right")
        self.relate("connect", "connector", "flank-left")
