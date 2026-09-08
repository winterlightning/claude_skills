"""Top-view mouse, rebuilt from the supplied reference on SOLO48.

VRECT_L centerline extremes: (8, 2)-(40, 46). Mirrored about x=24.
Lucide mouse informs tangent quarter-circle shoulders and a solid wheel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49aa3ae9-4599-4f0a-839e-996103c1a778'
SOURCE_PATH = 'pictographic-primitives/computers/batch-07/mouse remote_49aa3ae9-4599-4f0a-839e-996103c1a778.svg'


class WirelessMouseWithSignal(Solo48):
    icon_id = 'wireless-mouse-with-signal'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ('remote mouse',)
    keywords = ("mouse", "wireless", "scroll wheel", "computer", "peripheral")

    def build(self) -> None:
        # Equal corner radii and tangent straight walls preserve the capsule.
        self.add_line("body-top", (23, 22), (25, 22))
        self.add_arc("body-ne", (25, 22), (35, 32), radius_x=10)
        self.add_line("body-right", (35, 32), (35, 36))
        self.add_arc("body-se", (35, 36), (25, 46), radius_x=10)
        self.add_line("body-bottom", (25, 46), (23, 46))
        self.add_arc("body-sw", (23, 46), (13, 36), radius_x=10)
        self.add_line("body-left", (13, 36), (13, 32))
        self.add_arc("body-nw", (13, 32), (23, 22), radius_x=10)
        self.add_contour("body", "body-top", "body-ne", "body-right", "body-se",
                         "body-bottom", "body-sw", "body-left", "body-nw", closed=True)
        # The outlined source wheel becomes a readable round-capped stroke.
        self.add_line("scroll-wheel", (24, 30), (24, 34))
        # Two waves replace three fine source arcs to preserve negative space.
        self.add_arc("signal-outer-left", (8, 8), (24, 2), radius_x=16, radius_y=6)
        self.add_arc("signal-outer-right", (24, 2), (40, 8), radius_x=16, radius_y=6)
        self.add_contour("signal-outer", "signal-outer-left", "signal-outer-right")
        self.add_arc("signal-inner-left", (15, 14), (24, 10), radius_x=9, radius_y=4)
        self.add_arc("signal-inner-right", (24, 10), (33, 14), radius_x=9, radius_y=4)
        self.add_contour("signal-inner", "signal-inner-left", "signal-inner-right")
