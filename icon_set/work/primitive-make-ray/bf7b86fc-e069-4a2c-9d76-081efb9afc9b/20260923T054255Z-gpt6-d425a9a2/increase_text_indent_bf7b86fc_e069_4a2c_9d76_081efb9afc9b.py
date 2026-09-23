from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "bf7b86fc-e069-4a2c-9d76-081efb9afc9b"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/indent increase_bf7b86fc-e069-4a2c-9d76-081efb9afc9b.svg"
AUTHOR = "gpt-6"

class IncreaseTextIndent(Solo48):
    icon_id = "increase-text-indent"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/text"
    aliases = ("indent right",)
    keywords = ("lines", "paragraph", "triangle")

    def build(self) -> None:
        # Six equally spaced text rules; a hollow triangle points right beside them.
        for y in (4, 12, 20, 28, 36, 44):
            end = 28 if y in (4, 44) else 22
            self.add_line(f"text-{y}", (8, y), (end, y))
        self.add_polyline("indent-arrow", (30, 16), (40, 24), (30, 32), (30, 16), closed=True)
