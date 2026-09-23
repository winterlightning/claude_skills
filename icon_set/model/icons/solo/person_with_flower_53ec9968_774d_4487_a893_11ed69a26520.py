from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "53ec9968-774d-4487-a893-11ed69a26520"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/florist_53ec9968-774d-4487-a893-11ed69a26520.svg"
AUTHOR = "gpt-6"

class PersonWithFlower(Solo48):
    icon_id = "person-with-flower"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/occupation"
    aliases = ("florist",)
    keywords = ("person", "flower", "gardener")

    def build(self) -> None:
        # Shared human bust: head radius 5, y=16 lower centerline, shoulders y=24: exact 8-unit centerline gap.
        self.add_arc("head-top", (8, 11), (18, 11), radius_x=5, sweep=True)
        self.add_arc("head-bottom", (18, 11), (8, 11), radius_x=5, sweep=True)
        self.add_contour("head", "head-top", "head-bottom", closed=True)
        self.add_polyline("body", (6, 42), (6, 31), (10, 24), (20, 24), (20, 42))
        self.add_arc("bloom-top", (31, 13), (41, 13), radius_x=5, sweep=True)
        self.add_arc("bloom-bottom", (41, 13), (31, 13), radius_x=5, sweep=True)
        self.add_contour("bloom", "bloom-top", "bloom-bottom", closed=True)
        self.add_line("stem", (36, 18), (36, 42))
        self.add_line("leaf-left", (36, 34), (28, 30))
        self.add_line("leaf-right", (36, 34), (42, 30))
        self.relate("connect", "bloom", "stem")
        self.relate("connect", "stem", "leaf-left")
        self.relate("connect", "stem", "leaf-right")
