"""crane-hook-beneath-tapered-block (redraw of the new-pipeline traced SVG).

Plan: a hoist block over a crane hook on VRECT_M (centerline box
(10,4)-(38,44)), the keyshape the metrics suggested for this tall subject.
- block: one closed trapezoid, mirror-symmetric about x=24. Its top wall
  spans the full box width (10..38 on y=4), so it owns the top, left and
  right extremes; the bottom wall is 12 wide (18..30 on y=BLOCK_BOTTOM), the
  image's strong taper (bottom about 0.43 of the top).
- hook: one open contour on the x=24 axis. A short upright shank drops from
  8 below the block to the top of a radius-7 bowl centred on the axis, then
  the bowl runs counterclockwise through its left, bottom (y=44, the bottom
  extreme) and right points, and a short tip flares up and outward from the
  right point to (34,33), the image's outward-kinked point, which keeps the
  hook's throat open (tip to shank end 10.4 on centerlines).
  The shank meets the bowl with a deliberate round-joined corner, as the
  generated image's shank kinks into the bowl.
Vertical budget (40): block 14, gap 8, shank 4, bowl 14.
Lucide `anchor`/`cable-car` offered no direct hook; the construction (shank +
circular bowl + short tip) follows the generated image, simplified.

Metric issues (crane-hook-beneath-tapered-block_metrics.json):
- stroke-width (info, trace 2.66 after fitting): redrawn at stroke 4; every
  gap budgeted for 4 (hook tip to shank end 10.4 on centerlines).
- keyshape-short-axis (warn, x filled 86%): the block's top wall now spans
  x=10..38, so both VRECT_M x extremes are exact; y=4 and y=44 are the block
  top and hook bottom.
- clearance e0/e1 (error, 3.26 apart): the shank now starts exactly 8 below
  the block's bottom wall.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a48942b9-22b4-5473-bb69-75298cd6eb3f"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1051-crane-hook-beneath-tapered-block/crane-hook-beneath-tapered-block_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP, BOTTOM = 4, 44
TOP_HALF = 14                   # block top wall 10..38
BLOCK_BOTTOM = 18
BOTTOM_HALF = 6                 # block bottom wall 18..30
SHANK_TOP = BLOCK_BOTTOM + 8
R = 7                           # bowl radius
BOWL_CY = BOTTOM - R            # 37
TIP = (AXIS + R + 3, BOWL_CY - 4)  # (34,33): tip flares up and out, as in the image


class CraneHookBeneathTaperedBlockRedraw(Solo48):
    icon_id = "crane-hook-beneath-tapered-block-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("crane hook", "hoist", "lifting hook", "pulley block")
    keywords = ("crane", "hook", "hoist", "lift", "block", "construction",
                "cargo", "load", "rigging")

    def build(self) -> None:
        self.add_polyline(
            "block",
            (AXIS - TOP_HALF, TOP), (AXIS + TOP_HALF, TOP),
            (AXIS + BOTTOM_HALF, BLOCK_BOTTOM), (AXIS - BOTTOM_HALF, BLOCK_BOTTOM),
            closed=True,
        )

        top, left = (AXIS, BOWL_CY - R), (AXIS - R, BOWL_CY)
        bottom, right = (AXIS, BOWL_CY + R), (AXIS + R, BOWL_CY)
        self.add_line("hook-shank", (AXIS, SHANK_TOP), top)
        self.add_arc("hook-bowl-1", top, left, radius_x=R, sweep=False)
        self.add_arc("hook-bowl-2", left, bottom, radius_x=R, sweep=False)
        self.add_arc("hook-bowl-3", bottom, right, radius_x=R, sweep=False)
        self.add_line("hook-tip", right, TIP)
        self.add_contour("hook", "hook-shank", "hook-bowl-1", "hook-bowl-2",
                         "hook-bowl-3", "hook-tip")
