"""Bacteria magnifying glass: a lens with a handle, showing scattered bacteria dots.

Symbol plan: lens circle radius 15 touching the SQUARE's top-left; the handle
leaves the lens at the integer 3-4-5 point (12, 9) from its centre and ends in
the bottom-right corner (a 16-degree lean from radial is the price of integer
contact). Bacteria: four dots on a rotated square about the lens centre --
each 8.2 from its neighbours and 9.2 from the lens -- so they read as a loose
scatter; the reference's seven specks cannot hold the 8-unit clearance inside
a 30-unit lens. Lucide: `search` (circle plus diagonal handle).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "713363eb-bbe5-4962-bce9-7de2465bfdd4"
SOURCE_PATH = "icon_set/work/todo-references/bacteria magnifying glass_713363eb-bbe5-4962-bce9-7de2465bfdd4.svg"
AUTHOR = "claude-opus-5-5"

C, R = 21, 15
HANDLE_START = (C + 12, C + 9)
HANDLE_END = (42, 42)
DOTS = ((-3, -5), (5, -3), (-5, 3), (3, 5))


class BacteriaMagnifyingGlass(Solo48):
    icon_id = "bacteria-magnifying-glass"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science/microscopy"
    aliases = ("microbe search", "inspect bacteria", "germ magnifier")
    keywords = ("bacteria", "germ", "microbe", "magnifier", "lens", "search", "inspect")

    def build(self) -> None:
        self.add_arc("lens-a", HANDLE_START, (C - R, C), radius_x=R, radius_y=R, large_arc=False, sweep=True)
        self.add_arc("lens-b", (C - R, C), HANDLE_START, radius_x=R, radius_y=R, large_arc=True, sweep=True)
        self.add_contour("lens", "lens-a", "lens-b", closed=True)
        self.add_line("handle", HANDLE_START, HANDLE_END)
        self.relate("connect", "handle", "lens-a", "lens-b")
        for i, (dx, dy) in enumerate(DOTS, 1):
            self.add_dot(f"bacterium-{i}", (C + dx, C + dy))
