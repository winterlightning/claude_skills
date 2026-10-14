"""Tall shopfront for a two-line CLOSE label. Two mirrored awning scallops; SQUARE ink bounds (4,4)-(60,60). Lucide store original and atomic-debug informed the awning and continuous walls. Parent preserved."""

from ...keyshapes import Keyshape
from ._base import Container64
SOURCE_ICON_ID = 'b4fbca27-9be1-465c-821d-8b7db21f4d87'
SOURCE_PATH = 'pictographic-primitives/shopping/shop_b4fbca27-9be1-465c-821d-8b7db21f4d87.svg'
AUTHOR = 'gpt-6'

class AwningStorefrontContainerVariant2(Container64):
    icon_id = 'awning-storefront-container-v2'
    variant_of = 'awning-storefront-container'
    variant_label = 'Taller panel for wrapped shop text'
    keyshape = Keyshape.SQUARE
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ()

    def build(self) -> None:
        # Shared x=32 axis; two equal awning scallops and a taller, open shop front.
        # SQUARE ink (4,4)-(60,60). Lucide store informs the scallops and side walls.
        left, right, axis, eave, floor = 6, 58, 32, 10, 58
        self.add_line('roof-left', (left, eave), (12, 6))
        self.add_line('roof-top', (12, 6), (52, 6))
        self.add_line('roof-right', (52, 6), (right, eave))
        self.add_arc('scallop-right', (right, eave), (axis, eave), radius_x=13, radius_y=4)
        self.add_arc('scallop-left', (axis, eave), (left, eave), radius_x=13, radius_y=4)
        self.add_contour('awning', 'roof-left', 'roof-top', 'roof-right', 'scallop-right', 'scallop-left', closed=True)
        self.add_line('wall-left', (left, eave), (left, floor))
        self.add_line('floor', (left, floor), (right, floor))
        self.add_line('wall-right', (right, floor), (right, eave))
        self.add_contour('shop', 'wall-left', 'floor', 'wall-right')
        self.relate('connect', 'shop', 'awning')
