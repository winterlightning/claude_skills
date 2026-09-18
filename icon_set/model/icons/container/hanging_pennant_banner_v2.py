"""Widen the banner while keeping the cord and pointed lower edge.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class HangingPennantBannerVariant2(Container64):
    icon_id = 'hanging-pennant-banner-v2'
    variant_of = 'hanging-pennant-banner'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        line('rod',(6,14),(58,14));poly('cord',(18,14),(32,2),(46,14))
        poly('banner',(10,14),(10,50),(32,62),(54,50),(54,14))
        join('rod','cord');join('rod','banner');join('cord','banner')
