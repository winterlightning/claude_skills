"""Modern Smartphone Device: independently authored container.

Construction plan: Rounded smartphone with bottom bezel, top earpiece and centered home bar; shared central axis.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/phones/mobile phone_e676ebab-d256-40ae-9c9a-301b15d45e29.svg. Lucide smartphone original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (smartphone-home-bar-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'e676ebab-d256-40ae-9c9a-301b15d45e29'
SOURCE_PATH = 'pictographic-primitives/phones/mobile phone_e676ebab-d256-40ae-9c9a-301b15d45e29.svg'
AUTHOR = 'claude-opus-5-5'


class SmartphoneHomeBarContainer(Container64):
    icon_id = 'smartphone-home-bar-container'
    keyshape = Keyshape.VRECT_M
    category = 'phones'
    categories = ('phones', 'primitives')
    aliases = ()
    keywords = ('smartphone', 'home', 'bar', 'container')

    def build(self) -> None:
        self.add_line('phone-0', (18, 4), (46, 4))
        self.add_arc('phone-1', (46, 4), (52, 10), radius_x=6)
        self.add_line('phone-2', (52, 10), (52, 54))
        self.add_arc('phone-3', (52, 54), (46, 60), radius_x=6)
        self.add_line('phone-4', (46, 60), (18, 60))
        self.add_arc('phone-5', (18, 60), (12, 54), radius_x=6)
        self.add_line('phone-6', (12, 54), (12, 10))
        self.add_arc('phone-7', (12, 10), (18, 4), radius_x=6)
        self.add_line('speaker', (28, 14), (36, 14))
        self.add_line('home', (28, 52), (36, 52))
        self.add_contour('phone', 'phone-0', 'phone-1', 'phone-2', 'phone-3', 'phone-4', 'phone-5', 'phone-6', 'phone-7', closed=True)
