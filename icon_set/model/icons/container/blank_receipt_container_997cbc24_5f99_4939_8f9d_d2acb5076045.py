"""Simple Paper Receipt: independently authored container.

Construction plan: Blank vertical receipt with repeating equal tear teeth at both ends; no currency text.
Keyshape VRECT_L; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/shopping/receipt_997cbc24-5f99-4939-8f9d-d2acb5076045.svg. Lucide receipt original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (8, 0, 56, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (blank-receipt-container VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '997cbc24-5f99-4939-8f9d-d2acb5076045'
SOURCE_PATH = 'pictographic-primitives/shopping/receipt_997cbc24-5f99-4939-8f9d-d2acb5076045.svg'
AUTHOR = 'claude-opus-5-5'


class BlankReceiptContainer(Container64):
    icon_id = 'blank-receipt-container'
    keyshape = Keyshape.VRECT_M
    category = 'shopping'
    categories = ('shopping', 'primitives')
    aliases = ()
    keywords = ('blank', 'receipt', 'container')

    def build(self) -> None:
        self.add_line('receipt-1', (12, 4), (22, 10))
        self.add_line('receipt-2', (22, 10), (32, 4))
        self.add_line('receipt-3', (32, 4), (42, 10))
        self.add_line('receipt-4', (42, 10), (52, 4))
        self.add_line('receipt-5', (52, 4), (52, 60))
        self.add_line('receipt-6', (52, 60), (42, 54))
        self.add_line('receipt-7', (42, 54), (32, 60))
        self.add_line('receipt-8', (32, 60), (22, 54))
        self.add_line('receipt-9', (22, 54), (12, 60))
        self.add_line('receipt-10', (12, 60), (12, 4))
        self.add_contour('receipt', 'receipt-1', 'receipt-2', 'receipt-3', 'receipt-4', 'receipt-5', 'receipt-6', 'receipt-7', 'receipt-8', 'receipt-9', 'receipt-10', closed=True)
