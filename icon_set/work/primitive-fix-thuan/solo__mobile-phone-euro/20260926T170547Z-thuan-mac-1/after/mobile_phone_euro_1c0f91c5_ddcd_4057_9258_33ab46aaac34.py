from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "1c0f91c5-ddcd-4057-9258-33ab46aaac34"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mobile-phone-euro/20260926T170547Z-thuan-mac-1/reference/mobile phone euro sign_1c0f91c5-ddcd-4057-9258-33ab46aaac34.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "mobile-phone-euro"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ("mobile", "phone", "smartphone")
    def build(self) -> None:
        self.add_polyline("phone-outline", (12,5),(36,5),(39,8),(39,40),(36,43),(12,43),(9,40),(9,8),closed=True)
        self.add_line("speaker", (20,9), (28,9))
        self.add_arc("euro-curve", (30,17), (30,31), radius_x=9, radius_y=8, sweep=False)
        self.add_line("euro-upper", (18,21), (28,21)); self.add_line("euro-lower", (17,27), (27,27))
        self.add_line("home", (21,39), (27,39))
