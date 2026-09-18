"""Raise the lock body and use a smaller open shackle, retaining a clear opening.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class UnlockedSecurityPadlockVariant2(Container64):
    icon_id = 'unlocked-security-padlock-v2'
    variant_of = 'unlocked-security-padlock'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        rect(self,'body',6,18,58,62,5)
        path(self,'shackle',(20,18),[('L',(20,12)),('A',(40,12),10,10,True)]);join('shackle','body')
