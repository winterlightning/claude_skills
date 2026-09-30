"""A blank paper page with a clipped upper-right fold silhouette.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide file: straight diagonal and rounded page corners; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (paper-document VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'claude-opus-5-5'


class PaperDocument(Container64):
    icon_id = 'paper-document'
    keyshape = Keyshape.VRECT_M
    aliases = ()
    keywords = ('paper', 'document')

    def build(self) -> None:
        self.add_line('page-0', (16, 4), (37, 4))
        self.add_line('page-1', (37, 4), (52, 19))
        self.add_line('page-2', (52, 19), (52, 56))
        self.add_arc('page-3', (52, 56), (48, 60), radius_x=4)
        self.add_line('page-4', (48, 60), (16, 60))
        self.add_arc('page-5', (16, 60), (12, 56), radius_x=4)
        self.add_line('page-6', (12, 56), (12, 8))
        self.add_arc('page-7', (12, 8), (16, 4), radius_x=4)
        self.add_contour('page', 'page-0', 'page-1', 'page-2', 'page-3', 'page-4', 'page-5', 'page-6', 'page-7', closed=True)
