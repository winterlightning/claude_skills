"""A cell membrane with rounded lobes enclosing an empty interior.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: cloud: coherent circular lobes and deliberate scallop junctions; symmetric membrane outline. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class WhiteBloodCell(Container64):
    icon_id = 'white-blood-cell'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('white', 'blood', 'cell')

    def build(self) -> None:
        self.add_arc('membrane-0', (17, 12), (47, 12), radius_x=15, radius_y=10, sweep=True)
        self.add_arc('membrane-1', (47, 12), (58, 26), radius_x=11, radius_y=14, sweep=True)
        self.add_arc('membrane-2', (58, 26), (62, 36), radius_x=4, radius_y=10, sweep=True)
        self.add_arc('membrane-3', (62, 36), (54, 46), radius_x=8, radius_y=10, sweep=True)
        self.add_arc('membrane-4', (54, 46), (40, 56), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('membrane-5', (40, 56), (24, 56), radius_x=8, radius_y=6, sweep=True)
        self.add_arc('membrane-6', (24, 56), (10, 46), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('membrane-7', (10, 46), (2, 36), radius_x=8, radius_y=10, sweep=True)
        self.add_arc('membrane-8', (2, 36), (6, 26), radius_x=4, radius_y=10, sweep=True)
        self.add_arc('membrane-9', (6, 26), (17, 12), radius_x=11, radius_y=14, sweep=True)
        self.add_contour('membrane', 'membrane-0', 'membrane-1', 'membrane-2', 'membrane-3', 'membrane-4', 'membrane-5', 'membrane-6', 'membrane-7', 'membrane-8', 'membrane-9', closed=True)
