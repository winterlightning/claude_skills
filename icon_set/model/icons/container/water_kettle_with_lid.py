"""A lidded kettle with a pouring spout and a loop handle.

Keyshape SQUARE, bounds (0, 0, 64, 64): chosen for the reference proportions.
Lucide construction: cooking-pot: joined rim, vessel and lid; asymmetric spout and handle retained. Independently authored on CONTAINER64.
Essential reference features retained.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class WaterKettleWithLid(Container64):
    icon_id = 'water-kettle-with-lid'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('water', 'kettle', 'with', 'lid')

    def build(self) -> None:
        self.add_line('body-0', (2, 16), (36, 16))
        self.add_arc('body-1', (36, 16), (52, 32), radius_x=20, radius_y=40, sweep=True)
        self.add_arc('body-2', (52, 32), (56, 56), radius_x=20, radius_y=40, sweep=True)
        self.add_arc('body-3', (56, 56), (50, 62), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-4', (50, 62), (8, 62))
        self.add_arc('body-5', (8, 62), (2, 56), radius_x=6, radius_y=6, sweep=True)
        self.add_line('body-6', (2, 56), (6, 28))
        self.add_line('body-7', (6, 28), (2, 16))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_arc('lid-0', (12, 16), (24, 4), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('lid-1', (24, 4), (36, 16), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('lid', 'lid-0', 'lid-1', closed=False)
        self.relate("connect", 'body', 'lid')
        self.add_line('knob', (24, 2), (24, 4))
        self.relate("connect", 'knob', 'lid')
        self.add_line('handle-0', (36, 16), (50, 16))
        self.add_arc('handle-1', (50, 16), (62, 24), radius_x=12, radius_y=8, sweep=True)
        self.add_arc('handle-2', (62, 24), (52, 32), radius_x=10, radius_y=8, sweep=True)
        self.add_contour('handle', 'handle-0', 'handle-1', 'handle-2', closed=False)
        self.relate("connect", 'body', 'handle')
        self.relate("connect", 'lid', 'handle')
