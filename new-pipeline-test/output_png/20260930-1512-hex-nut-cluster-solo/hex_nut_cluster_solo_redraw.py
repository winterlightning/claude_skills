"""hex-nut-cluster-solo (redraw of the new-pipeline traced SVG).

Plan: SQUARE, centerline box (6,6)-(42,42); three pointy-top hex nuts packed
as a triad (one centred above two), mirrored about x=24.
- one hex definition: half-width 9, points 10 above/below the centre,
  shoulders 6 above/below (18 wide flat-to-flat, 20 tall).
- bottom nuts centred (15,32) and (33,32); top nut centred (24,16). The
  honeycomb offset (9 across, 16 up) makes every neighbouring pair share one
  edge exactly, so the nuts read as packed together: the left nut is a closed
  hex, the right nut is an open run on the left nut's shared wall x=24, and
  the top nut is an open run from the left nut's top point over to the right
  nut's top point (its lower edges are the bottom nuts' upper edges).
- each nut's bore is a centre dot: 9 from the flat walls and 9.1 from the
  slanted walls.
Extremes: x 6/42 from the bottom nuts' outer walls, y 6 from the top nut's
point and 42 from the bottom nuts' points.
Metric issues fixed:
- clearance e0..e5 (every hex/ring pair 3.2-7.9 apart): no distinct parts sit
  closer than 8 any more; neighbouring hexes share walls and nodes (declared
  connect) and each bore dot is at least 9 from every wall.
- holes at (24.0,9.1), (19.4,29.2), (39.2,29.3) (1.5 wide slivers between
  hexes and rings) and (23.9,15.6), (13.9,32.7), (33.7,32.7) (3.4 wide ring
  bores): the rings are gone; each nut is one clean hex cell (interior
  inscribed ~14) with a solid bore dot, and there are no slivers.
- stroke-width: authored at stroke 4 with every gap budgeted on centerlines.
Not fixable as traced:
- three separate nuts with white gaps: a bore mark needs a hex inradius of 8
  (a ring bore needs 11), and three separated hexes with 8-unit gaps then
  need at least 40 x 39 of centerline box, more than SQUARE's 36 x 36 (or
  any SOLO48 keyshape). The nuts are therefore packed edge to edge.
- ring bores: a ring (r3, the smallest exempt ring) plus 8 clearance needs a
  hex 22 wide; two of them side by side need 44. The bore is a dot instead.
Lucide: `hexagon` / `bolt` (hex outline with a centred bore) for the nut.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e9326841-b6b1-432e-a99d-c2065849139b"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1512-hex-nut-cluster-solo/"
    "hex-nut-cluster-solo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# One pointy-top hex: flat walls at cx +- HALF_W, points at cy +- TIP,
# shoulders at cy +- SHOULDER.
HALF_W, TIP, SHOULDER = 9, 10, 6
LEFT, RIGHT, TOP = (15, 32), (33, 32), (24, 16)


def hex_points(centre: tuple[int, int]) -> dict[str, tuple[int, int]]:
    cx, cy = centre
    return {
        "top": (cx, cy - TIP),
        "ur": (cx + HALF_W, cy - SHOULDER),
        "lr": (cx + HALF_W, cy + SHOULDER),
        "bottom": (cx, cy + TIP),
        "ll": (cx - HALF_W, cy + SHOULDER),
        "ul": (cx - HALF_W, cy - SHOULDER),
    }


class HexNutClusterSoloRedraw(Solo48):
    icon_id = "hex-nut-cluster-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("hex nuts", "nuts", "hardware", "nut cluster")
    keywords = ("nut", "hex", "hexagon", "hardware", "bolt", "fastener", "screw", "parts")

    def build(self) -> None:
        left, right, top = hex_points(LEFT), hex_points(RIGHT), hex_points(TOP)

        # -- left nut: the one closed hex ---------------------------------
        self.add_polyline(
            "nut-left", left["top"], left["ur"], left["lr"], left["bottom"],
            left["ll"], left["ul"], closed=True,
        )
        # -- right nut: shares the left nut's wall x=24 --------------------
        self.add_polyline(
            "nut-right", right["ul"], right["top"], right["ur"], right["lr"],
            right["bottom"], right["ll"],
        )
        self.relate("connect", "nut-right", "nut-left")
        # -- top nut: its lower edges are the bottom nuts' upper edges ------
        self.add_polyline(
            "nut-top", top["ll"], top["ul"], top["top"], top["ur"], top["lr"],
        )
        self.relate("connect", "nut-top", "nut-left")
        self.relate("connect", "nut-top", "nut-right")

        # -- bores ----------------------------------------------------------
        self.add_dot("bore-left", LEFT)
        self.add_dot("bore-right", RIGHT)
        self.add_dot("bore-top", TOP)
