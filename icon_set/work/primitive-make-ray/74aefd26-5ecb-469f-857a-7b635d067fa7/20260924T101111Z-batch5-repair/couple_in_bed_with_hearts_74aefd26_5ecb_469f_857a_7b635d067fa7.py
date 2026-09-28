"""love boat: standalone repair of supplied reference.

Plan: Wide paired heads and bed rail. Keyshape HRECT_L.
Reduction: Omitted blanket contour and second bed rail; rounded paired hearts and visible heads carry the scene.
Construction references: local Lucide originals and atomic-debug: bed-double, heart.
human_ref/full_body_ref.png: repeated radius-2 heads at y=30 end at y=32; bed/body cover at y=40 gives 8 centerline / 4 ink gap. Bodies are covered.
All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

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
        # Shared heart lobes have exact cardinal extremes and broad lower bowls.
        for index, cx in enumerate((12, 36)):
            self.add_arc(f"heart-{index}-left", (cx-8, 12), (cx, 12), radius_x=4)
            self.add_arc(f"heart-{index}-right", (cx, 12), (cx+8, 12), radius_x=4)
            self.add_bezier(f"heart-{index}-bottom", (cx+8, 12),
                ((cx+8, 17), (cx+3, 20), (cx, 20)),
                ((cx-3, 20), (cx-8, 17), (cx-8, 12)))
            self.add_contour(f"heart-{index}",f"heart-{index}-left",f"heart-{index}-right",f"heart-{index}-bottom",closed=True)
        for index, cx in enumerate((14, 34)):
            self.add_arc(f"head-{index}-top", (cx-2, 30), (cx+2, 30), radius_x=2, sweep=True)
            self.add_arc(f"head-{index}-bottom", (cx+2, 30), (cx-2, 30), radius_x=2, sweep=True)
            self.add_contour(f"head-{index}", f"head-{index}-top", f"head-{index}-bottom", closed=True)
        self.add_line("bed-left", (4, 30), (4, 40))
        self.add_line("bed-rail", (4, 40), (44, 40))
        self.add_line("bed-right", (44, 30), (44, 40))
        self.relate("connect", "bed-left", "bed-rail")
        self.relate("connect", "bed-right", "bed-rail")
