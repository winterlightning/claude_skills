"""A broadcast van: a box van with a sloped front and two wheels, carrying a tilted satellite dish on a mast.

Symbol plan: the van body is one closed outline - flat roof, 45-degree windscreen, short
front, a bottom line split for the wheels, rounded rear corners. Each wheel is a large
arc (r5) hanging from the bottom line at shared endpoints, so the body's bottom edge
reads as the wheel arch. The dish is a half disc on a 45-degree chord (10,10): two cubic
quarter circles (radius 5*sqrt2 about the chord centre) meeting at the integer bowl apex
straight below the chord's upper end, so it faces up and right. A feed arm leaves the
chord centre along the axis; the mast drops from the chord's lower end to the roof
(shared endpoints), with the bowl's lowest point about 9 above the roof.
Lucide construction: 'satellite-dish' (half-disc bowl with a feed arm) on a 'truck'-like
box body.
Keyshape VRECT_L: centerline x 8..40 (front, rear), y 4..44 (chord top, wheel bottoms).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "493ede0a-6fdc-424e-ac62-2775797bcb36"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__broadcast-van-dish/20260926T034135Z-thuan-mac/reference/radio van_493ede0a-6fdc-424e-ac62-2775797bcb36.svg"
AUTHOR = "claude-opus-5-5"


class BroadcastVanDish(Solo48):
    icon_id = "broadcast-van-dish"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/road"
    aliases = ("radio van", "broadcast van", "satellite truck", "news van")
    keywords = ("van", "broadcast", "satellite", "dish", "radio", "news", "tv", "outside broadcast", "vehicle")

    def build(self) -> None:
        front, rear, roof, bottom, rr = 8, 40, 25, 36, 3
        w1, w2, wr = 15, 33, 5  # wheel centres; chord ends at x +-4 on the bottom line
        a, b = (11, 4), (21, 14)  # dish chord, 45 degrees
        mid = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)
        mast_x = b[0]
        # van body
        self.add_line("roof-front", (13, roof), (mast_x, roof))
        self.add_line("roof-rear", (mast_x, roof), (rear - rr, roof))
        self.add_arc("corner-rt", (rear - rr, roof), (rear, roof + rr), radius_x=rr)
        self.add_line("rear-wall", (rear, roof + rr), (rear, bottom - rr))
        self.add_arc("corner-rb", (rear, bottom - rr), (rear - rr, bottom), radius_x=rr)
        self.add_line("bottom-rear", (rear - rr, bottom), (w2 + 4, bottom))
        self.add_line("bottom-w2", (w2 + 4, bottom), (w2 - 4, bottom))
        self.add_line("bottom-mid", (w2 - 4, bottom), (w1 + 4, bottom))
        self.add_line("bottom-w1", (w1 + 4, bottom), (w1 - 4, bottom))
        self.add_line("bottom-front", (w1 - 4, bottom), (front, bottom))
        self.add_line("front-wall", (front, bottom), (front, 30))
        self.add_line("windscreen", (front, 30), (13, roof))
        self.add_contour("body", "roof-front", "roof-rear", "corner-rt", "rear-wall", "corner-rb",
                         "bottom-rear", "bottom-w2", "bottom-mid", "bottom-w1", "bottom-front",
                         "front-wall", "windscreen", closed=True)
        # wheels
        for name, wx in (("wheel-front", w1), ("wheel-rear", w2)):
            self.add_arc(name, (wx - 4, bottom), (wx + 4, bottom), radius_x=wr, large_arc=True, sweep=False)
            self.relate("connect", "body", name)
        # dish
        self.add_line("chord-upper", a, mid)
        self.add_line("chord-lower", mid, b)
        apex = (a[0], b[1])
        k = 0.5523 * 5  # cubic quarter-circle handle for radius 5*sqrt2, per axis
        self.add_bezier("bowl", b, ((b[0] - k, b[1] + k), (apex[0] + k, apex[1] + k), apex),
                        ((apex[0] - k, apex[1] - k), (a[0] - k, a[1] + k), a))
        self.add_contour("dish", "chord-upper", "chord-lower", "bowl", closed=True)
        self.add_line("feed", mid, (mid[0] + 5, mid[1] - 5))
        self.add_line("mast", b, (mast_x, roof))
        self.relate("connect", "dish", "feed")
        self.relate("connect", "dish", "mast")
        self.relate("connect", "mast", "body")
