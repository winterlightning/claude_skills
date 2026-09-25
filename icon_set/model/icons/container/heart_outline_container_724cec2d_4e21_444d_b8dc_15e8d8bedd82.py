"""Simple Heart Symbol: independently authored container.

Construction plan: Two circular lobes flow into broad lower shoulders and a central pointed base; symmetric enclosure.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg. Lucide heart original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus does not clear, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '724cec2d-4e21-444d-b8dc-15e8d8bedd82'
SOURCE_PATH = 'pictographic-primitives/romance/heart_724cec2d-4e21-444d-b8dc-15e8d8bedd82.svg'
AUTHOR = 'gpt-6'


class HeartOutlineContainer(Container64):
    icon_id = 'heart-outline-container'
    category = 'romance'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('heart', 'outline', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'heart',(32,14),[('A',(18,6),14,8,False),('A',(2,22),16,16,False),('A',(10,38),20,20,False),('L',(32,58)),('L',(54,38)),('A',(62,22),20,20,False),('A',(46,6),16,16,False),('A',(32,14),14,8,False)],True)
