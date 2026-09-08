"""Top-view mouse, rebuilt from the supplied reference on SOLO48.

VRECT_L centerline extremes: (8, 2)-(40, 46). Mirrored about x=24.
Lucide mouse informs tangent quarter-circle shoulders and a solid wheel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2093c04a-d4d9-43f4-8144-230c0b88af74'
SOURCE_PATH = 'pictographic-primitives/computers/batch-07/mouse smart_2093c04a-d4d9-43f4-8144-230c0b88af74.svg'
AUTHOR = 'astra-chatgpt'


class WirelessMouse(Solo48):
    icon_id = 'wireless-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ('cordless mouse',)
    keywords = ("mouse", "wireless", "scroll wheel", "computer", "peripheral")

    def build(self) -> None:
        # Equal corner radii and tangent straight walls preserve the capsule.
        self.add_line("body-top", (22, 2), (26, 2))
        self.add_arc("body-ne", (26, 2), (40, 16), radius_x=14)
        self.add_line("body-right", (40, 16), (40, 32))
        self.add_arc("body-se", (40, 32), (26, 46), radius_x=14)
        self.add_line("body-bottom", (26, 46), (22, 46))
        self.add_arc("body-sw", (22, 46), (8, 32), radius_x=14)
        self.add_line("body-left", (8, 32), (8, 16))
        self.add_arc("body-nw", (8, 16), (22, 2), radius_x=14)
        self.add_contour("body", "body-top", "body-ne", "body-right", "body-se",
                         "body-bottom", "body-sw", "body-left", "body-nw", closed=True)
        # The outlined source wheel becomes a readable round-capped stroke.
        self.add_line("scroll-wheel", (24, 12), (24, 20))
