"""Decorative Flower Vase: independently authored container.

Construction plan: Narrow open neck expands into a rounded pear-shaped vase; ellipse shoulders share an axis.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg. Lucide droplet original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (flower-vase-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): a symbol of at least 24 fits with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg'
AUTHOR = 'claude-opus-5-5'


class FlowerVaseContainer(Container64):
    icon_id = 'flower-vase-container'
    keyshape = Keyshape.SQUARE
    category = 'decoration'
    categories = ('decoration', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('flower', 'vase', 'container')

    def build(self) -> None:
        # SQUARE (was VRECT_M): a round-bellied vase, lip 22..42 at the top, neck 26..38, belly swelling to the full
        # keyshape width at y 39 and a flat base; holds a symbol of 26 with a 4 px gap (was 21). Mirrored about x = 32.
        self.add_line('lip', (22, 6), (42, 6))
        self.add_line('lip-right', (42, 6), (38, 12))
        self.add_line('neck-right', (38, 12), (38, 15))
        self.add_bezier('belly-right', (38, 15), ((51, 18), (58, 27), (58, 39)), ((58, 51), (50, 58), (40, 58)))
        self.add_line('base', (40, 58), (24, 58))
        self.add_bezier('belly-left', (24, 58), ((14, 58), (6, 51), (6, 39)), ((6, 27), (13, 18), (26, 15)))
        self.add_line('neck-left', (26, 15), (26, 12))
        self.add_line('lip-left', (26, 12), (22, 6))
        self.add_contour('vase', 'lip', 'lip-right', 'neck-right', 'belly-right', 'base', 'belly-left', 'neck-left', 'lip-left', closed=True)
