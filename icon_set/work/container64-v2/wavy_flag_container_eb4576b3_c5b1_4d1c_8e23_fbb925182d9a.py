"""Simple Wavy Flag: independently authored container.

Construction plan: Two matching smooth wave edges joined by upright sides; no pole beyond the source flag.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/social/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.svg. Lucide flag original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (wavy-flag-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'eb4576b3-c5b1-4d1c-8e23-fbb925182d9a'
SOURCE_PATH = 'pictographic-primitives/social/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.svg'
AUTHOR = 'claude-opus-5-5'


class WavyFlagContainer(Container64):
    icon_id = 'wavy-flag-container'
    keyshape = Keyshape.HRECT_L
    category = 'social'
    categories = ('social', 'primitives')
    aliases = ()
    keywords = ('wavy', 'flag', 'container')

    def build(self) -> None:
        self.add_arc('flag-0', (4, 14), (32, 14), radius_x=14, radius_y=4)
        self.add_arc('flag-1', (32, 14), (60, 14), radius_x=14, radius_y=4, sweep=False)
        self.add_line('flag-2', (60, 14), (60, 50))
        self.add_arc('flag-3', (60, 50), (32, 50), radius_x=14, radius_y=4)
        self.add_arc('flag-4', (32, 50), (4, 50), radius_x=14, radius_y=4, sweep=False)
        self.add_line('flag-5', (4, 50), (4, 14))
        self.add_contour('flag', 'flag-0', 'flag-1', 'flag-2', 'flag-3', 'flag-4', 'flag-5', closed=True)
