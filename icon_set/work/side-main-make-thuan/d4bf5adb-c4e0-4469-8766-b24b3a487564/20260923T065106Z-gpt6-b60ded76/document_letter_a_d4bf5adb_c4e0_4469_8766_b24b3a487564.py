"""A document marked with a large outlined capital A."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d4bf5adb-c4e0-4469-8766-b24b3a487564"
SOURCE_PATH = "pictographic-primitives/other/a text in file_d4bf5adb-c4e0-4469-8766-b24b3a487564.svg"
AUTHOR = "gpt-6"


class DocumentLetterA(Solo48):
    icon_id = "document-letter-a"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/document"
    aliases = ("a text file", "letter a document")
    keywords = ("file", "text", "alphabet", "typography")

    def build(self) -> None:
        # The upper-right diagonal is the page's folded-corner silhouette.
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

        # Hand-authored letter A, mirrored around x=24. The crossbar attaches
        # at exact leg vertices, keeping the source's single outlined glyph.
        self.add_line("a-left-lower", (17, 35), (19, 29))
        self.add_line("a-left-upper", (19, 29), (24, 14))
        self.add_line("a-right-upper", (24, 14), (29, 29))
        self.add_line("a-right-lower", (29, 29), (31, 35))
        self.add_contour("a-legs", "a-left-lower", "a-left-upper",
                         "a-right-upper", "a-right-lower")
        self.add_line("a-crossbar", (19, 29), (29, 29))
        self.relate("connect", "a-crossbar", "a-left-lower")
        self.relate("connect", "a-crossbar", "a-left-upper")
        self.relate("connect", "a-crossbar", "a-right-upper")
        self.relate("connect", "a-crossbar", "a-right-lower")
