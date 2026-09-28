"""adjacent-teeth-with-braces (redraw of the new-pipeline traced SVG).

Plan: two equal molars side by side on HRECT_M (centerline box
(4,10)-(44,38)), one bracket per tooth and one straight wire crossing both.
- tooth: 16 wide, repeated at x=4 and x=28 (8 apart, so the gap between the
  teeth is a clean 4-unit ink channel). Crown = two r5 cusp arcs about
  (x+5,15) and (x+11,15) meeting at a notch (x+8,11) (3-4-5 point, so the
  cusp tops land exactly on y=10); straight side walls down to the neck
  (y=26), then vertical-in/vertical-out cubics step the walls in by 2 to two
  r3 root lobes about (x+5,35) and (x+11,35) reaching y=38, meeting at a
  root notch (x+8,35).
- wire: y=23, x=4..44, split at every wall and bracket so each contact is a
  shared integer endpoint declared `connect`.
- bracket: a vertical bar (x+8, 20..26) across the wire, 9 below the crown
  notch and 9 above the root notch, 8 from each wall.
No local Lucide original was consulted; the cusped crown and lobed roots
follow the usual line-icon molar. The generated PNG gave the paired teeth and the wire running edge to edge.

Metric issues (adjacent-teeth-with-braces_metrics.json):
- clearance errors (e0..e4, teeth/brackets/wire fused or 1-7.8 apart in the
  trace): fixed -- teeth are 8 apart, brackets 8+ from every wall and notch,
  every real contact (wire/wall, wire/bracket) shares an endpoint + connect.
- holes 1.97-3.69 inscribed (bracket halves split by the wire, narrow root
  channels): fixed -- the bracket box is reduced to a bar so no tiny holes
  remain, and the deep root split is reduced to two lobes; each tooth keeps
  two openings (above and below the wire) wider than 6.
- keyshape-short-axis (y filled 84%): fixed -- cusps reach y=10, root lobes
  y=38, walls x=4 and x=44.
- loose-join (wire ends 1.2-1.4 short of the walls): fixed -- wire ends on
  the outer walls at (4,23) and (44,23), shared endpoints, connect.
- stroke-width (trace 2.63): redrawn at stroke 4.
Not kept: the square bracket outline (a box crossed by the wire needs 20 units
of height for two 6-unit holes; a 10-unit box beside the wire would sit 3 from
the tooth wall), the crown-to-crown touch (would fuse the teeth into a
sub-8 V), and the deep root split (needs 24 units per tooth at stroke 4).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4fe6a86e-b26a-405a-9e35-84f3c5a12b9e"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1717-adjacent-teeth-with-braces/adjacent-teeth-with-braces_raw.svg"
AUTHOR = "claude-opus-5-5"

TOOTH_W = 16
TOOTH_XS = (4, 28)          # left walls; right walls at x + 16
TOP, BOTTOM = 10, 38
CUSP_R = 5
CUSP_Y = 15                 # cusp centres (x+5, 15), (x+11, 15)
CROWN_NOTCH_Y = 11          # (x+8, 11) lies on both r5 cusps
NECK_Y = 26                 # walls stay straight down to here
ROOT_IN = 2                 # roots step in 2 from each wall
ROOT_R = 3
ROOT_Y = BOTTOM - ROOT_R    # lobe centres (x+5, 35), (x+11, 35)
WIRE_Y = 23
BRACKET = (20, 26)          # bar ends; wire crosses at 23


class AdjacentTeethWithBracesRedraw(Solo48):
    icon_id = "adjacent-teeth-with-braces-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ("dental braces", "orthodontics", "teeth braces")
    keywords = ("teeth", "tooth", "braces", "orthodontic", "bracket", "wire", "dental", "dentist")

    def _tooth(self, name: str, x: int) -> None:
        mid, right = x + TOOTH_W // 2, x + TOOTH_W
        p = name + "-"
        # Crown: two cusps meeting at a notch; straight walls to the neck.
        self.add_arc(p + "cusp-l", (x, CUSP_Y), (mid, CROWN_NOTCH_Y), radius_x=CUSP_R)
        self.add_arc(p + "cusp-r", (mid, CROWN_NOTCH_Y), (right, CUSP_Y), radius_x=CUSP_R)
        self.add_line(p + "wall-r1", (right, CUSP_Y), (right, WIRE_Y))
        self.add_line(p + "wall-r2", (right, WIRE_Y), (right, NECK_Y))
        # Neck to root: vertical-in, vertical-out cubic, stepping in by ROOT_IN.
        self.add_bezier(p + "taper-r", (right, NECK_Y),
                        ((right, NECK_Y + 4), (right - ROOT_IN, ROOT_Y - 4), (right - ROOT_IN, ROOT_Y)))
        self.add_arc(p + "root-r", (right - ROOT_IN, ROOT_Y), (mid, ROOT_Y), radius_x=ROOT_R)
        self.add_arc(p + "root-l", (mid, ROOT_Y), (x + ROOT_IN, ROOT_Y), radius_x=ROOT_R)
        self.add_bezier(p + "taper-l", (x + ROOT_IN, ROOT_Y),
                        ((x + ROOT_IN, ROOT_Y - 4), (x, NECK_Y + 4), (x, NECK_Y)))
        self.add_line(p + "wall-l2", (x, NECK_Y), (x, WIRE_Y))
        self.add_line(p + "wall-l1", (x, WIRE_Y), (x, CUSP_Y))
        self.add_contour(name, *(p + s for s in (
            "cusp-l", "cusp-r", "wall-r1", "wall-r2", "taper-r", "root-r",
            "root-l", "taper-l", "wall-l2", "wall-l1",
        )), closed=True)

    def build(self) -> None:
        wire_nodes = []
        for i, x in enumerate(TOOTH_XS):
            self._tooth(f"tooth-{i + 1}", x)
            wire_nodes += [(x, WIRE_Y), (x + TOOTH_W // 2, WIRE_Y), (x + TOOTH_W, WIRE_Y)]
        self.add_polyline("wire", *wire_nodes)
        for i, x in enumerate(TOOTH_XS):
            bx = x + TOOTH_W // 2
            self.add_polyline(f"bracket-{i + 1}", (bx, BRACKET[0]), (bx, WIRE_Y), (bx, BRACKET[1]))
            self.relate("connect", "wire", f"tooth-{i + 1}")
            self.relate("connect", f"bracket-{i + 1}", "wire")
