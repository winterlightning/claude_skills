from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '155592b3-ec54-46c3-8558-333e4090664f'
SOURCE_PATH = 'pictographic-primitives/shipping/package_155592b3-ec54-46c3-8558-333e4090664f.svg'
AUTHOR = 'gpt-6-astra'


class ClosedShippingBox(Solo48):
    icon_id = 'closed-shipping-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('box', 'parcel', 'shipping', 'package', 'carton', 'tape')

    def build(self) -> None:
        # Shared centre axis 24; paired lid seams and shoulders.
        self.add_polyline("outline", (4,21), (10,8), (20,8), (28,8), (38,8), (44,21), (44,40), (4,40), (4,21))
        self.add_polyline("lid-edge", (4,21), (17,21), (31,21), (44,21))
        self.add_line("tape-left", (20,8), (17,21))
        self.add_line("tape-right", (28,8), (31,21))
        self.relate("connect", "outline", "lid-edge")
        for tape in ("tape-left", "tape-right"):
            self.relate("connect", "outline", tape)
            self.relate("connect", "lid-edge", tape)
