from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '958637b4-0216-5d2f-a6a7-e9708b032af8'
SOURCE_PATH = 'pictographic-primitives/shipping/logistic damaged package_958637b4-0216-5d2f-a6a7-e9708b032af8.svg'
AUTHOR = 'gpt-6-astra'


class DamagedShippingBox(Solo48):
    icon_id = 'damaged-shipping-box'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shipping"
    aliases = ()
    keywords = ('box', 'parcel', 'damage', 'tear', 'shipping', 'package')

    def build(self) -> None:
        # Square centerlines (6,6)-(42,42); perspective faces share lid corners.
        self.add_polyline("outline", (24,6), (42,15), (42,33), (24,42), (6,33), (6,15), (24,6))
        self.add_polyline("lid", (6,15), (24,24), (42,15))
        self.add_polyline("torn-corner", (24,24), (24,29), (30,32), (24,37), (24,42))
        self.relate("connect", "outline", "lid")
        self.relate("connect", "outline", "torn-corner")
        self.relate("connect", "lid", "torn-corner")
