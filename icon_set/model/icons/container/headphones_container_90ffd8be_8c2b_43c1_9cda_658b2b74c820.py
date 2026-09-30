"""Stereo Music Listening Headphones: independently authored container.

Construction plan: One semicircular headband connects two rounded ear cups; bilateral symmetry.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/audio/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.svg. Lucide headphones original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (headphones-container SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '90ffd8be-8c2b-43c1-9cda-658b2b74c820'
SOURCE_PATH = 'pictographic-primitives/audio/headphones_90ffd8be-8c2b-43c1-9cda-658b2b74c820.svg'
AUTHOR = 'claude-opus-5-5'


class HeadphonesContainer(Container64):
    icon_id = 'headphones-container'
    keyshape = Keyshape.SQUARE
    category = 'audio'
    categories = ('audio', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('headphones', 'container')

    def build(self) -> None:
        self.add_line('band-0', (14, 37), (13, 25))
        self.add_arc('band-1', (13, 25), (51, 25), radius_x=19)
        self.add_line('band-2', (51, 25), (50, 37))
        self.add_line('left-cup-0', (14, 37), (12, 37))
        self.add_arc('left-cup-1', (12, 37), (6, 43), radius_x=6, sweep=False)
        self.add_line('left-cup-2', (6, 43), (6, 52))
        self.add_arc('left-cup-3', (6, 52), (12, 58), radius_x=6, sweep=False)
        self.add_line('left-cup-4', (12, 58), (14, 58))
        self.add_line('left-cup-5', (14, 58), (14, 37))
        self.add_line('right-cup-0', (50, 37), (52, 37))
        self.add_arc('right-cup-1', (52, 37), (58, 43), radius_x=6)
        self.add_line('right-cup-2', (58, 43), (58, 52))
        self.add_arc('right-cup-3', (58, 52), (52, 58), radius_x=6)
        self.add_line('right-cup-4', (52, 58), (50, 58))
        self.add_line('right-cup-5', (50, 58), (50, 37))
        self.add_contour('band', 'band-0', 'band-1', 'band-2')
        self.add_contour('left-cup', 'left-cup-0', 'left-cup-1', 'left-cup-2', 'left-cup-3', 'left-cup-4', 'left-cup-5', closed=True)
        self.add_contour('right-cup', 'right-cup-0', 'right-cup-1', 'right-cup-2', 'right-cup-3', 'right-cup-4', 'right-cup-5', closed=True)
        self.relate('connect', 'band', 'left-cup')
        self.relate('connect', 'band', 'right-cup')
