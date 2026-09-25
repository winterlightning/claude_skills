from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c0f91c5-ddcd-4057-9258-33ab46aaac34'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A rounded mobile phone showing a euro sign above a bottom panel.

    Plan: Rounded rectangle x8..40 y4..44 radius4; split walls at bottom panel y36. Euro is one C contour with an attached single crossbar as in source, about x24 y20.
    References: Supplied phone reference; Lucide smartphone rounded frame and euro open-C construction, original and atomic geometry.
    """
    icon_id = 'mobile-phone-euro'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
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
        self.add_arc("euro-upper", (29,13), (17,20), radius_x=12, radius_y=7, sweep=False)
        self.add_arc("euro-lower", (17,20), (29,27), radius_x=12, radius_y=7, sweep=False)
        self.add_contour("euro", "euro-upper", "euro-lower")
        self.add_line("euro-bar", (17,20), (26,20))
        self.relate("connect", "euro", "euro-bar")
