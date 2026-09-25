from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '45efdc96-5aab-49eb-ac68-b0e1ceb428c9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone key_45efdc96-5aab-49eb-ac68-b0e1ceb428c9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A mobile phone displaying a diagonal round-bow security key.

    Plan: Phone bounds x8..40,y4..44 radius4 with panel y36. Key circle center22,22 radius5 uses exact 3-4-5 attachment25,18; shaft points upper-right. One terminal tooth retained.
    References: Source reference supplies complete phone and key arrangement. Lucide smartphone original/atoms inform the rounded enclosure; key-round original/atoms inform coherent ring/shaft topology. Existing SYMBOL32 module inspected for context only; geometry authored anew.
    """
    icon_id = 'smartphone-security-key'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ()

    def build(self):
        left, right, top, bottom, radius = 8, 40, 4, 44, 4
        self.add_line("top", (12,top), (36,top))
        self.add_arc("tr", (36,top), (right,8), radius_x=radius)
        self.add_line("right-upper", (right,8), (right,36))
        self.add_line("right-lower", (right,36), (right,40))
        self.add_arc("br", (right,40), (36,bottom), radius_x=radius)
        self.add_line("bottom", (36,bottom), (12,bottom))
        self.add_arc("bl", (12,bottom), (left,40), radius_x=radius)
        self.add_line("left-lower", (left,40), (left,36))
        self.add_line("left-upper", (left,36), (left,8))
        self.add_arc("tl", (left,8), (12,top), radius_x=radius)
        self.add_contour("phone", "top", "tr", "right-upper", "right-lower", "br", "bottom", "bl", "left-lower", "left-upper", "tl", closed=True)
        self.add_line("panel", (left,36), (right,36))
        self.relate("connect", "phone", "panel")
        cx, cy, radius = 22, 22, 5
        join = (25,18)
        opposite = (19,26)
        self.add_arc("bow-a", join, opposite, radius_x=radius)
        self.add_arc("bow-b", opposite, join, radius_x=radius)
        self.add_contour("bow", "bow-a", "bow-b", closed=True)
        self.add_polyline("shaft", join, (31,13), (27,13))
        self.relate("connect", "bow", "shaft")
