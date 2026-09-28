from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "e101e849-9e14-4d6e-9afb-b2a07c50a1df"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mobile-phone-circle-add/20260926T170547Z-thuan-mac-1/reference/mobile phone circle add_e101e849-9e14-4d6e-9afb-b2a07c50a1df.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "mobile-phone-circle-add"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ("mobile", "phone", "smartphone")
    def build(self) -> None:
        self.add_polyline("phone-outline", (12,5),(36,5),(39,8),(39,40),(36,43),(12,43),(9,40),(9,8),closed=True)
        self.add_line("speaker", (20,9), (28,9))
        self.add_arc("badge-top", (24,16), (24,32), radius_x=8, radius_y=8, sweep=True)
        self.add_arc("badge-bottom", (24,32), (24,16), radius_x=8, radius_y=8, sweep=True)
        self.add_line("plus-vertical", (24,20), (24,28)); self.add_line("plus-horizontal", (20,24), (28,24))
        self.add_line("home", (21,39), (27,39))
