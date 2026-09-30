"""Circular Refresh Arrow: independently authored container.

Construction plan: Circular clockwise arrow with a broad open lower-right gap; retain source direction.
Keyshape CIRCLE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/synchronize refresh arrow_b3069a62-a707-4dfe-ad1b-5c5d76ab3dc0.svg. Lucide refresh-cw original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (clockwise-refresh-container CIRCLE -> CIRCLE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'b3069a62-a707-4dfe-ad1b-5c5d76ab3dc0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/synchronize refresh arrow_b3069a62-a707-4dfe-ad1b-5c5d76ab3dc0.svg'
AUTHOR = 'claude-opus-5-5'


class ClockwiseRefreshContainer(Container64):
    icon_id = 'clockwise-refresh-container'
    keyshape = Keyshape.CIRCLE
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('clockwise', 'refresh', 'container')

    def build(self) -> None:
        self.add_arc('ring-0', (32, 60), (4, 32), radius_x=28)
        self.add_arc('ring-1', (4, 32), (32, 4), radius_x=28)
        self.add_arc('ring-2', (32, 4), (60, 32), radius_x=28)
        self.add_line('head-1', (49, 24), (60, 32))
        self.add_line('head-2', (60, 32), (53, 42))
        self.add_contour('ring', 'ring-0', 'ring-1', 'ring-2')
        self.add_contour('head', 'head-1', 'head-2')
        self.relate('connect', 'head', 'ring')
