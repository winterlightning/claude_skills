"""crane-hook-with-square-mount (redraw of the new-pipeline traced SVG).

Plan: a square mounting block over one open J-shaped crane hook on VRECT_M
(centerline box (10,4)-(38,44)), the keyshape the metrics suggested for this
tall subject.
- mount: one closed square, 12x12, mirror-symmetric about x=24 (18..30,
  4..16). Its top wall owns the top extreme. The bottom wall is split at the
  axis so the hook shank shares its endpoint (24,16) (declared connect).
- hook: one open contour. A short upright shank drops from the mount, a
  tangent S-cubic swings it right onto the bowl's right point, then a broad
  radius-14 semicircle centred at (24,30) runs clockwise through its bottom
  (y=44, the bottom extreme) to its left point, and a short upright tip
  rises from there, as in the generated image. The bowl's right and left
  points own the x extremes 38 and 10.
Vertical budget (40): mount 12, shank 4, S-curve 10, bowl 14.
Lucide `anchor` gave the idea of a single broad bowl with an upturned tip;
no direct crane-hook match. The mount and bowl share the x=24 axis; the
hook is deliberately asymmetric (shank swings right, tip rises left).

Metric issues (crane-hook-with-square-mount_metrics.json):
- stroke-width (info, trace 2.67 after fitting): redrawn at stroke 4; every
  gap is budgeted for 4 (mount corner to S-curve and tip to mount both
  clear 8 on centerlines).
- keyshape-short-axis (warn, x filled 47%): the bowl is widened to radius 14,
  the brief's "broad semicircular bottom curve", so its left and right
  points sit exactly on x=10 and x=38; y=4 is the mount top and y=44 the
  bowl bottom. The mount stays square rather than being stretched.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fd80bcd7-73ab-4b8e-8a28-7672b7384731"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1054-crane-hook-with-square-mount/crane-hook-with-square-mount_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP, BOTTOM = 4, 44
HALF = 6                        # mount 18..30
MOUNT_BOTTOM = TOP + 2 * HALF   # 16: square
SHANK_END = MOUNT_BOTTOM + 4    # 20
R = 14                          # bowl radius: 10..38
BOWL_CY = BOTTOM - R            # 30
TIP_TOP = BOWL_CY - 4           # 26


class CraneHookWithSquareMountRedraw(Solo48):
    icon_id = "crane-hook-with-square-mount-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("crane hook", "hoist hook", "lifting hook")
    keywords = ("crane", "hook", "hoist", "lift", "mount", "construction",
                "cargo", "load", "rigging")

    def build(self) -> None:
        left, right = AXIS - HALF, AXIS + HALF
        joint = (AXIS, MOUNT_BOTTOM)
        self.add_polyline(
            "mount",
            joint, (left, MOUNT_BOTTOM), (left, TOP), (right, TOP),
            (right, MOUNT_BOTTOM), closed=True,
        )

        bowl_right, bowl_bottom = (AXIS + R, BOWL_CY), (AXIS, BOTTOM)
        bowl_left = (AXIS - R, BOWL_CY)
        self.add_line("hook-shank", joint, (AXIS, SHANK_END))
        self.add_bezier("hook-swing", (AXIS, SHANK_END),
                        ((AXIS, SHANK_END + 6), (AXIS + R, BOWL_CY - 6), bowl_right))
        self.add_arc("hook-bowl-1", bowl_right, bowl_bottom, radius_x=R, sweep=True)
        self.add_arc("hook-bowl-2", bowl_bottom, bowl_left, radius_x=R, sweep=True)
        self.add_line("hook-tip", bowl_left, (AXIS - R, TIP_TOP))
        self.add_contour("hook", "hook-shank", "hook-swing", "hook-bowl-1",
                         "hook-bowl-2", "hook-tip")
        self.relate("connect", "mount", "hook")
