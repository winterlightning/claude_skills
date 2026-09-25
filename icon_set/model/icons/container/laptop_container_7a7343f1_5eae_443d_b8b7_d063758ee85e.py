"""Personal Laptop Computer: independently authored container.

Construction plan: Rounded upright screen and flared base share the screen lower edge; no keyboard detail in source.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg. Lucide laptop original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '7a7343f1-5eae-443d-b8b7-d063758ee85e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_7a7343f1-5eae-443d-b8b7-d063758ee85e.svg'
AUTHOR = 'gpt-6'


class LaptopContainer(Container64):
    icon_id = 'laptop-container'
    category = 'computers'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('laptop', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'screen',(6,46),[('L',(6,10)),('A',(10,6),4,4,True),('L',(54,6)),('A',(58,10),4,4,True),('L',(58,46))])
        poly('base',(6,46),(58,46),(62,58),(2,58),closed=True);join('base','screen')
