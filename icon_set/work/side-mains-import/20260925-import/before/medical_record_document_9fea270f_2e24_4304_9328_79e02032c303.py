"""A folded medical record document with an outlined cross."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9fea270f-2e24-4304-9328-79e02032c303"
SOURCE_PATH = "pictographic-primitives/health/medical file_9fea270f-2e24-4304-9328-79e02032c303.svg"
AUTHOR = "gpt-6"


class MedicalRecordDocument(Solo48):
    icon_id = "medical-record-document"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health/records"
    aliases = ("medical file", "health document")
    keywords = ("patient", "record", "cross", "medical")

    def build(self) -> None:
        # Folded page perimeter, with matching rounded outer corners.
        self.add_line("page-top", (12, 4), (31, 4))
        self.add_line("page-fold", (31, 4), (40, 13))
        self.add_line("page-right", (40, 13), (40, 40))
        self.add_arc("page-se", (40, 40), (36, 44), radius_x=4)
        self.add_line("page-bottom", (36, 44), (12, 44))
        self.add_arc("page-sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("page-left", (8, 40), (8, 8))
        self.add_arc("page-nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("page", "page-top", "page-fold", "page-right",
                         "page-se", "page-bottom", "page-sw", "page-left",
                         "page-nw", closed=True)

        # A single centered, square-cornered outline preserves the source cross.
        self.add_polyline("medical-cross", (20, 15), (28, 15), (28, 20),
                          (31, 20), (31, 28), (28, 28), (28, 33),
                          (20, 33), (20, 28), (17, 28), (17, 20),
                          (20, 20), closed=True)
