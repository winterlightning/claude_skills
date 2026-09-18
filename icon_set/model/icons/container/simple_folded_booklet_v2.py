"""Widen the front cover while retaining the sloping rear cover.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class SimpleFoldedBookletVariant2(Container64):
    icon_id = 'simple-folded-booklet-v2'
    variant_of = 'simple-folded-booklet'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('front',(6,14),(58,14),(58,62),(6,62),closed=True)
        poly('rear',(6,14),(54,2),(54,14));join('front','rear')
