from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "0de879ae-e966-445d-830f-f7fac1a38800"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/flat_0de879ae-e966-445d-830f-f7fac1a38800.svg"
AUTHOR = "gpt-6"

class FrontCarWindshield(Solo48):
    icon_id = "front-car-windshield"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("car windshield", "windscreen")
    keywords = ("car", "front", "glass")

    def build(self) -> None:
        # Shared horizontal centre axis; broad lower edge and narrower roof edge.
        self.add_polyline("windshield-outline", (10, 10), (38, 10), (44, 38), (4, 38), closed=True)
