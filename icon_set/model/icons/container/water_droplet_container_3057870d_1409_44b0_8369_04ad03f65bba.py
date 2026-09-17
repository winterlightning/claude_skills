"""Water Droplet: independently authored container.

Construction plan: Mirrored pointed drop with two broad tangent lower arcs; no internal symbol.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg. Lucide droplet original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'pictographic-primitives/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.svg'
AUTHOR = 'gpt-6'


class WaterDropletContainer(Container64):
    icon_id = 'water-droplet-container'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('water', 'droplet', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'drop',(32,2),[('L',(16,26)),('A',(10,40),22,24,False),('A',(54,40),22,22,False),('A',(48,26),22,24,False),('L',(32,2))],True)
