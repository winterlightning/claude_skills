"""A clipped-corner image document with sun and two mountains."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "41f3ad63-cd17-441d-b26d-945da63c6f7c"
SOURCE_PATH = "pictographic-primitives/files/image file_41f3ad63-cd17-441d-b26d-945da63c6f7c.svg"
AUTHOR = "gpt-6"


class LandscapePictureMediaFile(Solo48):
    icon_id = "landscape-picture-media-file"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/media"
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
        # A compact but complete circular sun above a two-peak landscape.
        self.add_arc("sun-upper", (21, 16), (17, 16), radius_x=2, sweep=False)
        self.add_arc("sun-lower", (17, 16), (21, 16), radius_x=2, sweep=False)
        self.add_contour("sun", "sun-upper", "sun-lower", closed=True)
        self.add_polyline("landscape", (17, 35), (20, 27), (23, 31),
                          (28, 21), (31, 35), (17, 35), closed=True)
