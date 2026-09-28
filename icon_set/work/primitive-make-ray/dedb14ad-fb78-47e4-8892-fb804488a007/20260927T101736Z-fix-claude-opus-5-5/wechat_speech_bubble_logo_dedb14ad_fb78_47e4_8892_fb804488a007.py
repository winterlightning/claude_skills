"""WeChat single speech bubble: a round oval bubble with a lower-left tail and two
left-aligned text lines (long over short).

Plan: one ellipse-like bubble about (24,21), rx 18 / ry 15 on the SQUARE centerline box
(6,6)-(42,42); the tail tip reaches the bottom extreme (10,42). Text lines share the left
edge x=16 like the reference. Lucide `message-circle` informed the bubble + tail join.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "dedb14ad-fb78-47e4-8892-fb804488a007"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__wechat-speech-bubble-logo/20260927T101553Z-thuan-mac-1/reference/wechat logo_dedb14ad-fb78-47e4-8892-fb804488a007.svg"
AUTHOR = "claude-opus-5-5"


class WechatSpeechBubbleLogo(Solo48):
    icon_id = "wechat-speech-bubble-logo"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ("wechat", "chat", "message", "speech-bubble", "logo", "brand", "text")

    def build(self) -> None:
        cx, cy, rx, ry = 24, 21, 18, 15
        kx, ky = 10, 8  # quarter-ellipse handle lengths (kappa ~0.55)
        self.add_bezier(
            "bubble",
            (12, 32),
            ((8, 29), (cx - rx, cy + 5), (cx - rx, cy)),
            ((cx - rx, cy - ky), (cx - kx, cy - ry), (cx, cy - ry)),
            ((cx + kx, cy - ry), (cx + rx, cy - ky), (cx + rx, cy)),
            ((cx + rx, cy + ky), (cx + kx, cy + ry), (cx, cy + ry)),
            ((22, 36), (20, 36), (18, 35)),
        )
        self.add_line("tail-out", (18, 35), (10, 42))
        self.add_line("tail-back", (10, 42), (12, 32))
        self.add_contour("bubble-outline", "bubble", "tail-out", "tail-back", closed=True)
        left = 17
        self.add_line("text-long", (left, 17), (31, 17))
        self.add_line("text-short", (left, 25), (26, 25))
