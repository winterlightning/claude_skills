"""Photo brightness adjustment: a sun whose disc is half filled, ringed by eight short rays.

Symbol plan: concentric about (24,24). The disc is an r8 circle split by its vertical
diameter into two half discs (the outline form of the half-filled brightness disc; a
stroke-filled half failed the hole/pinch gate). Eight detached rays start 8 beyond the rim: the four cardinal rays run r16..20,
the diagonals from (12,12) to (14,14) off centre.
Lucide construction: 'sun' - circle with eight detached rays; 'contrast' - half-filled
circle for the brightness state.
Keyshape CIRCLE: ray tips reach centerline radius 20 about (24,24).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "1f15b907-4008-5d37-802a-a4bd5dab0293"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__brightness-half-disc-sun/20260926T030905Z-thuan-mac/reference/photo adjust brightness_1f15b907-4008-5d37-802a-a4bd5dab0293.svg"
AUTHOR = "claude-opus-5-5"


class BrightnessHalfDiscSun(Solo48):
    icon_id = "brightness-half-disc-sun"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/editing"
    aliases = ("photo-adjust-brightness", "brightness", "contrast-sun")
    keywords = ("brightness", "sun", "light", "exposure", "adjust", "photo", "edit", "contrast", "display")

    def build(self) -> None:
        c, r = 24, 8
        top, bottom = (c, c - r), (c, c + r)
        self.add_arc("disc-right", top, bottom, radius_x=r, sweep=True)
        self.add_arc("disc-left", bottom, top, radius_x=r, sweep=True)
        self.add_contour("disc", "disc-right", "disc-left", closed=True)
        self.add_line("disc-diameter", top, bottom)
        self.relate("connect", "disc", "disc-diameter")
        for name, a, b in (("n", (0, -16), (0, -20)), ("s", (0, 16), (0, 20)),
                           ("e", (16, 0), (20, 0)), ("w", (-16, 0), (-20, 0)),
                           ("ne", (12, -12), (14, -14)), ("se", (12, 12), (14, 14)),
                           ("sw", (-12, 12), (-14, 14)), ("nw", (-12, -12), (-14, -14))):
            self.add_line(f"ray-{name}", (c + a[0], c + a[1]), (c + b[0], c + b[1]))
