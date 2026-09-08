"""A complete phone enclosure with a radiating front-camera flash. Clipped lower body is restored.

Keyshape: VRECT_L; centerline extremes recorded in build.
Construction reference: Lucide smartphone: equal body corner radii, with an open shoulder around the flash.. Mirrored about x=32.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class SmartphoneFrontCameraFlash(Container64):
    icon_id = 'smartphone-front-camera-flash'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('smartphone', 'front', 'camera', 'flash')

    def build(self) -> None:
        # Centerline (10,2)-(54,62).
        self.add_arc('shoulder-right',(48,10),(54,16),radius_x=6)
        self.add_line('right',(54,16),(54,56))
        self.add_arc('se',(54,56),(48,62),radius_x=6)
        self.add_line('base',(48,62),(16,62))
        self.add_arc('sw',(16,62),(10,56),radius_x=6)
        self.add_line('left',(10,56),(10,16))
        self.add_arc('shoulder-left',(10,16),(16,10),radius_x=6)
        self.add_contour('body','shoulder-right','right','se','base','sw','left','shoulder-left')
        self.add_line('divider',(10,26),(54,26))
        self.relate('connect','divider','body')
        self.add_dot('camera',(32,17))
        self.add_line('ray-top',(32,2),(32,6))
        self.add_line('ray-left',(21,3),(24,6))
        self.add_line('ray-right',(43,3),(40,6))
        self.add_line('ray-west',(19,17),(23,17))
        self.add_line('ray-east',(41,17),(45,17))
