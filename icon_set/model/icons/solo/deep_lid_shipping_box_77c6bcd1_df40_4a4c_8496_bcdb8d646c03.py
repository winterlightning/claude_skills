from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '77c6bcd1-df40-4a4c-8496-bcdb8d646c03'
SOURCE_PATH = 'pictographic-primitives/shipping/package_77c6bcd1-df40-4a4c-8496-bcdb8d646c03.svg'
AUTHOR = 'gpt-6-astra'


class DeepLidShippingBox(Solo48):
    icon_id = 'deep-lid-shipping-box'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('box', 'parcel', 'shipping', 'package', 'carton', 'tape')

    def build(self) -> None:
        # Shared centre axis 24; paired lid seams and shoulders.
        self.add_polyline("outline", (4,24), (10,8), (20,8), (28,8), (38,8), (44,24), (44,40), (4,40), (4,24))
        self.add_polyline("lid-edge", (4,24), (17,24), (31,24), (44,24))
        self.add_line("tape-left", (20,8), (17,24))
        self.add_line("tape-right", (28,8), (31,24))
        self.relate("connect", "outline", "lid-edge")
        for tape in ("tape-left", "tape-right"):
            self.relate("connect", "outline", tape)
            self.relate("connect", "lid-edge", tape)
