"""Vertical spacing between two aligned horizontal objects."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f31f1d33-4050-4371-af56-548e54cec150"
SOURCE_PATH = "icon_set/work/todo-references/align top bottom_f31f1d33-4050-4371-af56-548e54cec150.svg"
AUTHOR = "gpt-6"


class AlignTopBottom(Solo48):
    icon_id = "align-top-bottom"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/alignment"
    aliases = ("vertical-spacing",)
    keywords = ("align", "top", "bottom", "move", "distribute")

    def build(self) -> None:
        # Two wide objects reduced to rails; a mirrored arrow shows the gap.
        self.add_line("top-object", (6, 6), (42, 6))
        self.add_line("bottom-object", (6, 42), (42, 42))
        self.add_line("arrow-shaft", (24, 16), (24, 32))
        self.add_polyline("arrow-up", (18, 22), (24, 16), (30, 22))
        self.add_polyline("arrow-down", (18, 26), (24, 32), (30, 26))
        self.relate("connect", "arrow-shaft", "arrow-up")
        self.relate("connect", "arrow-shaft", "arrow-down")
