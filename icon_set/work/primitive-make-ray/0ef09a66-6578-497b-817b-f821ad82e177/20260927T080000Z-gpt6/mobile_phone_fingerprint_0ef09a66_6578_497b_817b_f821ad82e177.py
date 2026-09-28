from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "0ef09a66-6578-497b-817b-f821ad82e177"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mobile-phone-fingerprint/20260926T170547Z-thuan-mac-1/reference/mobile phone fingerprint_0ef09a66-6578-497b-817b-f821ad82e177.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "mobile-phone-fingerprint"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ("mobile", "phone", "smartphone")
    def build(self) -> None:
        self.add_polyline("phone-outline", (12,5),(36,5),(39,8),(39,40),(36,43),(12,43),(9,40),(9,8),closed=True)
        self.add_line("speaker", (20,9), (28,9))
        self.add_arc("ridge-outer", (16,28), (32,28), radius_x=8, radius_y=8, sweep=False)
        self.add_arc("ridge-inner", (20,29), (28,29), radius_x=4, radius_y=5, sweep=False)
        self.add_line("ridge-center", (24,21), (24,30))
        self.add_arc("ridge-left", (16,25), (20,30), radius_x=7, radius_y=5, sweep=False)
        self.add_arc("ridge-right", (28,30), (32,25), radius_x=7, radius_y=5, sweep=False)
        self.add_line("home", (21,39), (27,39))
