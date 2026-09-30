"""Medical IV Infusion Bag: independently authored container.

Construction plan: Rounded bag shoulder and bottom outlet nozzle with a short delivery tube; no medical glyph.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/health/blood bag_ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada.svg. Lucide battery-charging original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (iv-infusion-bag-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada'
SOURCE_PATH = 'pictographic-primitives/health/blood bag_ddd5c887-7f6f-4c09-900f-c7b0eb9b5ada.svg'
AUTHOR = 'claude-opus-5-5'


class IvInfusionBagContainer(Container64):
    icon_id = 'iv-infusion-bag-container'
    keyshape = Keyshape.VRECT_M
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('iv', 'infusion', 'bag', 'container')

    def build(self) -> None:
        self.add_line('bag-0', (22, 4), (42, 4))
        self.add_arc('bag-1', (42, 4), (52, 16), radius_x=10, radius_y=12)
        self.add_line('bag-2', (52, 16), (52, 37))
        self.add_arc('bag-3', (52, 37), (42, 48), radius_x=10, radius_y=11)
        self.add_line('bag-4', (42, 48), (38, 48))
        self.add_line('bag-5', (38, 48), (38, 54))
        self.add_line('bag-6', (38, 54), (26, 54))
        self.add_line('bag-7', (26, 54), (26, 48))
        self.add_line('bag-8', (26, 48), (22, 48))
        self.add_arc('bag-9', (22, 48), (12, 37), radius_x=10, radius_y=11)
        self.add_line('bag-10', (12, 37), (12, 16))
        self.add_arc('bag-11', (12, 16), (22, 4), radius_x=10, radius_y=12)
        self.add_line('tube', (32, 54), (32, 60))
        self.add_contour('bag', 'bag-0', 'bag-1', 'bag-2', 'bag-3', 'bag-4', 'bag-5', 'bag-6', 'bag-7', 'bag-8', 'bag-9', 'bag-10', 'bag-11', closed=True)
        self.relate('connect', 'tube', 'bag')
