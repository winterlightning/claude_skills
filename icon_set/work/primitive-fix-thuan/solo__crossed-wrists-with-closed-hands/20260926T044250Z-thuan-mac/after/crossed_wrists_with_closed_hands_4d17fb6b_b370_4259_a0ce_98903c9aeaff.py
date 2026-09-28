"""Sign language 'love': two forearms crossed at the wrists, each ending in a closed fist.

Symbol plan: mirrored about x=24. Each fist is a rounded block (r3), 14 wide and 16 tall,
in a top corner, 8 apart from the other, with a line across its middle for the folded
fingers. Each forearm is one straight stroke from under its fist down to the opposite
side of the bottom edge; the two cross square at the wrists (24,29). Ring-shaped 12x12
fists on thin arms read as scissors and were rejected. Two-edged forearm bands were tried: their crossings left undersized holes and
each band passed within 1.5 ink of the other fist.
Lucide construction: rounded-square fists as in 'square'; straight crossing strokes.
Keyshape SQUARE: centerline x 6..42, y 6..42 (fists, band ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4d17fb6b-b370-4259-a0ce-98903c9aeaff"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__crossed-wrists-with-closed-hands/20260926T044250Z-thuan-mac/reference/sign language love_4d17fb6b-b370-4259-a0ce-98903c9aeaff.svg"
AUTHOR = "claude-opus-5-5"


class CrossedWristsWithClosedHands(Solo48):
    icon_id = "crossed-wrists-with-closed-hands"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/sign-language"
    aliases = ("sign-language-love", "asl-love", "crossed-arms-love")
    keywords = ("sign", "language", "love", "asl", "hands", "fists", "arms", "crossed", "hug", "deaf")

    def _fist(self, name, x0, y0):
        # 14 wide, 16 tall, r3 corners, with the folded fingers' line across the middle
        x1, y1, r, ym = x0 + 14, y0 + 16, 3, y0 + 8
        self.add_line(f"{name}-top", (x0 + r, y0), (x1 - r, y0))
        self.add_arc(f"{name}-tr", (x1 - r, y0), (x1, y0 + r), radius_x=r, sweep=True)
        self.add_line(f"{name}-right-a", (x1, y0 + r), (x1, ym))
        self.add_line(f"{name}-right-b", (x1, ym), (x1, y1 - r))
        self.add_arc(f"{name}-br", (x1, y1 - r), (x1 - r, y1), radius_x=r, sweep=True)
        self.add_line(f"{name}-bottom", (x1 - r, y1), (x0 + r, y1))
        self.add_arc(f"{name}-bl", (x0 + r, y1), (x0, y1 - r), radius_x=r, sweep=True)
        self.add_line(f"{name}-left-a", (x0, y1 - r), (x0, ym))
        self.add_line(f"{name}-left-b", (x0, ym), (x0, y0 + r))
        self.add_arc(f"{name}-tl", (x0, y0 + r), (x0 + r, y0), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-top", f"{name}-tr", f"{name}-right-a", f"{name}-right-b", f"{name}-br",
                         f"{name}-bottom", f"{name}-bl", f"{name}-left-a", f"{name}-left-b", f"{name}-tl",
                         closed=True)
        self.add_line(f"{name}-fingers", (x0, ym), (x1, ym))
        self.relate("connect", name, f"{name}-fingers")

    def build(self) -> None:
        self._fist("fist-left", 6, 6)
        self._fist("fist-right", 28, 6)
        # forearms: single strokes from each fist's inner-lower corner, crossing at the wrists
        self.add_polyline("arm-left", (17, 22), (24, 29), (37, 42))
        self.add_polyline("arm-right", (31, 22), (24, 29), (11, 42))
        self.relate("connect", "arm-left", "fist-left")
        self.relate("connect", "arm-right", "fist-right")
        self.relate("connect", "arm-left", "arm-right")
