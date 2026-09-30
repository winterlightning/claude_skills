"""crossed-fork-and-chef-knife (redraw of the new-pipeline traced SVG).

Subject: a fork and a chef knife crossed in an X -- the fork runs from its
two-tine head at the upper left to its stem end at the lower right; the
knife, in front, runs from its pointed tip at the upper right to a hollow
rounded handle at the lower left, and the fork stem passes under the blade.

Plan: SQUARE, centerline box (6,6)-(42,42), both utensils on 45 deg lines.
Knife frame: a = x - y (along the knife), p = x + y (across it).
Extremes: the fork sets all four -- left tine tip (6,12) gives x=6, right
tine tip (12,6) gives y=6, stem end (42,42) gives x=42 and y=42. The knife
sits inside them (tip (36,6) also reaches y=6).
- fork: axis x = y. Two tines parallel to the axis, 8.5 apart on centerlines
  (offsets (+-3,-+3)), joined by a semicircular cup (r 4.24, two tangent
  quarter cubics, knot on the axis at the apex (15,15)); the stem leaves the
  apex along the axis.
- knife: straight spine on p = 42 from the heel (15,27) to the tip (36,6);
  a perpendicular heel line on a = -12 from the spine down to the belly heel
  (26,38); the belly runs straight and parallel to the spine (p = 64,
  11.3 deep) to the crossing knot (32,32), then one tangent cubic sweeps
  out and rises into a pointed tip. The handle is flush with
  the spine: edges on p = 42 and p = 58 (11.3 apart, hole 7.3), closed by a
  semicircular cap (two quarter cubics, radius 5.66, knot at (10,40)).
- crossing: the knife is in front, so the fork stem stops on the knife
  outline instead of crossing it -- upper stem (15,15)->(21,21) ends on the
  spine, lower stem (32,32)->(42,42) starts on the belly; both share a split
  point of the outline and are declared connect (Lucide utensils-crossed
  uses the same abutting occlusion).
Budget along the fork axis: the cup apex must stay 8 from the spine
(apex (15,15) is 8.49 off p=42), and the heel must stay 8 from the lower
stem (heel line a=-12 is 8.49 from x=y), which fixes spine p=42, heel a=-12
and leaves a 2:1 blade-to-handle ratio, close to the generated PNG.
References: generated PNG for the subject; Lucide `utensils-crossed` for the
occlusion by abutting strokes. No trace coordinates copied.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- clearance e0/e3 (5.89) and e1/e3 (2.06): the fork's upper stem crowded the
  knife's bolster line and spine. Fixed: the bolster tick is dropped (the
  heel line alone marks it) and the stem ends on the spine as a declared
  joint; the cup apex is 8.49 from the spine.
- clearance e2/e5 (1.91): the lower fork stem floated next to the belly.
  Fixed: it starts on a belly knot as a declared joint.
- hole [30.1,20.9] (4.95): the blade interior; now 15.6 deep at the heel
  and 15.6 at the crossing, well over 6.
- hole [11.4,36.9] (1.0): the handle; now 11.3 wide on centerlines, 7.3 hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "aba5bfb7-5990-4b45-9606-e4cfe58ad1ea"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1037-crossed-fork-and-chef-knife/crossed-fork-and-chef-knife_raw.svg"
AUTHOR = "claude-opus-5-5"

K = 0.5523  # cubic quarter-circle handle ratio


def xy(a: float, p: float) -> tuple[float, float]:
    """Knife frame (a = x - y, p = x + y) to canvas."""
    return ((a + p) / 2, (p - a) / 2)


# fork: axis x = y
TINE_L_TIP, TINE_L_END = (6, 12), (9, 15)
TINE_R_TIP, TINE_R_END = (12, 6), (15, 9)
CUP_APEX = (15, 15)
CUP_K = 3 * K  # control offset per axis for the r=4.24 cup
STEM_TOP = (21, 21)     # on the spine
STEM_BOTTOM = (32, 32)  # on the belly
FORK_END = (42, 42)

# knife: spine p = 42, heel a = -12, handle p = 42..58
TIP = (36, 6)
HEEL_TOP = (15, 27)
HANDLE_HEEL = (23, 35)
HEEL_BOTTOM = (26, 38)
HANDLE_TOP_END = (10, 32)
CAP_APEX = (10, 40)
HANDLE_BOTTOM_END = (18, 40)
CAP_K = 4 * K  # control offset per axis for the r=5.66 cap


class CrossedForkAndChefKnifeRedraw(Solo48):
    icon_id = "crossed-fork-and-chef-knife-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/kitchen"
    aliases = ("fork and knife", "crossed cutlery", "kitchen utensils")
    keywords = ("fork", "knife", "chef", "cutlery", "utensils", "kitchen", "cooking", "restaurant", "dining")

    def build(self) -> None:
        # fork head: tine, cup, tine
        tx, ty = TINE_L_END
        ax, ay = CUP_APEX
        rx, ry = TINE_R_END
        self.add_line("tine-left", TINE_L_TIP, TINE_L_END)
        self.add_bezier("cup-left", TINE_L_END,
                        ((tx + CUP_K, ty + CUP_K), (ax - CUP_K, ay + CUP_K), CUP_APEX))
        self.add_bezier("cup-right", CUP_APEX,
                        ((ax + CUP_K, ay - CUP_K), (rx + CUP_K, ry + CUP_K), TINE_R_END))
        self.add_line("tine-right", TINE_R_END, TINE_R_TIP)
        self.add_contour("fork-head", "tine-left", "cup-left", "cup-right", "tine-right")
        self.add_line("stem-upper", CUP_APEX, STEM_TOP)
        self.add_line("stem-lower", STEM_BOTTOM, FORK_END)

        # knife blade
        self.add_line("heel-upper", HEEL_TOP, HANDLE_HEEL)
        self.add_line("heel-lower", HANDLE_HEEL, HEEL_BOTTOM)
        self.add_line("belly-heel", HEEL_BOTTOM, STEM_BOTTOM)
        self.add_bezier("belly-tip", STEM_BOTTOM, (xy(12, 64), xy(26, 50), TIP))
        self.add_line("spine-tip", TIP, STEM_TOP)
        self.add_line("spine-heel", STEM_TOP, HEEL_TOP)
        self.add_contour("blade", "heel-upper", "heel-lower", "belly-heel", "belly-tip",
                         "spine-tip", "spine-heel", closed=True)

        # knife handle, flush with the spine
        hx, hy = HANDLE_TOP_END
        cx, cy = CAP_APEX
        bx, by = HANDLE_BOTTOM_END
        self.add_line("handle-top", HEEL_TOP, HANDLE_TOP_END)
        self.add_bezier("cap-top", HANDLE_TOP_END,
                        ((hx - CAP_K, hy + CAP_K), (cx - CAP_K, cy - CAP_K), CAP_APEX))
        self.add_bezier("cap-bottom", CAP_APEX,
                        ((cx + CAP_K, cy + CAP_K), (bx - CAP_K, by + CAP_K), HANDLE_BOTTOM_END))
        self.add_line("handle-bottom", HANDLE_BOTTOM_END, HANDLE_HEEL)
        self.add_contour("handle", "handle-top", "cap-top", "cap-bottom", "handle-bottom")

        self.relate("connect", "handle", "blade")
        self.relate("connect", "stem-upper", "fork-head")
        self.relate("connect", "stem-upper", "blade")
        self.relate("connect", "stem-lower", "blade")
