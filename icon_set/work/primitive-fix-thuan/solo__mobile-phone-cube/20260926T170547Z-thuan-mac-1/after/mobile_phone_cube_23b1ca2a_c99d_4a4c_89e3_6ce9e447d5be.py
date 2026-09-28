from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__mobile-phone-cube/20260926T170547Z-thuan-mac-1/reference/Mobile Phone Cube_23b1ca2a-c99d-4a4c-89e3-6ce9e447d5be.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "mobile-phone-cube"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ("mobile", "phone", "smartphone")
    def build(self) -> None:
        self.add_polyline("phone-outline", (12,5),(36,5),(39,8),(39,40),(36,43),(12,43),(9,40),(9,8),closed=True)
        self.add_line("speaker", (20,9), (28,9))
        self.add_polyline("cube-top", (24,15),(30,19),(24,23),(18,19),closed=True)
        self.add_polyline("cube-left", (18,19),(24,23),(24,31),(18,27),closed=True)
        self.add_polyline("cube-right", (24,23),(30,19),(30,27),(24,31),closed=True)
        self.add_line("home", (21,39), (27,39))
