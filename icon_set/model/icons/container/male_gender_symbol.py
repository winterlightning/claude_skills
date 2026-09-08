"""A male-symbol container with a circular enclosure and northeast arrow.

SQUARE: centerline extremes (2,2)-(62,62). The user explicitly confirmed
container classification. Lucide mars original and atomic-debug inform the
circular ring, separate shaft and joined arrowhead. The directional arrow
is deliberately asymmetric; all source-defining parts are retained.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class MaleGenderSymbol(Container64):
    icon_id = 'male-gender-symbol'
    keyshape = Keyshape.SQUARE
    aliases = ('mars-symbol-container',)
    keywords = ('male', 'gender', 'mars', 'circle', 'arrow')

    def build(self) -> None:
        # Radius 25 about (27,37); (42,17) is an exact 3:4:5 point.
        self.add_arc('ring-ne', (42,17), (52,37), radius_x=25)
        self.add_arc('ring-se', (52,37), (27,62), radius_x=25)
        self.add_arc('ring-sw', (27,62), (2,37), radius_x=25)
        self.add_arc('ring-nw', (2,37), (27,12), radius_x=25)
        self.add_arc('ring-top', (27,12), (42,17), radius_x=25)
        self.add_contour('ring','ring-ne','ring-se','ring-sw','ring-nw','ring-top',closed=True)
        self.add_line('shaft',(42,17),(62,2))
        self.add_polyline('head',(44,2),(62,2),(62,20))
        self.relate('connect','ring','shaft')
        self.relate('connect','shaft','head')
