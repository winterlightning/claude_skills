"""WeChat logo: two overlapping oval speech bubbles, the rear one upper-left with a
lower-left tail, the front one lower-right with a lower-right tail, the front occluding
the rear.

Plan: rear ellipse (19,18) rx13 ry12, front ellipse (31,30) rx11 ry9 on the SQUARE
centerline box (6,6)-(42,42). The two ellipses cross exactly at the integer points
J1=(32,21) and J2=(20,30); the front outline is split there and the rear outline ends there
(declared T-junction contacts). Lucide `messages-square` informed the occluded-bubble idea.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c7f3005c-d77c-49e4-8673-ec1048d8770e"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__wechat-logo/20260927T101553Z-thuan-mac-1/reference/wechat logo_c7f3005c-d77c-49e4-8673-ec1048d8770e.svg"
AUTHOR = "claude-opus-5-5"


class WechatLogo(Solo48):
    icon_id = "wechat-logo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ("wechat", "chat", "messenger", "speech-bubbles", "logo", "brand", "chinese")

    def build(self) -> None:
        j1, j2 = (32, 21), (20, 30)
        # Front bubble (closed): left point j2, top split at j1, tail lower right.
        self.add_bezier("front-upper-left", j2, ((20, 25), (26, 21), j1))
        self.add_bezier("front-right", j1, ((38, 21), (42, 25), (42, 30)), ((42, 33), (40, 35), (38, 37)))
        self.add_line("front-tail-out", (38, 37), (40, 42))
        self.add_line("front-tail-back", (40, 42), (34, 39))
        self.add_bezier("front-lower-left", (34, 39), ((27, 40), (20, 36), j2))
        self.add_contour("front", "front-upper-left", "front-right", "front-tail-out",
                         "front-tail-back", "front-lower-left", closed=True)
        # Rear bubble (visible part only): from j1 over the top and left to its tail, back to j2.
        self.add_bezier("rear-upper", j1, ((32, 12), (27, 6), (19, 6)), ((11, 6), (6, 12), (6, 18)),
                        ((6, 22), (7, 24), (9, 26)))
        self.add_line("rear-tail-out", (9, 26), (7, 34))
        self.add_line("rear-tail-back", (7, 34), (13, 29))
        self.add_bezier("rear-lower", (13, 29), ((15, 30), (18, 30), j2))
        self.add_contour("rear", "rear-upper", "rear-tail-out", "rear-tail-back", "rear-lower")
        for rear, front in (("rear-upper", "front-upper-left"), ("rear-upper", "front-right"),
                            ("rear-lower", "front-upper-left"), ("rear-lower", "front-lower-left")):
            self.relate("connect", rear, front)
