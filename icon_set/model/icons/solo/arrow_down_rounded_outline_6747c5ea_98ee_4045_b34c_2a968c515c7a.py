"""Outlined downward arrow. VRECT_L fits tall direction; mirror outline about x=24.
Reference contributes closed broad arrow; Lucide arrow-down contributes balanced diagonal arms.
Omit fine rounding on the diagonal tips to retain measurable openings."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "6747c5ea-98ee-4045-b34c-2a968c515c7a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_10/caret down_6747c5ea-98ee-4045-b34c-2a968c515c7a.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "arrow-down-rounded-outline"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Downward Pointing Arrow"]
    keywords = ["arrow", "down", "direction", "outlined", "rounded", "symbol", "navigation"]
    def build(self):
        self.add_polyline("outline", (18,4),(30,4),(30,24),(38,16),(40,28),(24,44),(8,28),(10,16),(18,24),closed=True)
