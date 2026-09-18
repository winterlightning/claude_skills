"""Raise the factory roof and shorten the twin smokestacks to deepen the main building.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class IndustrialFactoryWithSmokestacksVariant2(Container64):
    icon_id = 'industrial-factory-with-smokestacks-v2'
    variant_of = 'industrial-factory-with-smokestacks'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('building',(2,62),(2,18),(18,18),(32,10),(46,18),(62,18),(62,62),closed=True)
        poly('stack-left',(4,18),(6,2),(14,2),(18,18));poly('stack-right',(46,18),(50,2),(58,2),(60,18))
        join('building','stack-left');join('building','stack-right')
