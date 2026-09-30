"""Decorative Flower Vase: independently authored container.

Construction plan: Narrow open neck expands into a rounded pear-shaped vase; ellipse shoulders share an axis.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg. Lucide droplet original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (flower-vase-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg'
AUTHOR = 'claude-opus-5-5'


class FlowerVaseContainer(Container64):
    icon_id = 'flower-vase-container'
    keyshape = Keyshape.VRECT_M
    category = 'decoration'
    categories = ('decoration', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('flower', 'vase', 'container')

    def build(self) -> None:
        self.add_line('vase-0', (20, 4), (44, 4))
        self.add_line('vase-1', (44, 4), (38, 13))
        self.add_line('vase-2', (38, 13), (38, 19))
        self.add_arc('vase-3', (38, 19), (52, 41), radius_x=18, radius_y=24)
        self.add_arc('vase-4', (52, 41), (38, 60), radius_x=14, radius_y=19)
        self.add_line('vase-5', (38, 60), (26, 60))
        self.add_arc('vase-6', (26, 60), (12, 41), radius_x=14, radius_y=19)
        self.add_arc('vase-7', (12, 41), (26, 19), radius_x=18, radius_y=24)
        self.add_line('vase-8', (26, 19), (26, 13))
        self.add_line('vase-9', (26, 13), (20, 4))
        self.add_contour('vase', 'vase-0', 'vase-1', 'vase-2', 'vase-3', 'vase-4', 'vase-5', 'vase-6', 'vase-7', 'vase-8', 'vase-9', closed=True)
