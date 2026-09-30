"""bearded-gnome-in-bent-cap (redraw of the new-pipeline traced SVG).

Plan: garden-gnome face as three detached parts on VRECT_L (centerline box
(8,4)-(40,44)), rebuilt on the 48 grid from the trace's reading, not its
coordinates. Brim, nose and beard share the axis x=AXIS and are mirrored;
the cap is deliberately asymmetric because its tip bends to the right.
- cap: one closed contour. Brim is a shallow upward arc (r34, sagitta 3)
  between the corners (8,20) and (36,20); the left side sweeps up to the
  apex (y=4 extreme), the crown rolls over to the drooping tip (x=40
  extreme), and the tip's underside curls back to a notch from which the
  right side drops to the brim corner.
- nose: 4-arc oval, rx5 ry4, centred on the axis, 9 below the brim crest.
- beard: one two-cubic run from the left tip beside the nose down to a
  rounded point on the axis (y=44 extreme) and back up the mirrored side.
Keyshape: metrics suggested VRECT_M, but its 28-wide box must also hold the
cap tip's overhang (4 past the brim), leaving the beard at most 12 either side
of the axis: under 8 of clearance around a readable 5-wide oval nose.
VRECT_L gives the 4 extra units (beard half width 14) and the tip reaches x=40.
No useful Lucide match (no gnome); construction follows Lucide's
single-weight outlines with round joins.

Metric issues fixed:
- clearance e0/e1 (cap vs nose, 3.18): nose top sits 9 below the brim crest.
- clearance e0/e2 (cap vs beard, 5.52): beard tips start 9 below the brim
  corners.
- clearance e1/e2 (nose vs beard, 4.48): beard tips sit 8+ outside the
  nose's side vertices; the beard widens before it narrows.
- hole (0.4 wide sliver at the nose): the sliver came from the nose touching
  the cap; the parts are now detached and the nose hole is 10x8 on centerlines.
- keyshape-short-axis: widened to VRECT_L and touching x=8 (cap and beard),
  x=40 (cap tip), y=4 (apex) and y=44 (beard point) exactly.
- stroke-width: redrawn at stroke 4 with 8-unit clearances throughout.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ecf9e5e2-2492-45f9-962a-2754de0f8147"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260929-1825-bearded-gnome-in-bent-cap/"
    "bearded-gnome-in-bent-cap_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 22
HALF = 14                      # brim / beard half width -> x = 8 .. 36
BRIM_Y = 20
BRIM_R = 34                    # chord 28, sagitta 3 -> crest at y=17
BL, BR = (AXIS - HALF, BRIM_Y), (AXIS + HALF, BRIM_Y)
APEX = (26, 4)
TIP = (40, 11)
NOTCH = (32, 13)
NOSE_C, NOSE_RX, NOSE_RY = (AXIS, 30), 5, 4
BEARD_TOP_Y = 29
BEARD_POINT = (AXIS, 44)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class BeardedGnomeInBentCapRedraw(Solo48):
    icon_id = "bearded-gnome-in-bent-cap-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ("gnome", "garden gnome", "dwarf")
    keywords = ("gnome", "beard", "cap", "hat", "fantasy", "dwarf", "garden", "elf")

    def build(self) -> None:
        # Cap, clockwise from the left brim corner.
        self.add_bezier("cap-left", BL, ((13, 10), (18, 4), APEX))
        self.add_bezier("cap-crown", APEX, ((33, 4), (40, 6), TIP))
        self.add_bezier("cap-tip", TIP, ((40, 14), (35, 10), NOTCH))
        self.add_bezier("cap-right", NOTCH, ((31, 14), (34, 17), BR))
        self.add_arc("brim", BR, BL, radius_x=BRIM_R, sweep=False)
        self.add_contour(
            "cap", "cap-left", "cap-crown", "cap-tip", "cap-right", "brim", closed=True,
        )

        cx, cy = NOSE_C
        rx, ry = NOSE_RX, NOSE_RY
        self.add_arc("nose-1", (cx, cy - ry), (cx + rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc("nose-2", (cx + rx, cy), (cx, cy + ry), radius_x=rx, radius_y=ry)
        self.add_arc("nose-3", (cx, cy + ry), (cx - rx, cy), radius_x=rx, radius_y=ry)
        self.add_arc("nose-4", (cx - rx, cy), (cx, cy - ry), radius_x=rx, radius_y=ry)
        self.add_contour("nose", "nose-1", "nose-2", "nose-3", "nose-4", closed=True)

        left_top = (AXIS - HALF, BEARD_TOP_Y)
        down = ((8, 39), (17, 41), BEARD_POINT)
        up = (mx(down[1]), mx(down[0]), mx(left_top))
        self.add_bezier("beard", left_top, down, up)
