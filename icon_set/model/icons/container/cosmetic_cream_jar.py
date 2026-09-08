"""A rounded cosmetic jar with a narrower screw lid.

Keyshape SQUARE: chosen for the reference silhouette.
Lucide square-dashed: tangent quarter-circle corners; rebuilt on the integer CONTAINER64 grid.
Source details retained unless noted in the batch review.
Hosting (compose.py): plus valid, heart does not fit, check does not fit.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class CosmeticCreamJar(Container64):
    icon_id = 'cosmetic-cream-jar'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('cosmetic', 'cream', 'jar')

    def build(self) -> None:
        self.add_line('jar-0', (12, 18), (52, 18))
        self.add_arc('jar-1', (52, 18), (62, 28), radius_x=10, radius_y=10, sweep=True)
        self.add_line('jar-2', (62, 28), (62, 52))
        self.add_arc('jar-3', (62, 52), (52, 62), radius_x=10, radius_y=10, sweep=True)
        self.add_line('jar-4', (52, 62), (12, 62))
        self.add_arc('jar-5', (12, 62), (2, 52), radius_x=10, radius_y=10, sweep=True)
        self.add_line('jar-6', (2, 52), (2, 28))
        self.add_arc('jar-7', (2, 28), (12, 18), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('jar', 'jar-0', 'jar-1', 'jar-2', 'jar-3', 'jar-4', 'jar-5', 'jar-6', 'jar-7', closed=True)
        self.add_line('lid-left', (12, 18), (12, 6))
        self.add_arc('lid-nw', (12, 6), (16, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_line('lid-top', (16, 2), (48, 2))
        self.add_arc('lid-ne', (48, 2), (52, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_line('lid-right', (52, 6), (52, 18))
        self.add_contour('lid', 'lid-left', 'lid-nw', 'lid-top', 'lid-ne', 'lid-right', closed=False)
        self.relate("connect", 'lid', 'jar')
