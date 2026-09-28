"""Auto column width: a double-headed width arrow over two split columns.

Symbol plan: two identical column cards (a rectangle with a middle divider)
mirrored about x=24 with the 8-unit gap between them; a double-headed
horizontal arrow above, heads mirrored. Vertical budget on SQUARE (36):
arrow head half-height 4, 8 gap, card height 20 split into two 10-high cells.
Lucide: `move-horizontal` (shaft plus two chevron heads) and `columns-2`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "64ed5636-8e1f-4fbd-8a7a-ba14ed99b301"
SOURCE_PATH = "icon_set/work/todo-references/auto setting column width_64ed5636-8e1f-4fbd-8a7a-ba14ed99b301.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 6, 42, 6, 42
HEAD = 4                  # arrowhead half height and depth
ARROW_Y = TOP + HEAD
CARD_TOP = ARROW_Y + HEAD + 8
DIVIDER = (CARD_TOP + BOTTOM) // 2
CARD_W = (RIGHT - LEFT - 8) // 2


class AutoColumnWidth(Solo48):
    icon_id = "auto-column-width"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface/layout"
    aliases = ("autofit column width", "fit columns", "column width")
    keywords = ("column", "width", "auto", "fit", "resize", "table", "layout")

    def build(self) -> None:
        a0, a1 = LEFT + 2, RIGHT - 2
        self.add_line("shaft", (a0, ARROW_Y), (a1, ARROW_Y))
        self.add_polyline("head-left", (a0 + HEAD, ARROW_Y - HEAD), (a0, ARROW_Y), (a0 + HEAD, ARROW_Y + HEAD))
        self.add_polyline("head-right", (a1 - HEAD, ARROW_Y - HEAD), (a1, ARROW_Y), (a1 - HEAD, ARROW_Y + HEAD))
        self.relate("connect", "shaft", "head-left-1", "head-left-2")
        self.relate("connect", "shaft", "head-right-1", "head-right-2")

        for side, x0 in (("left", LEFT), ("right", RIGHT - CARD_W)):
            x1 = x0 + CARD_W
            self.add_polyline(
                f"card-{side}",
                (x0, CARD_TOP), (x1, CARD_TOP), (x1, DIVIDER), (x1, BOTTOM),
                (x0, BOTTOM), (x0, DIVIDER), closed=True,
            )
            self.add_line(f"divider-{side}", (x0, DIVIDER), (x1, DIVIDER))
            self.relate("connect", f"divider-{side}", f"card-{side}-2", f"card-{side}-3")
            self.relate("connect", f"divider-{side}", f"card-{side}-5", f"card-{side}-6")
