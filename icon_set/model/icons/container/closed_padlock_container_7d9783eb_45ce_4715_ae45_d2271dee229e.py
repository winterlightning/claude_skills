"""Raise the body top and shorten the shackle while keeping the closed lock.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '7d9783eb-45ce-4715-ae45-d2271dee229e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/lock_7d9783eb-45ce-4715-ae45-d2271dee229e.svg'
AUTHOR = 'gpt-6'

class ClosedPadlockContainer(Container64):
    icon_id = 'closed-padlock-container'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'body',6,18,58,62,5)
        path(self,'shackle',(20,18),[('L',(20,14)),('A',(44,14),12,12,True),('L',(44,18))]);join('shackle','body')
