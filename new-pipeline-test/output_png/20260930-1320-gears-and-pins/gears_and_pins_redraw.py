"""gears-and-pins (redraw of the new-pipeline traced SVG).

Plan: two equal six-tooth gears on the falling diagonal and two equal T pins
in the other two corners, on SQUARE (centerline box (6,6)-(42,42)), the
keyshape the metrics suggested (score 1.24, square hint).
- gear: one tooth definition (a quarter from the top tip to the side valley),
  mirrored on both axes into a closed 18-point outline, top tooth pointing up
  as in the generated image: V valleys on radius ~6, top/bottom tips flat and
  4 wide on radius 9, the four side teeth tapered to a 2.8 tip (7,5)-(9,3).
  The taper is deliberate: a side tooth whose flanks converge by less than
  30 degrees is a near-parallel internal-spacing finding in the build gate
  (flanks ~4.5 apart on centerlines), and narrower tips (tried: 1-2 wide on
  every tooth) turn the outline into a six-point star.
- upper-left gear centre (15,15): top tip on y 6, left tips on x 6.
- lower-right gear centre (33,33): bottom tip on y 42, right tips on x 42.
- pin: one T definition, head 10 wide, shaft 10 long, drawn as one polyline
  (head left end -> head centre -> shaft foot, plus the head's right half).
  Upper-right pin head on y 6 (x 31-41, shaft x 36); lower-left pin head on
  y 32 (x 6-16, shaft x 11 down to y 42) -- the same pin moved by (-25, 26).
The gear outline is the gear: its white interior (~7.7 wide) stands for the
large centre hole of the image.
Lucide construction: `cog` (evenly spaced teeth around one centre); its
ring-plus-hub build cannot hold 8-unit gaps at this size.

Metric issues (gears-and-pins_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (y filled 99%): the gears reach all four SQUARE sides
  exactly (top/left upper gear, bottom/right lower gear).
- clearance e0/e1, e0/e3, e0/e5, e1/e3, e3/e5 (gears vs pins and gear vs
  gear, 3.2-7.0): every distinct pair now keeps >= 8 on centerlines --
  gear/gear 8.94, upper gear/upper pin 9.22, upper gear/lower pin 8.0 (the
  straight tip y 24 against the head y 32), lower gear/upper pin 8.06,
  lower gear/lower pin 8.25.
- clearance e0/e2, e3/e4 (hub rings 3.2-3.5 from their own gear outline):
  not fixable with a ring -- a 6-wide hub hole plus 8 of clearance needs a
  valley radius of 13 (tip ~16), and two such gears cannot sit apart in a
  36 box. The hub rings are dropped; each gear outline's own interior
  (~7.7 wide) is the hole.
- hole x14 (tooth pinches 1.3-1.4 wide, hubs 4.2 wide): the pinches came
  from the thin trace hugging each tooth; each gear is now one stroke whose
  interior is one open region ~7.7 wide (>= 6). No other enclosed holes.
Not reproduced: the separate hub rings (see above).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6441c71e-2430-439c-b9ba-705297d8ec05"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1320-gears-and-pins/gears-and-pins_raw.svg"
AUTHOR = "claude-opus-5-5"

# Quarter outline relative to the gear centre: top tip corner, valley, the
# upper-right tooth's two tip corners, right valley. Mirrored on x and y.
GEAR_QUARTER = ((2, -9), (3, -5), (7, -5), (9, -3), (6, 0))
GEAR_CENTRES = ((15, 15), (33, 33))
PIN_HALF_HEAD = 5
PIN_SHAFT = 10
PIN_TOPS = ((36, 6), (11, 32))   # head centre of each pin


def gear_ring(quarter, centre):
    """Closed tooth outline, clockwise from the top tip's right corner."""
    half = list(quarter) + [(x, -y) for x, y in reversed(quarter) if y != 0]
    ring = half + [(-x, y) for x, y in reversed(half)]
    cx, cy = centre
    return [(cx + x, cy + y) for x, y in ring]


class GearsAndPinsRedraw(Solo48):
    icon_id = "gears-and-pins-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("gears and pins", "cogs and pins", "mechanical parts")
    keywords = ("gear", "cog", "pin", "mechanism", "machinery", "engineering", "parts", "hardware")

    def build(self) -> None:
        for name, centre in zip(("gear-upper", "gear-lower"), GEAR_CENTRES):
            self.add_polyline(name, *gear_ring(GEAR_QUARTER, centre), closed=True)

        for name, (px, py) in zip(("pin-upper", "pin-lower"), PIN_TOPS):
            self.add_polyline(
                f"{name}-left", (px - PIN_HALF_HEAD, py), (px, py), (px, py + PIN_SHAFT)
            )
            self.add_line(f"{name}-right", (px, py), (px + PIN_HALF_HEAD, py))
            self.relate("connect", f"{name}-left", f"{name}-right")
