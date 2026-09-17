"""Closed Security Padlock: independently authored container.

Construction plan: Rounded lock body and semicircular shackle, centered on a shared axis; no keyhole in source.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/lock_7d9783eb-45ce-4715-ae45-d2271dee229e.svg. Lucide lock original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
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
    keywords = ('closed', 'padlock', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'body',6,26,58,62,5)
        path(self,'shackle',(16,26),[('L',(16,18)),('A',(48,18),16,16,True),('L',(48,26))]);join('shackle','body')
