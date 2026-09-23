"""Two people tucked into one bed with two hearts overhead.

Plan: repeated circular heads and repeated hearts above a connected bed rail.
The people are represented by their visible heads; their bodies are under the
blanket. Human full_body_ref.png supplies round heads; Lucide bed-double
supplies the rail and posts, while heart supplies the paired lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "74aefd26-5ecb-469f-857a-7b635d067fa7"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/love boat_74aefd26-5ecb-469f-857a-7b635d067fa7.svg"
AUTHOR = "gpt-6"


class CoupleInBedWithHearts(Solo48):
    icon_id = "couple-in-bed-with-hearts"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/relationships"
    aliases = ("romantic-bed",)
    keywords = ("couple", "bed", "love", "hearts", "sleep")

    def build(self) -> None:
        for index, cx in enumerate((13, 35)):
            self.add_polyline(f"heart-{index}", (cx, 17), (cx-5, 12),
                              (cx-5, 10), (cx-3, 8), (cx, 10),
                              (cx+3, 8), (cx+5, 10), (cx+5, 12), closed=True)
        for index, cx in enumerate((14, 34)):
            self.add_arc(f"head-{index}-top", (cx-2, 27), (cx+2, 27), radius_x=2, sweep=True)
            self.add_arc(f"head-{index}-bottom", (cx+2, 27), (cx-2, 27), radius_x=2, sweep=True)
            self.add_contour(f"head-{index}", f"head-{index}-top", f"head-{index}-bottom", closed=True)
        self.add_line("bed-left", (4, 30), (4, 40))
        self.add_line("bed-rail", (4, 37), (44, 37))
        self.add_line("bed-right", (44, 30), (44, 40))
        self.relate("connect", "bed-left", "bed-rail")
        self.relate("connect", "bed-right", "bed-rail")
