"""Two objects moving upward to a shared top alignment rail."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c7665d4b-d589-4003-8834-958ea7cbf3a9"
SOURCE_PATH = "icon_set/work/todo-references/align top move_c7665d4b-d589-4003-8834-958ea7cbf3a9.svg"
AUTHOR = "gpt-6"


class AlignTopMove(Solo48):
    icon_id = "align-top-move"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "actions/alignment"
    aliases = ("move-to-top",)
    keywords = ("align", "top", "move", "objects", "arrows")

    def build(self) -> None:
        # One rail; paired arrows and upright objects use shared positions.
        self.add_line("alignment-rail", (4, 8), (44, 8))
        for name, cx, left, right in (("left", 14, 8, 20), ("right", 34, 28, 40)):
            self.add_polyline(f"{name}-arrow", (cx-4, 20), (cx, 16), (cx+4, 20))
            self.add_line(f"{name}-shaft", (cx, 16), (cx, 22))
            self.relate("connect", f"{name}-arrow", f"{name}-shaft")
            self.add_polyline(f"{name}-object", (left, 40), (left, 30), (right, 30), (right, 40))
