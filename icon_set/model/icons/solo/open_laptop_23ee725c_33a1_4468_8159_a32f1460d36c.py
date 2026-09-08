"""open-laptop: reconstructed from the batch-01 references on SOLO48.

Duplicate source drawings share one concept; SOURCE_REFERENCES retains every ID.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23ee725c-33a1-4468-8159-a32f1460d36c'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop 1_23ee725c-33a1-4468-8159-a32f1460d36c.svg'
SOURCE_REFERENCES = (('23ee725c-33a1-4468-8159-a32f1460d36c', 'pictographic-primitives/computers/batch-01/laptop 1_23ee725c-33a1-4468-8159-a32f1460d36c.svg'), ('9c785f9a-558d-4793-8f09-218c477d8c84', 'pictographic-primitives/computers/batch-01/laptop 1_9c785f9a-558d-4793-8f09-218c477d8c84.svg'), ('0eca8bb8-75fe-4501-aa58-53ce337798cc', 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'), ('4679969c-dfb9-4a03-ab57-4d2eded56e5a', 'pictographic-primitives/computers/batch-01/laptop_4679969c-dfb9-4a03-ab57-4d2eded56e5a.svg'), ('7a7343f1-5eae-443d-b8b7-d063758ee85e', 'pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg'), ('96bd0a70-5265-56a5-8f8c-7df6339b6c49', 'pictographic-primitives/computers/batch-01/laptop_96bd0a70-5265-56a5-8f8c-7df6339b6c49.svg'))

class OpenLaptop(Solo48):
    icon_id = "open-laptop"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("notebook-computer", "laptop")
    keywords = ("laptop", "computer", "portable", "screen", "notebook")

    def build(self) -> None:
        # Centreline extremes (2,8)-(46,40). Mirrored about x=24.
        # Lucide laptop informs the rounded screen and broad flared base.
        self.add_line("top", (10, 8), (38, 8))
        self.add_arc("upper-right", (38, 8), (42, 12), radius_x=4)
        self.add_line("screen-right", (42, 12), (42, 30))
        self.add_line("base-right", (42, 30), (46, 40))
        self.add_line("base-bottom", (46, 40), (2, 40))
        self.add_line("base-left", (2, 40), (6, 30))
        self.add_line("screen-left", (6, 30), (6, 12))
        self.add_arc("upper-left", (6, 12), (10, 8), radius_x=4)
        self.add_contour("outline", "top", "upper-right", "screen-right",
                         "base-right", "base-bottom", "base-left", "screen-left",
                         "upper-left", closed=True)
        self.add_line("hinge", (6, 30), (42, 30))
        self.relate("connect", "outline", "hinge")
