"""Four rounded corner brackets enclose a camera focus area. No central mark added.

Keyshape: SQUARE; centerline extremes recorded in build.
Construction reference: Lucide scan: four matching line-arc-line corner contours.. Mirrored about x=32.
Hosting measured with compose.py: plus valid, heart valid, check valid.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SquareCameraFocusViewfinder(Container64):
    icon_id = 'square-camera-focus-viewfinder'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('square', 'camera', 'focus', 'viewfinder')

    def build(self) -> None:
        # Centerline (2,2)-(62,62).
        for name,sx,sy in (('nw',1,1),('ne',-1,1),('se',-1,-1),('sw',1,-1)):
            def p(x,y):
                return (32+sx*(x-32),32+sy*(y-32))
            self.add_line(name+'-vertical',p(2,20),p(2,8))
            self.add_arc(name+'-corner',p(2,8),p(8,2),radius_x=6,sweep=(sx*sy>0))
            self.add_line(name+'-horizontal',p(8,2),p(20,2))
            self.add_contour(name,name+'-vertical',name+'-corner',name+'-horizontal')
