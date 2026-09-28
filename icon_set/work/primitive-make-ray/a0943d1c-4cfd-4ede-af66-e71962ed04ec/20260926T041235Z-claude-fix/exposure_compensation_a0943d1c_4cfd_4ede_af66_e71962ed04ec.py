"""Exposure compensation (light mode exposure): a minus and a plus on either side of a
diagonal slash.

Symbol plan: point-symmetric about (24,24). The slash runs corner to corner from (6,42)
to (42,6). The minus (10 long) is centred (13,13) in the upper-left half and the plus
(arms of 5) is centred (35,35) in the lower-right half, each 12+ clear of the slash.
The reference's rounded-square frame is dropped: with the frame, each half leaves room
for a symbol only about 2.5 units in radius after the 8-unit clearances, which is what
made the rejected plus a blob.
Lucide construction: 'diff'/'plus-minus' - straight plus and minus strokes; the slash as
in 'slash'.
Keyshape SQUARE: centerline x 6..42, y 6..42 (slash ends).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a0943d1c-4cfd-4ede-af66-e71962ed04ec"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__exposure-compensation/20260926T035939Z-thuan-mac/reference/light mode exposure 1_a0943d1c-4cfd-4ede-af66-e71962ed04ec.svg"
AUTHOR = "claude-opus-5-5"


class ExposureCompensation(Solo48):
    icon_id = "exposure-compensation"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "photography/settings"
    aliases = ("light-mode-exposure", "exposure", "exposure-plus-minus")
    keywords = ("exposure", "compensation", "plus", "minus", "brightness", "camera", "ev", "photo", "adjust")

    def build(self) -> None:
        self.add_line("slash", (6, 42), (42, 6))
        self.add_line("minus", (8, 13), (18, 13))
        self.add_line("plus-horizontal", (30, 35), (40, 35))
        self.add_line("plus-vertical", (35, 30), (35, 40))
        self.relate("connect", "plus-horizontal", "plus-vertical")
