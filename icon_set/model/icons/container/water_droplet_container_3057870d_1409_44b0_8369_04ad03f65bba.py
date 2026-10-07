"""Water Droplet: independently authored container.

Construction plan: Mirrored pointed drop with two broad tangent lower arcs; no internal symbol.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg. Lucide droplet original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (water-droplet-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.

v3 (2026-10-07): redrawn for symbol room on v2 (container-combination64): the shape caps it below 24, now it takes a 20 symbol with a 4 px gap.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg'
AUTHOR = 'claude-opus-5-5'


class WaterDropletContainer(Container64):
    icon_id = 'water-droplet-container'
    keyshape = Keyshape.VRECT_L
    category = 'smileys'
    categories = ('smileys', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('water', 'droplet', 'container')

    def build(self) -> None:
        # VRECT_L (was VRECT_M): round body r22 about (32,38) touching the frame sides and bottom, with straight
        # sides to the tip (32,4); mirrored about x = 32. Holds a symbol of 20 with a 4 px gap (was 19).
        self.add_line('drop-0', (32, 4), (15, 24))
        self.add_arc('drop-1', (15, 24), (10, 38), radius_x=24, sweep=False)
        self.add_arc('drop-2', (10, 38), (32, 60), radius_x=22, sweep=False)
        self.add_arc('drop-3', (32, 60), (54, 38), radius_x=22, sweep=False)
        self.add_arc('drop-4', (54, 38), (49, 24), radius_x=24, sweep=False)
        self.add_line('drop-5', (49, 24), (32, 4))
        self.add_contour('drop', 'drop-0', 'drop-1', 'drop-2', 'drop-3', 'drop-4', 'drop-5', closed=True)
