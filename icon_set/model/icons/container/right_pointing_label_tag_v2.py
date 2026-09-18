"""Increase tag height while retaining its pointed right end.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class RightPointingLabelTagVariant2(Container64):
    icon_id = 'right-pointing-label-tag-v2'
    variant_of = 'right-pointing-label-tag'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'outline',(7,6),[('L',(44,6)),('L',(62,32)),('L',(44,58)),('L',(7,58)),('A',(2,53),5,5,True),('L',(2,11)),('A',(7,6),5,5,True)],True)
