from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3f60e9c-d2ca-5f4e-a16c-be1d8d20e5d7'
SOURCE_PATH = 'pictographic-primitives/shipping/container_b3f60e9c-d2ca-5f4e-a16c-be1d8d20e5d7.svg'
AUTHOR = 'gpt-6-astra'


class ShippingContainerShutter(Solo48):
    icon_id = 'shipping-container-shutter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ()
    keywords = ('container', 'shutter', 'freight', 'storage', 'door', 'panel')

    def build(self) -> None:
        # Square centerlines (6,6)-(42,42); recessed panel inset 8.
        self.add_polyline("frame", (6,6), (42,6), (42,42), (6,42), (6,6))
        self.add_polyline("panel", (14,14), (34,14), (34,24), (34,34), (14,34), (14,24), (14,14))
        self.add_line("slat", (14,24), (34,24))
        self.relate("connect", "panel", "slat")
