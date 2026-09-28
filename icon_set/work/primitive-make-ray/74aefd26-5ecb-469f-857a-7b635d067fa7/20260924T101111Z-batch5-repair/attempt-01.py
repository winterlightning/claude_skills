"""Two people tucked into one bed with two hearts overhead.

Plan: repeated circular heads and repeated hearts above a connected bed rail.
The people are represented by their visible heads; their bodies are under the
blanket. Human full_body_ref.png supplies round heads; Lucide bed-double
supplies the rail and posts, while heart supplies the paired lobes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "74aefd26-5ecb-469f-857a-7b635d067fa7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/love boat_74aefd26-5ecb-469f-857a-7b635d067fa7.svg"
AUTHOR = "gpt-6"


class CoupleInBedWithHearts(Solo48):
    icon_id = "couple-in-bed-with-hearts"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/relationships"
    aliases = ("romantic-bed",)
    keywords = ("couple", "bed", "love", "hearts", "sleep")

    def build(self) -> None:
        for index, cx in enumerate((13, 35)):
            self.add_bezier(f"heart-{index}", (cx, 22),
                ((cx-4, 19), (cx-8, 15), (cx-8, 12)),
                ((cx-8, 8), (cx-3, 8), (cx, 11)),
                ((cx+3, 8), (cx+8, 8), (cx+8, 12)),
                ((cx+8, 15), (cx+4, 19), (cx, 22)))
        for index, cx in enumerate((14, 34)):
            self.add_arc(f"head-{index}-top", (cx-2, 32), (cx+2, 32), radius_x=2, sweep=True)
            self.add_arc(f"head-{index}-bottom", (cx+2, 32), (cx-2, 32), radius_x=2, sweep=True)
            self.add_contour(f"head-{index}", f"head-{index}-top", f"head-{index}-bottom", closed=True)
        self.add_line("bed-left", (6, 32), (6, 42))
        self.add_line("bed-rail", (6, 42), (42, 42))
        self.add_line("bed-right", (42, 32), (42, 42))
        self.relate("connect", "bed-left", "bed-rail")
        self.relate("connect", "bed-right", "bed-rail")
