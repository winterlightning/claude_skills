"""A circular enclosure made of eight separated curved dashes.

Keyshape CIRCLE: chosen for the reference silhouette.
Lucide circle-dashed: separated arcs around a shared center; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class DashedCircleShape(Container64):
    icon_id = 'dashed-circle-shape'
    keyshape = Keyshape.CIRCLE
    aliases = ()
    keywords = ('dashed', 'circle', 'shape')

    def build(self) -> None:
        self.add_arc('cardinal-0', (25, 3), (39, 3), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('diagonal-0', (48, 7), (57, 16), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('cardinal-1', (61, 25), (61, 39), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('diagonal-1', (57, 48), (48, 57), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('cardinal-2', (39, 61), (25, 61), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('diagonal-2', (16, 57), (7, 48), radius_x=30, radius_y=30, sweep=True)
        self.add_arc('cardinal-3', (3, 39), (3, 25), radius_x=25, radius_y=25, sweep=True)
        self.add_arc('diagonal-3', (7, 16), (16, 7), radius_x=30, radius_y=30, sweep=True)
