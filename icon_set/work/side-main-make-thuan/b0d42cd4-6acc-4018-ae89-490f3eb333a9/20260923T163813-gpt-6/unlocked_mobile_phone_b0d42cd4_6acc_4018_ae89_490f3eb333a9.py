from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b0d42cd4-6acc-4018-ae89-490f3eb333a9'
SOURCE_PATH = 'pictographic-primitives/other/mobile phone unlock_b0d42cd4-6acc-4018-ae89-490f3eb333a9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A rounded mobile phone displaying an open padlock.

    Plan: Phone x8..40,y4..44,r4. Lock body x17..31,y26..35,r2; top split at20,26. Shackle stem20,26 to20,17, semicircle center24,17 radius4 ending28,17 leaves9 centerline units above the lock top.
    References: Source phone/open padlock; Lucide smartphone frame construction previously inspected; Lucide lock-keyhole-open original and atoms inform attached left shackle and free right end. Source has no keyhole, so none added.
    """
    icon_id = 'unlocked-mobile-phone'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/other'
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
        self.add_line("lock-top-a", (17,26), (20,26))
        self.add_line("lock-top-b", (20,26), (31,26))
        self.add_line("lock-right", (31,26), (31,33))
        self.add_arc("lock-br", (31,33), (29,35), radius_x=2)
        self.add_line("lock-bottom", (29,35), (19,35))
        self.add_arc("lock-bl", (19,35), (17,33), radius_x=2)
        self.add_line("lock-left", (17,33), (17,26))
        self.add_contour("lock-body", "lock-top-a", "lock-top-b", "lock-right", "lock-br", "lock-bottom", "lock-bl", "lock-left", closed=True)
        self.add_line("shackle-stem", (20,26), (20,17))
        self.add_arc("shackle-arch", (20,17), (28,17), radius_x=4)
        self.add_contour("shackle", "shackle-stem", "shackle-arch")
        self.relate("connect", "lock-body", "shackle")
