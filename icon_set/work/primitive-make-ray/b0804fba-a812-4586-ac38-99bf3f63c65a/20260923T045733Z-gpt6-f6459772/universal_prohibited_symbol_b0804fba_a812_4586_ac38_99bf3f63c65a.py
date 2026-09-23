from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "b0804fba-a812-4586-ac38-99bf3f63c65a"
SOURCE_PATH = "pictographic-primitives/_uncategorized_20/gatsby logo_b0804fba-a812-4586-ac38-99bf3f63c65a.svg"
AUTHOR = "gpt-6"

class UniversalProhibitedSymbol(Solo48):
    icon_id = "universal-prohibited-symbol"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/status"
    aliases = ("no symbol", "ban")
    keywords = ("prohibited", "forbidden", "slash")

    def build(self) -> None:
        # Radius-20 circular boundary; slash endpoints use the 12-16-20 integer triangle.
        self.add_arc("ring-top", (4, 24), (44, 24), radius_x=20, sweep=True)
        self.add_arc("ring-bottom", (44, 24), (4, 24), radius_x=20, sweep=True)
        self.add_contour("ring", "ring-top", "ring-bottom", closed=True)
        self.add_line("slash", (8, 12), (40, 36))
        self.relate("connect", "ring", "slash")
