"""A pointed house enclosure with an empty interior. Preserves the deliberate roof corners.

Keyshape: VRECT_XL; centerline extremes recorded in build.
Construction reference: Lucide house: paired diagonal roof slopes and rounded lower corners; no added door.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-house-outline VRECT_XL -> VRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class SimpleHouseOutline(Container64):
    icon_id = 'simple-house-outline'
    keyshape = Keyshape.VRECT_L
    aliases = ('simple-upward-pointing-house',)
    keywords = ('simple', 'house', 'outline')

    def build(self) -> None:
        self.add_line('roof-1', (10, 25), (32, 4))
        self.add_line('roof-2', (32, 4), (54, 25))
        self.add_line('right', (54, 25), (54, 56))
        self.add_arc('se', (54, 56), (50, 60), radius_x=4)
        self.add_line('base', (50, 60), (14, 60))
        self.add_arc('sw', (14, 60), (10, 56), radius_x=4)
        self.add_line('left', (10, 56), (10, 25))
        self.add_contour('roof', 'roof-1', 'roof-2')
        self.add_contour('walls', 'right', 'se', 'base', 'sw', 'left')
        self.relate('connect', 'roof', 'walls')
