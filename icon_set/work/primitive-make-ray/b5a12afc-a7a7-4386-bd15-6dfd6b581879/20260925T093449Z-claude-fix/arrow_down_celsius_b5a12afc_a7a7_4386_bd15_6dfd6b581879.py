"""Arrow pointing down onto a floor line: the temperature falls to its low mark.

Symbol plan: one vertical shaft on the x=24 axis, a mirrored 45-degree chevron head
whose tip shares the shaft end, and a detached floor line one clear gap below.
Lucide construction: arrow-down-to-line (shaft + chevron + separate base bar).
Keyshape VRECT_L: centerline x 8..40 (floor line), y 4..44 (shaft top, floor line).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b5a12afc-a7a7-4386-bd15-6dfd6b581879"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__arrow-down-celsius/20260925T093141Z-thuan-mac/reference/arrow down celsius_b5a12afc-a7a7-4386-bd15-6dfd6b581879.svg"
AUTHOR = "claude-opus-5-5"


class ArrowDownCelsius(Solo48):
    icon_id = "arrow-down-celsius"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "state"
    aliases = ("temperature-down", "arrow-down-to-line")
    keywords = ("arrow", "down", "celsius", "temperature", "decrease", "minimum", "state")

    def build(self) -> None:
        axis, tip, wing = 24, 34, 12
        self.add_line("shaft", (axis, 4), (axis, tip))
        self.add_polyline("head", (axis - wing, tip - wing), (axis, tip), (axis + wing, tip - wing))
        self.relate("connect", "shaft", "head")
        self.add_line("floor", (8, 44), (40, 44))
