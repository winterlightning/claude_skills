"""croissant (redraw of the new-pipeline traced SVG, batch 011 #10).

Subject: a front-view croissant, a wide crescent whose two tips curl down,
with two curved seams cutting the plump middle from the side lobes.

Plan: HRECT_M (centerline box (4,10)-(44,38)), the suggested keyshape.
One closed crust contour mirrored about x 24, plus two mirrored seams.
- dome: arc about (24,25) radius 15 (a 3-4-5 triangle) from the seam
  nodes (12,16) / (36,16) over the apex (24,10), the y 10 extreme.
- lobes: cubics leaving the dome tangent-continuously, widest on x 4 / 44
  at y 28 and turning into the tips (8,38) / (40,38), the y 38 extremes.
- inner edge: from each tip up to the seam foot (17,29) / (31,29), then a
  shallow arch over (24,28); the tips are shared nodes, so the converging
  crust and inner edge there are exempt from internal spacing.
- seams: cubics from the dome nodes bowing toward the centre down to the
  seam feet, split nodes on both ends and declared connected.
Lucide `croissant` (segmented crescent) informed the seam cells; the
image's symmetric front view was kept instead of Lucide's diagonal.

Metric issues (croissant-batch-011-10_metrics.json):
- stroke-width (info, trace 2.67 fitted): redrawn at stroke 4 with every
  cell budgeted so the side-lobe holes stay above 6 inscribed at stroke 4.
- keyshape-short-axis (warn, HRECT_M y fill 86%): fixed; the dome apex is
  on y 10 and the tips on y 38, the lobes on x 4 / 44, so all four extremes
  sit exactly on the box.
The small inward tip hooks of the trace are dropped: at 48 px they closed
into blobs; the tips are plain rounded points.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f9e55377-8da9-5927-845b-403bea7db251"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1056-croissant-batch-011-10/croissant-batch-011-10_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
DOME_CY, DOME_R = 25, 15      # apex y 10
SEAM_TOP = (12, 16)           # left dome node (3-4-5 off the dome centre)
SIDE = (4, 28)                # widest point of the left lobe
TIP = (8, 38)                 # left tip
SEAM_FOOT = (17, 29)          # left seam foot on the inner edge
ARCH_APEX_Y = 28


def _m(p):
    return (2 * AXIS - p[0], p[1])


def _mt(t):
    return (-t[0], t[1])


def _rev(t):
    return (-t[0], -t[1])


def _rmt(t):
    """Mirrored and reversed tangent (a left-half direction on the right half, travelling back)."""
    return (t[0], -t[1])


def _hermite(knots):
    """Cubic segments through knots with given tangent directions."""
    segs = []
    for (p0, t0), (p1, t1) in zip(knots, knots[1:]):
        d = ((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2) ** 0.5 / 3
        n0 = (t0[0] ** 2 + t0[1] ** 2) ** 0.5
        n1 = (t1[0] ** 2 + t1[1] ** 2) ** 0.5
        c1 = (round(p0[0] + t0[0] / n0 * d, 3), round(p0[1] + t0[1] / n0 * d, 3))
        c2 = (round(p1[0] - t1[0] / n1 * d, 3), round(p1[1] - t1[1] / n1 * d, 3))
        segs.append((c1, c2, p1))
    return segs


# Tangents on the left half (travelling tip -> lobe -> dome, and dome -> seam foot).
T_TIP_UP = (-1, -1)           # crust leaving the tip upward and outward
T_SIDE = (0, -1)
T_DOME = (3, -4)              # dome tangent at (12,16), perpendicular to (-12,-9)
T_SEAM_TOP = (1, 1)
T_SEAM_FOOT = (0, 1)
T_INNER_TIP = (1, -1.3)       # inner edge leaving the tip toward the seam foot
T_INNER_FOOT = (1, -0.25)


class CroissantBatch01110Redraw(Solo48):
    icon_id = "croissant-batch-011-10-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/bakery"
    aliases = ("croissant", "crescent roll", "pastry")
    keywords = ("croissant", "pastry", "bakery", "breakfast", "french", "bread", "food", "cafe")

    def build(self) -> None:
        top_l, top_r = SEAM_TOP, _m(SEAM_TOP)
        foot_l, foot_r = SEAM_FOOT, _m(SEAM_FOOT)
        tip_l, tip_r = TIP, _m(TIP)
        side_l, side_r = SIDE, _m(SIDE)
        apex = (AXIS, ARCH_APEX_Y)

        self.add_bezier("lobe-l", tip_l, *_hermite([
            (tip_l, T_TIP_UP), (side_l, T_SIDE), (top_l, T_DOME)]))
        self.add_arc("dome", top_l, top_r, radius_x=DOME_R, sweep=True)
        self.add_bezier("lobe-r", top_r, *_hermite([
            (top_r, _rmt(T_DOME)), (side_r, _rmt(T_SIDE)), (tip_r, _rmt(T_TIP_UP))]))
        self.add_bezier("inner-r", tip_r, *_hermite([
            (tip_r, _mt(T_INNER_TIP)), (foot_r, _mt(T_INNER_FOOT))]))
        self.add_bezier("arch", foot_r, *_hermite([
            (foot_r, _mt(T_INNER_FOOT)), (apex, (-1, 0)), (foot_l, _rev(T_INNER_FOOT))]))
        self.add_bezier("inner-l", foot_l, *_hermite([
            (foot_l, _rev(T_INNER_FOOT)), (tip_l, _rev(T_INNER_TIP))]))
        self.add_contour("crust", "lobe-l", "dome", "lobe-r", "inner-r", "arch", "inner-l", closed=True)

        self.add_bezier("seam-l", top_l, *_hermite([(top_l, T_SEAM_TOP), (foot_l, T_SEAM_FOOT)]))
        self.add_bezier("seam-r", top_r, *_hermite([(top_r, _mt(T_SEAM_TOP)), (foot_r, T_SEAM_FOOT)]))
        self.relate("connect", "seam-l", "crust")
        self.relate("connect", "seam-r", "crust")
