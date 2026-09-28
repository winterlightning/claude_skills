"""A love candle: a heart-shaped flame on a wick over a round-shouldered candle standing on a saucer.

Symbol plan: symmetric about x=24. The heart is one closed outline: two r4 lobes meeting
at a notch, each flowing tangentially (vertical at the widest point) into a bezier side
down to the tip. The wick drops from the tip to the candle top (shared endpoints). The
candle is an open outline (r3 top corners) standing on the saucer's rim. The saucer is a
closed tapered dish, 8 deep. The reference's wax drip line inside the candle is dropped:
the candle body is 11 tall, so no line fits 8 from both its top and its base.
Lucide construction: 'heart' lobes and tip; 'flame'/'candle' style body on a dish.
Keyshape VRECT_L: centerline x 8..40 (saucer rim), y 4..44 (heart lobes, saucer base).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "38fd3f15-701d-4404-8da0-af7c79ef4dd2"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__candle-with-heart-flame/20260926T034135Z-thuan-mac/reference/love candle_38fd3f15-701d-4404-8da0-af7c79ef4dd2.svg"
AUTHOR = "claude-opus-5-5"


class CandleWithHeartFlame(Solo48):
    icon_id = "candle-with-heart-flame"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/home"
    aliases = ("love candle", "romantic candle")
    keywords = ("candle", "heart", "love", "romance", "valentine", "flame", "memorial", "candlelight")

    def build(self) -> None:
        ax = 24
        lobe_r, lobe_y, tip_y = 4, 8, 17
        top, rim, base, cr = 25, 36, 44, 3
        cl, crt = 18, 30  # candle walls

        def m(x):
            return 2 * ax - x

        # heart
        self.add_arc("lobe-l", (ax, lobe_y), (ax - 2 * lobe_r, lobe_y), radius_x=lobe_r, sweep=False)
        self.add_bezier("side-l", (ax - 2 * lobe_r, lobe_y),
                        ((ax - 2 * lobe_r, lobe_y + 4), (ax - 4, tip_y - 4), (ax, tip_y)))
        self.add_bezier("side-r", (ax, tip_y),
                        ((ax + 4, tip_y - 4), (m(ax - 2 * lobe_r), lobe_y + 4), (m(ax - 2 * lobe_r), lobe_y)))
        self.add_arc("lobe-r", (m(ax - 2 * lobe_r), lobe_y), (ax, lobe_y), radius_x=lobe_r, sweep=False)
        self.add_contour("heart", "lobe-l", "side-l", "side-r", "lobe-r", closed=True)
        # wick
        self.add_line("wick", (ax, tip_y), (ax, top))
        self.relate("connect", "heart", "wick")
        # candle
        self.add_line("candle-wall-l", (cl, rim), (cl, top + cr))
        self.add_arc("candle-corner-l", (cl, top + cr), (cl + cr, top), radius_x=cr)
        self.add_line("candle-top-l", (cl + cr, top), (ax, top))
        self.add_line("candle-top-r", (ax, top), (crt - cr, top))
        self.add_arc("candle-corner-r", (crt - cr, top), (crt, top + cr), radius_x=cr)
        self.add_line("candle-wall-r", (crt, top + cr), (crt, rim))
        self.add_contour("candle", "candle-wall-l", "candle-corner-l", "candle-top-l", "candle-top-r",
                         "candle-corner-r", "candle-wall-r")
        self.relate("connect", "wick", "candle")
        # saucer
        self.add_line("rim-l", (8, rim), (cl, rim))
        self.add_line("rim-m", (cl, rim), (crt, rim))
        self.add_line("rim-r", (crt, rim), (40, rim))
        self.add_bezier("dish-r", (40, rim), ((40, 41), (38, base), (34, base)))
        self.add_line("dish-base", (34, base), (14, base))
        self.add_bezier("dish-l", (14, base), ((10, base), (8, 41), (8, rim)))
        self.add_contour("saucer", "rim-l", "rim-m", "rim-r", "dish-r", "dish-base", "dish-l", closed=True)
        self.relate("connect", "candle", "saucer")
