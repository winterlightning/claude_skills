"""A pointed house enclosure with an empty interior. Preserves the deliberate roof corners.

Keyshape: VRECT_XL; centerline extremes recorded in build.
Construction reference: Lucide house: paired diagonal roof slopes and rounded lower corners; no added door.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SimpleHouseOutline(Container64):
    icon_id = 'simple-house-outline'
    keyshape = Keyshape.VRECT_XL
    aliases = ('simple-upward-pointing-house',)
    keywords = ('simple', 'house', 'outline')

    def build(self) -> None:
        # Centerline (6,2)-(58,62).
        self.add_polyline('roof',(6,24),(32,2),(58,24))
        self.add_line('right',(58,24),(58,58))
        self.add_arc('se',(58,58),(54,62),radius_x=4)
        self.add_line('base',(54,62),(10,62))
        self.add_arc('sw',(10,62),(6,58),radius_x=4)
        self.add_line('left',(6,58),(6,24))
        self.add_contour('walls','right','se','base','sw','left')
        self.relate('connect','roof','walls')
