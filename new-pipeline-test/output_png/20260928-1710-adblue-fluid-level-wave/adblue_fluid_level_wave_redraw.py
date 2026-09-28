"""adblue-fluid-level-wave (redraw of the new-pipeline traced SVG).

Plan: an upright droplet with one short fluid-level wave, on VRECT_M
(centerline box (10,4)-(38,44), ink (8,2)-(40,46)).
- droplet: one closed contour, mirrored about x=24.
  - bowl: an r14 arc about (24,30); its left, bottom and right apexes are
    (10,30), (24,44), (38,30), so it touches the box on x=10, x=38 and y=44
    exactly.
  - flanks: one cubic per side from the bowl apex up to the tip (24,4). The
    control at the bowl leaves vertically, so the flank-to-bowl join is
    tangent-continuous; the tip is the one deliberate corner.
- wave: a tilde of two cubics, point-symmetric about the bowl centre
  (24,30), tangent-continuous at the centre. Every wave point stays within
  radius 5.1 of (24,30), so it sits >= 8.9 from the bowl on centerlines, and
  it is far below the flanks.
Traced shape: 20260928-1710-adblue-fluid-level-wave/adblue-fluid-level-wave_raw.svg
(read for the subject only; nothing copied from its coordinates).
Lucide: droplet (round bowl + two curved flanks meeting in a pointed tip)
informs the droplet construction, redrawn on this grid and keyshape.

Metric issues:
- clearance e0/e2 (wave 3.77 from the droplet): fixed, the wave is rebuilt
  inside the radius-6 zone of the bowl centre, >= 8.9 from the outline.
- clearance e1/e2 (wave 7.62 from the droplet): fixed by the same rebuild.
- narrow-join e0/e1 (4.11 deg wedge): fixed, the trace split the outline
  into two paths meeting at a sliver; the droplet is now one closed contour
  with a tangent flank-to-bowl join and no wedge.
- keyshape-short-axis (x fills 86%): fixed, the bowl apexes sit on x=10 and
  x=38, the tip on y=4 and the bottom on y=44.
- stroke-width (info): drawn at stroke 4; all gaps budgeted for 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ddba64a9-7a33-401d-9571-bce55808907f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1710-adblue-fluid-level-wave/"
    "adblue-fluid-level-wave_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AX = 24          # mirror axis
TIP = (AX, 4)
BC = (AX, 30)    # bowl centre
BR = 14          # bowl radius
LEFT = (AX - BR, 30)
RIGHT = (AX + BR, 30)


def mirror(p):
    return (2 * AX - p[0], p[1])


def about_centre(p):
    return (2 * BC[0] - p[0], 2 * BC[1] - p[1])


class AdblueFluidLevelWaveRedraw(Solo48):
    icon_id = "adblue-fluid-level-wave-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle-fluids"
    aliases = ("adblue", "def-fluid", "diesel-exhaust-fluid")
    keywords = ("adblue", "def", "diesel exhaust fluid", "fluid level", "droplet", "liquid", "wave", "urea")

    def build(self) -> None:
        # Right flank: tip -> bowl apex, arriving vertically.
        c1, c2 = (27, 11), (38, 20)
        self.add_bezier("flank-right", TIP, (c1, c2, RIGHT))
        self.add_arc("bowl", RIGHT, LEFT, radius_x=BR, sweep=True)
        self.add_bezier("flank-left", LEFT, (mirror(c2), mirror(c1), TIP))
        self.add_contour("droplet", "flank-right", "bowl", "flank-left", closed=True)

        # Wave: rise, then fall through the centre, mirrored through (24,30).
        start = (19, 31)
        a1, a2 = (20.6, 29.2), (22.4, 28.8)
        self.add_bezier(
            "wave", start,
            (a1, a2, BC),
            (about_centre(a2), about_centre(a1), about_centre(start)),
        )
