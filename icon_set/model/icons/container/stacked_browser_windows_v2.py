"""Remove the secondary header divider while retaining its indicator and the rear window.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class StackedBrowserWindowsVariant2(Container64):
    icon_id = 'stacked-browser-windows-v2'
    variant_of = 'stacked-browser-windows'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'front',10,2,62,52,6)
        line('indicator',(20,10),(24,10))
        path(self,'back',(10,14),[('L',(8,14)),('A',(2,20),6,6,False),('L',(2,56)),('A',(8,62),6,6,False),('L',(46,62)),('A',(52,56),6,6,False),('L',(52,52))]);join('back','front')
