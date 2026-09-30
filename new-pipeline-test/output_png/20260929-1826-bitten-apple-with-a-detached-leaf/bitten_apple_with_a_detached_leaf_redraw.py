"""bitten-apple-with-a-detached-leaf (redraw of the new-pipeline traced SVG).

Plan: an apple body with a shallow top cleft and a round bite out of its
right side, and one detached lens leaf tilted 45 degrees above it, on
VRECT_M (centerline box (10,4)-(38,44)).
- body: one closed contour built from the Lucide apple (24-grid body
  scaled x1.4 onto the 28-unit width). Lobes top out at (17,22) and (31,22)
  mirrored about x=24, the cleft corner sits at (24,25), the widest point
  is x=10 / x=38 and the base has a small dip (24,42) between two feet on
  y=44. Every smooth node has horizontal or vertical tangents on both sides.
- bite: a semicircle r=5 about (38,32), from (38,37) up to (38,27); its tips
  are the body's right extremes, reached with vertical tangents, so the
  bite corners are the only deliberate kinks besides the cleft.
- leaf: a closed lens between tips (24,14) and (34,4), mirrored about its
  45 degree axis x+y=38 with integer controls; the upper side arrives at
  (34,4) horizontally, so the tip is the top extreme and cannot overshoot.
Deliberate asymmetry: the bite and the leaf (the body is otherwise mirrored).

Keyshape: the metrics suggest SQUARE (score 0.98, from the "square" shape
hint), but SQUARE needs a 1.36 x-stretch to put the apple on both side
walls; VRECT_M needs only 1.05 (fill 1.00 x 0.96), so the subject keeps
its trace proportions. VRECT_M is used.

Metric issues fixed:
- stroke-width (info): drawn at stroke 4; every gap is sized for it.
- keyshape-short-axis (warn): moot on VRECT_M; the body reaches x=10 and
  x=38 (the bite tips and the left flank), the leaf tip y=4, the feet y=44.
- clearance e0/e1 (error, 2.76): the leaf now clears the body by >= 8.5 on
  centerlines (tip (24,14) is 11 above the cleft, the lower leaf side
  8.5 from the right lobe).
- hole (error, leaf interior 0.85): the lens is 8.5 wide on centerlines
  (4.5 of open ink), up from 0.85.
Not fixed: the metric's 6-unit inscribed-ink hole for the leaf would need
a lens 10 wide and about 17 long; with the 8-unit gap it pushes the apple
down to a 28 x 18 body, which no longer reads as an apple. The 8.5-unit
lens clears the Solo48 hole rule (>= 6 on centerlines).

Lucide: apple (body lobes, cleft, flanks and dipped base) informed the
construction; its stem stroke was replaced by the brief's detached leaf.
Traced shape: 20260929-1826-bitten-apple-with-a-detached-leaf/
bitten-apple-with-a-detached-leaf_raw.svg
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1da8830f-8f47-4740-95c5-b3e0c19b2899"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1826-bitten-apple-with-a-detached-leaf/"
    "bitten-apple-with-a-detached-leaf_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
LOBE_Y = 22          # lobe tops
LOBE_DX = 7          # lobe tops at AXIS -/+ 7
CLEFT = (AXIS, 25)
LEFT, RIGHT = 10, 38
FLANK_Y = 28         # widest point of the left flank
BASE_Y, DIP_Y = 44, 42
FOOT_DX = 6          # feet at AXIS -/+ 6
BITE_C, BITE_R = (38, 32), 5
LEAF_A, LEAF_B = (24, 14), (34, 4)


class BittenAppleWithADetachedLeafRedraw(Solo48):
    icon_id = "bitten-apple-with-a-detached-leaf-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/fruit"
    aliases = ("apple-bite", "bitten-apple")
    keywords = ("apple", "fruit", "bite", "leaf", "food", "snack", "healthy")

    def build(self) -> None:
        lobe_l = (AXIS - LOBE_DX, LOBE_Y)
        lobe_r = (AXIS + LOBE_DX, LOBE_Y)
        foot_l = (AXIS - FOOT_DX, BASE_Y)
        foot_r = (AXIS + FOOT_DX, BASE_Y)
        dip = (AXIS, DIP_Y)
        bite_lo = (RIGHT, BITE_C[1] + BITE_R)
        bite_hi = (RIGHT, BITE_C[1] - BITE_R)

        # Body, counter-clockwise from the cleft: left lobe, flank, base,
        # right foot, bite, right lobe.
        self.add_bezier("body-left", CLEFT,
                        ((22.6, 24.2), (20, LOBE_Y), lobe_l),
                        ((13, LOBE_Y), (LEFT, 25), (LEFT, FLANK_Y)),
                        ((LEFT, 34), (14, BASE_Y), foot_l),
                        ((21, BASE_Y), (21, DIP_Y), dip))
        self.add_bezier("body-right", dip,
                        ((27, DIP_Y), (27, BASE_Y), foot_r),
                        ((34, BASE_Y), (RIGHT, 41), bite_lo))
        self.add_arc("bite", bite_lo, bite_hi, radius_x=BITE_R, sweep=True)
        self.add_bezier("body-top", bite_hi,
                        ((RIGHT, 25), (35, LOBE_Y), lobe_r),
                        ((28, LOBE_Y), (25.4, 24.2), CLEFT))
        self.add_contour("apple", "body-left", "body-right", "bite",
                         "body-top", closed=True)

        # Leaf: lens mirrored about its axis x + y = 38.
        self.add_bezier("leaf-upper", LEAF_A, ((24, 6), (26, 4), LEAF_B))
        self.add_bezier("leaf-lower", LEAF_B, ((34, 12), (32, 14), LEAF_A))
        self.add_contour("leaf", "leaf-upper", "leaf-lower", closed=True)
