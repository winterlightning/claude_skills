"""A tapered electric stove with a control band and inset base.

SQUARE: exact centerline extremes recorded in build.
Construction: Lucide smartphone, repeated rounded enclosure corners; tapered appliance silhouette comes from the supplied source. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class ElectricCookingStove(Container64):
    icon_id = 'electric-cooking-stove'
    keyshape = Keyshape.SQUARE
    aliases = ('modern-electric-cooking-stove',)
    keywords = ('electric', 'cooking', 'stove')

    def build(self) -> None:
        # Centerline (2,2)-(62,62).
        self.add_line('top',(14,2),(50,2))
        self.add_arc('ne',(50,2),(56,8),radius_x=6)
        self.add_line('taper-right',(56,8),(62,38))
        self.add_line('side-right',(62,38),(62,48))
        self.add_arc('se',(62,48),(56,54),radius_x=6)
        self.add_line('bottom',(56,54),(8,54))
        self.add_arc('sw',(8,54),(2,48),radius_x=6)
        self.add_line('side-left',(2,48),(2,38))
        self.add_line('taper-left',(2,38),(8,8))
        self.add_arc('nw',(8,8),(14,2),radius_x=6)
        self.add_contour('outline','top','ne','taper-right','side-right','se','bottom','sw','side-left','taper-left','nw',closed=True)
        self.add_line('divider',(2,38),(62,38))
        self.relate('connect','divider','outline')
        self.add_polyline('base',(8,54),(12,62),(52,62),(56,54))
        self.relate('connect','base','outline')
        self.add_line('control-left',(20,45),(20,47))
        self.add_line('control-right',(44,45),(44,47))
