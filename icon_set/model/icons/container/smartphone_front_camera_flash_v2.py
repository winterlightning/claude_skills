"""Move the camera band upward, keeping the lens and flash rays.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class SmartphoneFrontCameraFlashVariant2(Container64):
    icon_id = 'smartphone-front-camera-flash-v2'
    variant_of = 'smartphone-front-camera-flash'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'body',(48,10),[('A',(54,16),6,6,True),('L',(54,56)),('A',(48,62),6,6,True),('L',(16,62)),('A',(10,56),6,6,True),('L',(10,16)),('A',(16,10),6,6,True)])
        line('divider',(10,20),(54,20));join('divider','body');self.add_dot('camera',(32,12))
        line('ray-top',(32,2),(32,4));line('ray-left',(21,2),(23,4));line('ray-right',(43,2),(41,4));line('ray-west',(22,12),(24,12));line('ray-east',(40,12),(42,12))
