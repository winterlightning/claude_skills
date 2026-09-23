"""A magnifying lens contains two offset footprints and a diagonal handle.

Symbol plan: one symmetric rounded lens contour shares an explicit lower
right point with its handle; each footprint repeats an oval sole and heel
mark. Lucide search informed the handle; footprints informed the paired marks.
The staggered feet and down-right handle are intentional asymmetry.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3932acf9-d8a9-4dab-a9e2-4e0a52270bc7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/monitoring activity tracking 2_3932acf9-d8a9-4dab-a9e2-4e0a52270bc7.svg"
AUTHOR = "gpt-6"


class MagnifyingGlassFootprints(Solo48):
    icon_id = "magnifying-glass-footprints"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "activity/tracking"
    aliases = ("activity tracking magnifier", "search footprints")
    keywords = ("monitoring", "search", "steps", "walking")

    def oval(self, name: str, x: int, y: int, rx: int, ry: int) -> None:
        self.add_arc(name + "-right", (x, y - ry), (x, y + ry), radius_x=rx, radius_y=ry, sweep=True)
        self.add_arc(name + "-left", (x, y + ry), (x, y - ry), radius_x=rx, radius_y=ry, sweep=True)
        self.add_contour(name, name + "-right", name + "-left", closed=True)

    def build(self) -> None:
        self.add_bezier(
            "lens", (20, 6),
            ((28, 6), (34, 12), (34, 20)),
            ((34, 25), (33, 28), (30, 30)),
            ((28, 33), (24, 34), (20, 34)),
            ((12, 34), (6, 28), (6, 20)),
            ((6, 12), (12, 6), (20, 6)),
        )
        self.add_line("handle", (30, 30), (42, 42))
        self.relate("connect", "lens", "handle")
        self.oval("foot-left-sole", 16, 16, 3, 5)
        self.add_dot("foot-left-heel", (18, 25))
        self.oval("foot-right-sole", 26, 24, 3, 5)
        self.add_dot("foot-right-heel", (23, 31))
