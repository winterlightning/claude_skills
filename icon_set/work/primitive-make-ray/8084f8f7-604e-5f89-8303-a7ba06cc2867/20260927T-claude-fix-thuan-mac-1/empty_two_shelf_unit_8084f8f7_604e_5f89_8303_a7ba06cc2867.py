"""Empty two-shelf unit: an open shelving unit -- two tall posts carrying two
shelves, the posts running on above the top shelf and below the
bottom one.

Revision (disapproved, reason not recorded): the rejected drawing stacked five
evenly spaced rungs between the posts, so it read as a ladder; the original has
exactly two shelves, each a thick board drawn with a top and bottom edge, and
open space above, between and below them. The two boards are restored.

Symbol plan: mirror axis x=24. Posts: x=8 and x=40 from y=4 to y=44. Shelves: two
boards across the posts at y=15 and y=31, leaving a 16-high bay between them and
the posts running 11 above the top shelf and 13 below the bottom one, the
reference's proportions.
Omissions: each board's second edge. A closed board needs 10 units of height,
which makes four evenly spaced lines that read as a ladder again
(attempts/thick-boards.*); single-stroke shelves keep the two open bays.
Lucide construction: 'library' / 'bookshelf' posts and boards.
Keyshape VRECT_L: centerline (8,4)-(40,44).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8084f8f7-604e-5f89-8303-a7ba06cc2867"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__empty-two-shelf-unit/20260926T182653Z-thuan-mac-1/reference/office shelf_8084f8f7-604e-5f89-8303-a7ba06cc2867.svg"
AUTHOR = "claude-opus-5-5"

EDGES = (15, 31)


class EmptyTwoShelfUnit(Solo48):
    icon_id = "empty-two-shelf-unit"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furniture"
    aliases = ("office-shelf", "shelving-unit")
    keywords = ("shelf", "shelves", "shelving", "office", "storage", "furniture", "empty")

    def build(self) -> None:
        stops = (4,) + EDGES + (44,)
        for side, x in (("left", 8), ("right", 40)):
            names = []
            for a, b in zip(stops, stops[1:]):
                self.add_line(f"post-{side}-{a}", (x, a), (x, b))
                names.append(f"post-{side}-{a}")
            self.add_contour(f"post-{side}", *names)
        for y in EDGES:
            self.add_line(f"board-{y}", (8, y), (40, y))
            self.relate("connect", f"board-{y}", "post-left")
            self.relate("connect", f"board-{y}", "post-right")
