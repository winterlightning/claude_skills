"""ice-cream-pushcart-umbrella (redraw of the new-pipeline traced SVG).

Plan: street ice cream pushcart: a closed domed parasol on one central pole,
a rectangular cart box, a bent push handle on the right and two ring wheels
hanging tangent under the box, on VRECT_L (centerline box (8,4)-(40,44)).
The trace fits SQUARE, but the vertical stack cannot fit 36 on the grid:
canopy 11 (hole >= 6) + pole gap 8 + box 11 (hole >= 6) + wheel diameter 10
= 40. VRECT_L gives exactly that height; the width (32) still holds the box,
the handle and two r5 wheels 18 apart (8 clear between them).
- canopy: half-ellipse rx 14 ry 11 about (22,15), top y=4 on the box edge,
  closed by a flat base line y=15 from x=8 to x=36.
- pole: x=22 from the canopy base to the box top, connected at both ends.
- box: closed rectangle (8,23)-(36,34) on the same axis; the bottom edge is
  split at the wheel tops x=13 and x=31 so each wheel shares its apex with
  the box. Canopy, box and wheels mirror about x=22; only the handle is
  asymmetric, as the subject is.
- wheels: 4-arc r5 rings about (13,39) and (31,39), bottom y=44.
- handle: one 45 degree grip from the box right wall (36,30) up to (40,26),
  the right extreme of the box. 45 degrees keeps it out of the wall's
  30 degree parallel band (a 1:2 grip failed the build gate's internal
  spacing against the wall above the joint). A variant with a box 8..34 and
  an elbowed handle passed too, but its right wheel overhung the box by 2;
  the centred wheels read better at 48 px.
No useful Lucide match (Lucide has no pushcart); the canopy follows Lucide
umbrella's dome-plus-pole reading, the wheels Lucide shopping-cart's rings.

Metric issues:
- clearance e1/e4 and e2/e4 (wheels 0.57/0.54 from the box): fixed; each
  wheel apex is a shared, declared contact point on the split box bottom,
  and the rest of the ring falls away from the box.
- hole 5.0 (box interior): fixed; the box is 11 high, a 7-unit hole.
- holes 1.46 / 1.56 (wheel rings): fixed; r5 rings leave 6-wide holes.
- stroke-width (trace 2.4): redrawn at stroke 4 with every gap re-measured.
- keyshape SQUARE (suggested): not used; the stack above needs 40 in
  height, so VRECT_L replaces it (reported, not a metric issue).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7c387930-dc52-4c49-b9d9-34b20fc71ad1"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1529-ice-cream-pushcart-umbrella/"
    "ice-cream-pushcart-umbrella_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 22                      # pole, canopy and box centre
CANOPY_TOP, CANOPY_BASE = 4, 15
CANOPY_RX = 14                 # canopy x 8..36
BOX_L, BOX_R = 8, 36
BOX_TOP, BOX_BOTTOM = 23, 34   # CANOPY_BASE + 8, BOX_TOP + 11
WHEEL_R = 5
WHEELS = (13, 31)              # 18 apart: 8 clear between the rings
WHEEL_CY = BOX_BOTTOM + WHEEL_R
HANDLE = ((BOX_R, 30), (40, 26))


class IceCreamPushcartUmbrellaRedraw(Solo48):
    icon_id = "ice-cream-pushcart-umbrella-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/vendor"
    aliases = ("ice cream cart", "vendor cart", "street food cart")
    keywords = ("ice cream", "cart", "pushcart", "umbrella", "parasol", "vendor", "street food", "kiosk")

    def build(self) -> None:
        left, right = AXIS - CANOPY_RX, AXIS + CANOPY_RX
        ry = CANOPY_BASE - CANOPY_TOP
        self.add_arc("canopy-dome-1", (left, CANOPY_BASE), (AXIS, CANOPY_TOP),
                     radius_x=CANOPY_RX, radius_y=ry, sweep=True)
        self.add_arc("canopy-dome-2", (AXIS, CANOPY_TOP), (right, CANOPY_BASE),
                     radius_x=CANOPY_RX, radius_y=ry, sweep=True)
        self.add_line("canopy-base-r", (right, CANOPY_BASE), (AXIS, CANOPY_BASE))
        self.add_line("canopy-base-l", (AXIS, CANOPY_BASE), (left, CANOPY_BASE))
        self.add_contour("canopy", "canopy-dome-1", "canopy-dome-2",
                         "canopy-base-r", "canopy-base-l", closed=True)

        self.add_line("pole", (AXIS, CANOPY_BASE), (AXIS, BOX_TOP))

        w1, w2 = WHEELS
        hx, hy = HANDLE[0]
        self.add_polyline(
            "box",
            (BOX_L, BOX_TOP), (AXIS, BOX_TOP), (BOX_R, BOX_TOP), (hx, hy),
            (BOX_R, BOX_BOTTOM), (w2, BOX_BOTTOM), (w1, BOX_BOTTOM),
            (BOX_L, BOX_BOTTOM),
            closed=True,
        )
        self.relate("connect", "pole", "canopy-base-r")
        self.relate("connect", "pole", "canopy-base-l")
        self.relate("connect", "pole", "box-1")
        self.relate("connect", "pole", "box-2")

        for index, cx in enumerate(WHEELS, start=1):
            top, r = (cx, BOX_BOTTOM), WHEEL_R
            wid = f"wheel-{index}"
            self.add_arc(f"{wid}-1", top, (cx + r, WHEEL_CY), radius_x=r, sweep=True)
            self.add_arc(f"{wid}-2", (cx + r, WHEEL_CY), (cx, WHEEL_CY + r), radius_x=r, sweep=True)
            self.add_arc(f"{wid}-3", (cx, WHEEL_CY + r), (cx - r, WHEEL_CY), radius_x=r, sweep=True)
            self.add_arc(f"{wid}-4", (cx - r, WHEEL_CY), top, radius_x=r, sweep=True)
            self.add_contour(wid, f"{wid}-1", f"{wid}-2", f"{wid}-3", f"{wid}-4", closed=True)
        self.relate("connect", "wheel-1-1", "box-6")
        self.relate("connect", "wheel-1-4", "box-7")
        self.relate("connect", "wheel-2-1", "box-5")
        self.relate("connect", "wheel-2-4", "box-6")

        self.add_polyline("handle", *HANDLE)
        self.relate("connect", "handle", "box-3")
        self.relate("connect", "handle", "box-4")
