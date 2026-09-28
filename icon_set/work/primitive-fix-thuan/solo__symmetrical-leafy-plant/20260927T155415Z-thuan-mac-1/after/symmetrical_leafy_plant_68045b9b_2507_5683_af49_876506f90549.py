"""Five-leaf wasabi plant, redrawn from the supplied reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "68045b9b-2507-5683-af49-876506f90549"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__symmetrical-leafy-plant/20260927T155415Z-thuan-mac-1/reference/wasabi plant_68045b9b-2507-5683-af49-876506f90549.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "symmetrical-leafy-plant"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ("wasabi-plant",)
    keywords = ("plant", "leaves", "stem", "wasabi")

    def build(self):
        # Five pointed leaves share the vertical stem; mirrored pairs use one definition.
        self.add_line("stem", (24, 15), (24, 44))
        self.add_bezier("top-left", (24, 4), ((18, 8), (18, 11), (24, 15)))
        self.add_bezier("top-right", (24, 15), ((30, 11), (30, 8), (24, 4)))
        self.add_contour("top-leaf", "top-left", "top-right", closed=True)
        self.relate("connect", "stem", "top-leaf")
        for side in (-1, 1):
            suffix = "left" if side == -1 else "right"
            mirror = lambda x: 24 + side * x
            for tier, attach_y, tip_y in (("upper", 25, 22), ("lower", 40, 37)):
                name = f"{tier}-{suffix}-leaf"
                rise = 7 if tier == "upper" else 5
                self.add_bezier(name + "-upper", (24, attach_y), ((mirror(6), attach_y - rise), (mirror(12), tip_y - 2), (mirror(16), tip_y)))
                self.add_bezier(name + "-lower", (mirror(16), tip_y), ((mirror(16), tip_y + 3), (mirror(13), attach_y), (mirror(9), attach_y + 1)))
                self.add_contour(name, name + "-upper", name + "-lower")
                self.relate("connect", "stem", name)
