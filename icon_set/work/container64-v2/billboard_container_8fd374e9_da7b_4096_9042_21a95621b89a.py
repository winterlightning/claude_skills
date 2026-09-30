"""Large Display Billboard Sign: independently authored container.

Construction plan: A large rounded sign panel supported by two equal posts and feet.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/billboard_8fd374e9-da7b-4096-9042-21a95621b89a.svg. Lucide calendar original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (billboard-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '8fd374e9-da7b-4096-9042-21a95621b89a'
SOURCE_PATH = 'pictographic-primitives/business/billboard_8fd374e9-da7b-4096-9042-21a95621b89a.svg'
AUTHOR = 'claude-opus-5-5'


class BillboardContainer(Container64):
    icon_id = 'billboard-container'
    keyshape = Keyshape.SQUARE
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('billboard', 'container')

    def build(self) -> None:
        self.add_line('panel-0', (11, 6), (53, 6))
        self.add_arc('panel-1', (53, 6), (58, 11), radius_x=5)
        self.add_line('panel-2', (58, 11), (58, 40))
        self.add_arc('panel-3', (58, 40), (53, 45), radius_x=5)
        self.add_line('panel-4', (53, 45), (11, 45))
        self.add_arc('panel-5', (11, 45), (6, 40), radius_x=5)
        self.add_line('panel-6', (6, 40), (6, 11))
        self.add_arc('panel-7', (6, 11), (11, 6), radius_x=5)
        self.add_line('post-10', (14, 45), (14, 58))
        self.add_line('foot-10', (8, 58), (20, 58))
        self.add_line('post-54', (50, 45), (50, 58))
        self.add_line('foot-54', (44, 58), (56, 58))
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
        self.relate('connect', 'panel', 'post-10')
        self.relate('connect', 'post-10', 'foot-10')
        self.relate('connect', 'panel', 'post-54')
        self.relate('connect', 'post-54', 'foot-54')
