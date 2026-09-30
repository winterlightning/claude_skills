"""Victory Achievement Trophy Cup: independently authored container.

Construction plan: Symmetric deep cup, two loop handles, flared stem and plinth; preserve all trophy features.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/trophy_8f2bc2ca-50f8-49a3-87de-95aa816792cc.svg. Lucide trophy original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check does not clear.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (trophy-cup-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '8f2bc2ca-50f8-49a3-87de-95aa816792cc'
SOURCE_PATH = 'pictographic-primitives/business/trophy_8f2bc2ca-50f8-49a3-87de-95aa816792cc.svg'
AUTHOR = 'claude-opus-5-5'


class TrophyCupContainer(Container64):
    icon_id = 'trophy-cup-container'
    keyshape = Keyshape.SQUARE
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('trophy', 'cup', 'container')

    def build(self) -> None:
        self.add_line('cup-0', (14, 6), (14, 24))
        self.add_arc('cup-1', (14, 24), (32, 42), radius_x=18, sweep=False)
        self.add_arc('cup-2', (32, 42), (50, 24), radius_x=18, sweep=False)
        self.add_line('cup-3', (50, 24), (50, 6))
        self.add_line('cup-4', (50, 6), (14, 6))
        self.add_line('handle--1-0', (14, 14), (6, 14))
        self.add_arc('handle--1-1', (6, 14), (14, 24), radius_x=8, radius_y=10, sweep=False)
        self.add_line('handle-1-0', (50, 14), (58, 14))
        self.add_arc('handle-1-1', (58, 14), (50, 24), radius_x=8, radius_y=10)
        self.add_line('stem-1', (24, 50), (32, 42))
        self.add_line('stem-2', (32, 42), (40, 50))
        self.add_line('base-1', (18, 50), (46, 50))
        self.add_line('base-2', (46, 50), (46, 58))
        self.add_line('base-3', (46, 58), (18, 58))
        self.add_line('base-4', (18, 58), (18, 50))
        self.add_contour('cup', 'cup-0', 'cup-1', 'cup-2', 'cup-3', 'cup-4', closed=True)
        self.add_contour('handle--1', 'handle--1-0', 'handle--1-1')
        self.add_contour('handle-1', 'handle-1-0', 'handle-1-1')
        self.add_contour('stem', 'stem-1', 'stem-2')
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', closed=True)
        self.relate('connect', 'cup', 'handle--1')
        self.relate('connect', 'cup', 'handle-1')
        self.relate('connect', 'stem', 'cup')
        self.relate('connect', 'base', 'stem')
