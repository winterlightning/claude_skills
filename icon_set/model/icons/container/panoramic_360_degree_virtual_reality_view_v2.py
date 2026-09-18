"""Narrow the folded side panels while retaining the curved panoramic outline.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class Panoramic360DegreeVirtualRealityViewVariant2(Container64):
    icon_id = 'panoramic-360-degree-virtual-reality-view-v2'
    variant_of = 'panoramic-360-degree-virtual-reality-view'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'outline',(2,16),[('A',(62,16),30,10,True),('L',(62,48)),('A',(2,48),30,10,True),('L',(2,16))],True)
        poly('panel-left',(2,16),(10,20),(10,55));poly('panel-right',(62,16),(54,20),(54,55));join('panel-left','outline');join('panel-right','outline')
