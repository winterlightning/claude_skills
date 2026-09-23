from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "26417ba5-2631-48ff-a294-d0bcf4e7a13e"
SOURCE_PATH = "pictographic-primitives/_uncategorized_21/god_26417ba5-2631-48ff-a294-d0bcf4e7a13e.svg"
AUTHOR = "gpt-6"

class PersonWithHalo(Solo48):
    icon_id = "person-with-halo"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/symbolic"
    aliases = ("haloed person",)
    keywords = ("person", "bust", "halo")

    def build(self) -> None:
        # Shared human bust proportions: head radius 6; bottom y30 to shoulder y38 is 8 centerline / 4 visible units.
        self.add_arc("halo-top", (12, 7), (36, 7), radius_x=12, radius_y=3, sweep=True)
        self.add_arc("halo-bottom", (36, 7), (12, 7), radius_x=12, radius_y=3, sweep=True)
        self.add_contour("halo", "halo-top", "halo-bottom", closed=True)
        self.add_arc("head-top", (18, 24), (30, 24), radius_x=6, sweep=True)
        self.add_arc("head-bottom", (30, 24), (18, 24), radius_x=6, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_polyline("shoulders", (8, 44), (10, 40), (16, 38), (32, 38), (38, 40), (40, 44))
