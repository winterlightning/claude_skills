"""v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (towel-ring SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'towel-ring'
SOURCE_PATH = 'icon_set/dist/failed/container64/towel-ring.svg'
AUTHOR = 'claude-opus-5-5'


class TowelRing(Container64):
    icon_id = 'towel-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('circular-towel-ring-hanger',)
    keywords = ('towel', 'ring')

    def build(self) -> None:
        self.add_line('mount', (6, 6), (58, 6))
        self.add_line('hanger', (32, 6), (32, 14))
        self.add_arc('ring-0', (10, 36), (54, 36), radius_x=22)
        self.add_arc('ring-1', (54, 36), (10, 36), radius_x=22)
        self.add_contour('ring', 'ring-0', 'ring-1', closed=True)
        self.relate('connect', 'mount', 'hanger')
        self.relate('connect', 'hanger', 'ring')
