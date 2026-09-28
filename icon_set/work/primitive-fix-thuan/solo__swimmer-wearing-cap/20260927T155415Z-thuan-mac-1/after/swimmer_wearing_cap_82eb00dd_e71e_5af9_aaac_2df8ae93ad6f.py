"""Front facing swimmer's cap, ears, and face."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "82eb00dd-e71e-5af9-aaac-2df8ae93ad6f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__swimmer-wearing-cap/20260927T155415Z-thuan-mac-1/reference/swimming cap_82eb00dd-e71e-5af9-aaac-2df8ae93ad6f.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "swimmer-wearing-cap"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("swimming-cap",)
    keywords = ("swimmer", "cap", "ears", "face")

    def build(self):
        # One continuous head profile incorporates both ears, mirroring at x=24.
        self.add_arc("cap-dome", (8, 20), (40, 20), radius_x=16, radius_y=14)
        self.add_bezier("right-ear-upper", (40, 20), ((42, 21), (42, 23), (42, 24)))
        self.add_bezier("right-ear-lower", (42, 24), ((42, 27), (41, 28), (40, 29)))
        self.add_bezier("right-jaw", (40, 29), ((37, 37), (29, 42), (24, 42)))
        self.add_bezier("left-jaw", (24, 42), ((19, 42), (11, 37), (8, 29)))
        self.add_bezier("left-ear-lower", (8, 29), ((7, 28), (6, 27), (6, 24)))
        self.add_bezier("left-ear-upper", (6, 24), ((6, 23), (6, 21), (8, 20)))
        self.add_contour("head", "cap-dome", "right-ear-upper", "right-ear-lower", "right-jaw", "left-jaw", "left-ear-lower", "left-ear-upper", closed=True)
        self.add_line("cap-edge", (8, 20), (40, 20))
        self.relate("connect", "head", "cap-edge")
        self.add_arc("smile", (20, 29), (28, 29), radius_x=4, radius_y=2, sweep=False)
