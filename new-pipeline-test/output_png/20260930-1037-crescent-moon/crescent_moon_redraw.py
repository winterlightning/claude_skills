"""Crescent moon, redrawn from the PNG-pipeline trace on SOLO48.

Plan: one closed contour of two circular arcs, a broad crescent opening to
the upper right, mirrored about the 45-degree diagonal through (24,24).
- CIRCLE keyshape (the metrics suggestion, score 1.23, round shape hint):
  the outer arc is the keyshape circle itself, radius 20 about (24,24), so
  it touches the radial envelope exactly (ink radius 22).
- Horn tips on that circle at the top (24,4) and right (44,24) cardinal
  points, the grid points nearest the trace's (23,4) and (44,28); they are
  mirror images across the diagonal, so both tips get the same angle.
- Bite arc radius 15 through both tips (large arc). Its centre falls on the
  diagonal at about (30.5,17.5), close to the trace's (32.4,16.8) r15.5, so
  the crescent keeps the trace's weight: 14.1 between centrelines at the
  thickest point, a 10-unit inked hole.
- Lucide `moon` informs the construction: two opposing circular arcs, no
  corners except the two tips.

Metric issues:
- stroke-width (info): the trace is 3.02 after fitting; redrawn at stroke 4.
  The only gap that shrinks is the hole, which stays ~10 wide (min 6).
No other issues were listed (no junctions, clearances or human parts).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f947813-75bf-523b-bb36-5f6abbd3d57b"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1037-crescent-moon/crescent-moon_raw.svg"
AUTHOR = "claude-opus-5-5"

OUTER_R = 20          # keyshape circle about (24,24)
TIP_TOP = (24, 4)
TIP_RIGHT = (44, 24)  # mirror of TIP_TOP across the diagonal
BITE_R = 15           # centre lands on the diagonal, ~(30.5,17.5)


class CrescentMoonRedraw(Solo48):
    icon_id = "crescent-moon-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "weather"
    aliases = ("crescent", "moon")
    keywords = ("moon", "crescent", "lunar", "night", "sleep", "dark mode", "sky", "astrology")

    def build(self) -> None:
        self.add_arc("outer", TIP_TOP, TIP_RIGHT, radius_x=OUTER_R, large_arc=True, sweep=False)
        self.add_arc("bite", TIP_RIGHT, TIP_TOP, radius_x=BITE_R, large_arc=True, sweep=True)
        self.add_contour("crescent", "outer", "bite", closed=True)
