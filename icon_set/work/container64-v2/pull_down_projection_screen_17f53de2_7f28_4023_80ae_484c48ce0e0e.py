"""Pull Down Projection Screen: independently authored container.

Construction plan: A hanging rectangular screen with extended top rail and central pull ring. Calendar informs straight header construction.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.svg. Lucide calendar original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (pull-down-projection-screen SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '17f53de2-7f28-4023-80ae-484c48ce0e0e'
SOURCE_PATH = 'pictographic-primitives/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.svg'
AUTHOR = 'claude-opus-5-5'


class PullDownProjectionScreen(Container64):
    icon_id = 'pull-down-projection-screen'
    keyshape = Keyshape.SQUARE
    category = 'office'
    categories = ('office', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('pull', 'down', 'projection', 'screen')

    def build(self) -> None:
        self.add_line('screen-0', (10, 6), (10, 40))
        self.add_arc('screen-1', (10, 40), (14, 44), radius_x=4, sweep=False)
        self.add_line('screen-2', (14, 44), (50, 44))
        self.add_arc('screen-3', (50, 44), (54, 40), radius_x=4, sweep=False)
        self.add_line('screen-4', (54, 40), (54, 6))
        self.add_line('rail', (6, 6), (58, 6))
        self.add_line('pull', (32, 44), (32, 50))
        self.add_arc('ring-0', (28, 54), (36, 54), radius_x=4)
        self.add_arc('ring-1', (36, 54), (28, 54), radius_x=4)
        self.add_contour('screen', 'screen-0', 'screen-1', 'screen-2', 'screen-3', 'screen-4')
        self.add_contour('ring', 'ring-0', 'ring-1', closed=True)
        self.relate('connect', 'screen', 'rail')
        self.relate('connect', 'pull', 'screen')
        self.relate('connect', 'pull', 'ring')
