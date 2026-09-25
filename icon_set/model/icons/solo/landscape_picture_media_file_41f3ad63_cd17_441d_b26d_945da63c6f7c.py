"""A clipped-corner image document with a sun and a mountain."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "41f3ad63-cd17-441d-b26d-945da63c6f7c"
SOURCE_PATH = "pictographic-primitives/files/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg"
AUTHOR = "claude-fable-5-1"


class LandscapePictureMediaFile(Solo48):
    icon_id = "landscape-picture-media-file-solo"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "files"
    categories = ("files", "other", "primitives-generate")
    aliases = ("image file", "picture document")
    keywords = ("photo", "landscape", "mountain", "file")

    def build(self) -> None:
        self.add_line("top", (12, 4), (31, 4))
        self.add_line("fold-angle", (31, 4), (40, 13))
        self.add_line("right", (40, 13), (40, 40))
        self.add_arc("corner-se", (40, 40), (36, 44), radius_x=4)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("corner-sw", (12, 44), (8, 40), radius_x=4)
        self.add_line("left", (8, 40), (8, 8))
        self.add_arc("corner-nw", (8, 8), (12, 4), radius_x=4)
        self.add_contour("page-outline", "top", "fold-angle", "right",
                         "corner-se", "bottom", "corner-sw", "left",
                         "corner-nw", closed=True)
        # Lucide image: a complete 6-unit sun and one open mountain line, so
        # nothing encloses a pocket below a valley.
        self.add_arc("sun-upper", (23, 16), (17, 16), radius_x=3, sweep=False)
        self.add_arc("sun-lower", (17, 16), (23, 16), radius_x=3, sweep=False)
        self.add_contour("sun", "sun-upper", "sun-lower", closed=True)
        self.add_polyline("mountain", (17, 35), (27, 26), (31, 33))
