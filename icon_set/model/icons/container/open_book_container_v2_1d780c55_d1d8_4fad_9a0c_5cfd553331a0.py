"""Give the right page more width, keeping a narrower visible left page and curved binding.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '1d780c55-d1d8-4fad-9a0c-5cfd553331a0'
SOURCE_PATH = 'pictographic-primitives/content/book open 1_1d780c55-d1d8-4fad-9a0c-5cfd553331a0.svg'
AUTHOR = 'gpt-6'

class OpenBookContainerVariant2(Container64):
    icon_id = 'open-book-container-v2'
    variant_of = 'open-book-container'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'outline',(2,6),[('A',(20,12),18,6,True),('A',(62,6),42,6,True),('L',(62,52)),('A',(20,58),42,6,False),('A',(2,52),18,6,False),('L',(2,6))],True)
        line('spine',(20,12),(20,58));join('spine','outline')
