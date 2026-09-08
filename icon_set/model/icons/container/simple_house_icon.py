"""A house-shaped enclosure has a pitched roof and rounded lower corners.

SQUARE: visible bounds (0, 0, 64, 64), chosen for the subject proportions.
Lucide house: mirrored pitched roof and rounded wall junctions; original and atomic-debug inspected.
The empty source silhouette is retained; no doorway added. Bilateral symmetry.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SimpleHouseIcon(Container64):
    icon_id = 'simple-house-icon'
    keyshape = Keyshape.SQUARE
    aliases = ('house-container',)
    keywords = ('simple', 'house', 'icon')

    def build(self) -> None:
        self.add_line('roof-right', (32, 2), (56, 20))
        self.add_arc('shoulder-right', (56, 20), (62, 32), radius_x=15, radius_y=15, sweep=True)
        self.add_line('wall-right', (62, 32), (62, 58))
        self.add_arc('base-se', (62, 58), (58, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('base', (58, 62), (6, 62))
        self.add_arc('base-sw', (6, 62), (2, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('wall-left', (2, 58), (2, 32))
        self.add_arc('shoulder-left', (2, 32), (8, 20), radius_x=15, radius_y=15, sweep=True)
        self.add_line('roof-left', (8, 20), (32, 2))
        self.add_contour('house', 'roof-right', 'shoulder-right', 'wall-right', 'base-se', 'base', 'base-sw', 'wall-left', 'shoulder-left', 'roof-left', closed=True)
