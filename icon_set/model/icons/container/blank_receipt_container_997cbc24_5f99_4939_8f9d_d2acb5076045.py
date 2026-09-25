"""Simple Paper Receipt: independently authored container.

Construction plan: Blank vertical receipt with repeating equal tear teeth at both ends; no currency text.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shopping/receipt_997cbc24-5f99-4939-8f9d-d2acb5076045.svg. Lucide receipt original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '997cbc24-5f99-4939-8f9d-d2acb5076045'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt_997cbc24-5f99-4939-8f9d-d2acb5076045.svg'
AUTHOR = 'gpt-6'


class BlankReceiptContainer(Container64):
    icon_id = 'blank-receipt-container'
    category = 'shopping'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('blank', 'receipt', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        points=[(10,2)]+[(x,2 if i%2==0 else 8) for i,x in enumerate(range(10,55,11))][1:]+[(54,62)]+[(x,62 if i%2==0 else 56) for i,x in enumerate(range(54,9,-11))][1:]
        poly('receipt',*points,closed=True)
