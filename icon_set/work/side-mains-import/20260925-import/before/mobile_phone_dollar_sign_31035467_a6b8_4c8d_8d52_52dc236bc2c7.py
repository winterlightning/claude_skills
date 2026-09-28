"""A mobile phone displaying a dollar sign."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "31035467-a6b8-4c8d-8d52-52dc236bc2c7"
SOURCE_PATH = "pictographic-primitives/other/mobile phone dollar sign_31035467-a6b8-4c8d-8d52-52dc236bc2c7.svg"
AUTHOR = "claude-fable-5-1"


class MobilePhoneDollarSign(Solo48):
    icon_id = "mobile-phone-dollar-sign"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("payment phone", "dollar smartphone")
    keywords = ("mobile", "money", "commerce", "payment")

    def build(self) -> None:
        # Phone: Lucide smartphone frame, 4-unit corners. The footer divider
        # is dropped so the 20-unit currency mark keeps 10 units top and bottom.
        axis_x = 24
        left, right = 8, 2 * axis_x - 8
        radius = 4
        self.add_line("top", (12, 4), (36, 4))
        self.add_arc("ne", (36, 4), (right, 8), radius_x=radius)
        self.add_line("right", (right, 8), (right, 40))
        self.add_arc("se", (right, 40), (36, 44), radius_x=radius)
        self.add_line("bottom", (36, 44), (12, 44))
        self.add_arc("sw", (12, 44), (left, 40), radius_x=radius)
        self.add_line("left", (left, 40), (left, 8))
        self.add_arc("nw", (left, 8), (12, 4), radius_x=radius)
        self.add_contour("phone-frame", "top", "ne", "right", "se",
                         "bottom", "sw", "left", "nw", closed=True)
        # Currency mark: Lucide dollar-sign construction (two bows, no spine)
        # on rows y=14/24/34, ten units apart so curved pairs clear MIC.
        self.add_line("dollar-top", (28, 14), (20, 14))
        self.add_arc("dollar-upper-bow", (20, 14), (20, 24), radius_x=3, radius_y=5, sweep=False)
        self.add_line("dollar-middle", (20, 24), (28, 24))
        self.add_arc("dollar-lower-bow", (28, 24), (28, 34), radius_x=3, radius_y=5, sweep=True)
        self.add_line("dollar-bottom", (28, 34), (20, 34))
        self.add_contour("dollar", "dollar-top", "dollar-upper-bow", "dollar-middle",
                         "dollar-lower-bow", "dollar-bottom")
