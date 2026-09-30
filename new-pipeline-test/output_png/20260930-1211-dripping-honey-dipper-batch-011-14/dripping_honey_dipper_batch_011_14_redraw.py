"""dripping-honey-dipper-batch-011-14 (redraw of the new-pipeline traced SVG).

Plan: a honey dipper tilted up to the right on the trace's ~27 degree axis,
drawn on the (2,-1) lattice direction so every node stays on the grid, with a
separate drop hanging below the head's lower tip. SQUARE, centerline box
(6,6)-(42,42).
- head: one closed capsule contour along AXIS=(2,-1): top side (15,12)-(23,8),
  bottom side offset by SIDE=(6,12) (width sqrt(180) = 13.4), and two
  half-circle caps of radius sqrt(45) about (18,18) and (26,14), each built
  from two quarter cubics, so caps meet the sides tangent-continuously and
  the apexes (12,21) and (32,11) are integer.
- grooves: the two crosswise lines at the cap joins, 4 axis steps (8.94)
  apart. The head reads as two rounded end bands and a middle band, which is
  how the trace's head looks.
- handle: one straight stroke from the upper cap apex (32,11), along the same
  axis, to the (42,6) corner.
- drop: a teardrop, tip (10,31) just left of the lower apex, radius-4 bowl on
  (10,38). Its left and bottom edges set the x=6 and y=42 extremes.
Keyshape: SQUARE, as suggested. The handle end sets x=42 and y=6 and the drop
sets x=6 and y=42. The head caps stay inside, with the left edge at 11.3 and
the top at 7.3.
Metric issues fixed:
- stroke-width 2.38 -> 4 (every clearance re-budgeted for 4).
- keyshape-short-axis (x filled 86%) -> every extreme lies exactly on the box.
- clearance e0/e2 5.1 (head outline vs handle) -> the handle starts at the
  cap apex as one connected part, collinear with the head axis.
- clearance e1/e3 3.68 (groove vs neck contour) -> grooves end on the outline
  at shared nodes, 8.94 apart. The separate neck contour is gone.
- clearance e0/e4 3.93 and e1/e4 5.08 (head vs drop) -> drop tip is 8.56 from
  the lower cap on centerlines (>= 8).
- holes 1.41 / 0.85 / 3.67 / 2.84 -> end bands are half discs (radius 6.7),
  the middle band is 8.94 x 13.4 and the drop bowl diameter is 8.
Nothing was dropped. The trace's hollow handle (e2) and neck contour (e3)
became the single-stroke handle the brief asked for.
validate_icon: valid, 0 warnings; build_gate: PASS, 0 errors, 0 warnings.
Lucide: droplet (tip + round bowl joined by smooth cubics). Lucide has no
honey dipper.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "938032ae-5024-5ede-94da-88527f48269f"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1211-dripping-honey-dipper-batch-011-14/"
    "dripping-honey-dipper-batch-011-14_raw.svg"
)
AUTHOR = "claude-opus-5-5"

K = 0.5523               # quarter-circle cubic handle ratio
AXIS = (2, -1)           # one lattice step along the dipper
SIDE = (6, 12)           # top side -> bottom side, perpendicular to AXIS
T0 = (15, 12)            # top side, lower-cap end
BAND = 4                 # axis steps between the two grooves
HANDLE_END = (42, 6)
DROP_TIP, DROP_C, DROP_R = (10, 31), (10, 38), 4


def _add(p, q, k=1):
    return (p[0] + k * q[0], p[1] + k * q[1])


def _quarter(p0, p1, centre):
    """Cubic for a 90 degree circular arc p0 -> p1 about centre."""
    c1 = (p0[0] + K * (p1[0] - centre[0]), p0[1] + K * (p1[1] - centre[1]))
    c2 = (p1[0] + K * (p0[0] - centre[0]), p1[1] + K * (p0[1] - centre[1]))
    return (c1, c2, p1)


class DrippingHoneyDipperBatch01114Redraw(Solo48):
    icon_id = "dripping-honey-dipper-batch-011-14-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("honey dipper", "honey drizzler", "honey stick")
    keywords = ("honey", "dipper", "drip", "drop", "sweet", "food", "utensil")

    def build(self) -> None:
        top = [T0, _add(T0, AXIS, BAND)]
        bottom = [_add(p, SIDE) for p in top]
        half = (SIDE[0] // 2, SIDE[1] // 2)
        low_c, up_c = _add(top[0], half), _add(top[1], half)
        low_apex = _add(low_c, AXIS, -half[0])  # radius sqrt(45) = 3 steps
        up_apex = _add(up_c, AXIS, half[0])

        self.add_line("top", top[0], top[1])
        self.add_bezier("cap-up-1", top[1], _quarter(top[1], up_apex, up_c))
        self.add_bezier("cap-up-2", up_apex, _quarter(up_apex, bottom[1], up_c))
        self.add_line("bottom", bottom[1], bottom[0])
        self.add_bezier("cap-low-1", bottom[0], _quarter(bottom[0], low_apex, low_c))
        self.add_bezier("cap-low-2", low_apex, _quarter(low_apex, top[0], low_c))
        self.add_contour(
            "head", "top", "cap-up-1", "cap-up-2", "bottom", "cap-low-1", "cap-low-2",
            closed=True,
        )

        self.add_line("groove-1", top[0], bottom[0])
        self.add_line("groove-2", top[1], bottom[1])
        self.relate("connect", "groove-1", "head")
        self.relate("connect", "groove-2", "head")

        self.add_line("handle", up_apex, HANDLE_END)
        self.relate("connect", "handle", "head")

        tx, ty = DROP_TIP
        cx, cy = DROP_C
        r = DROP_R
        right, left, base = (cx + r, cy), (cx - r, cy), (cx, cy + r)
        self.add_bezier("drop-right", DROP_TIP, ((tx + 2, ty + 2), (cx + r, cy - 3), right))
        self.add_arc("drop-base-right", right, base, radius_x=r, sweep=True)
        self.add_arc("drop-base-left", base, left, radius_x=r, sweep=True)
        self.add_bezier("drop-left", left, ((cx - r, cy - 3), (tx - 2, ty + 2), DROP_TIP))
        self.add_contour(
            "drop", "drop-right", "drop-base-right", "drop-base-left", "drop-left",
            closed=True,
        )
