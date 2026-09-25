"""Magnifying Glass with Circular Arrows: independently authored container.

Construction plan: A magnifying handle attaches to an open circular pair of refresh arrows; preserve the two directional heads.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg. Lucide refresh-cw original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'cddee393-b2d9-4824-86a6-013321aa73e8'
SOURCE_PATH = 'pictographic-primitives/business/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg'
AUTHOR = 'gpt-6'


class RefreshMagnifierContainer(Container64):
    icon_id = 'refresh-magnifier-container'
    category = 'business'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('refresh', 'magnifier', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'upper',(7,42),[('A',(2,27),25,25,True),('A',(27,2),25,25,True)])
        poly('upper-head',(19,2),(27,2),(25,10));join('upper','upper-head')
        path(self,'lower',(47,12),[('A',(52,27),25,25,True),('A',(42,47),25,25,True),('A',(27,52),25,25,True)])
        poly('lower-head',(35,52),(27,52),(29,44));join('lower','lower-head')
        line('handle',(42,47),(62,62));join('handle','lower')
