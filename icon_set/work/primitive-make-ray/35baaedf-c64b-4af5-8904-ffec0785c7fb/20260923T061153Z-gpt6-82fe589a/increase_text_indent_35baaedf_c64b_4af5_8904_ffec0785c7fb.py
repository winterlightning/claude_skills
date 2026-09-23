"""Three equal text lines above a long right arrow.

Symbol plan: repeated horizontal line definition, then a shaft and symmetric
open chevron sharing its right tip. SQUARE extremes are x/y 6..42.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "35baaedf-c64b-4af5-8904-ffec0785c7fb"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/insert image bottom_35baaedf-c64b-4af5-8904-ffec0785c7fb.svg"
AUTHOR = "gpt-6"


class IncreaseTextIndent(Solo48):
    icon_id = "increase-text-indent"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/text"
    aliases = ("text lines arrow right", "insert below")
    keywords = ("text", "lines", "arrow", "right", "indent")

    def build(self) -> None:
        for index, y in enumerate((6, 14, 22), 1):
            self.add_line(f"text-line-{index}", (6, y), (36, y))
        self.add_line("arrow-shaft", (6, 36), (42, 36))
        self.add_polyline("arrow-head", (36, 30), (42, 36), (36, 42))
        self.relate("connect", "arrow-shaft", "arrow-head")
