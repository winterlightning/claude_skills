"""A blank paper page with a clipped upper-right fold silhouette.

VRECT_L: (8, 0, 56, 64); chosen for the source silhouette.
Lucide file: straight diagonal and rounded page corners; original and atomic-debug inspected for construction.
Source details retained; export irregularities simplified.
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class PaperDocument(Container64):
    icon_id = 'paper-document'
    keyshape = Keyshape.VRECT_L
    aliases = ()
    keywords = ('paper', 'document')

    def build(self) -> None:
        self.add_line('page-0', (14, 2), (38, 2))
        self.add_line('page-1', (38, 2), (54, 18))
        self.add_line('page-2', (54, 18), (54, 58))
        self.add_arc('page-3', (54, 58), (50, 62), radius_x=4, radius_y=4, sweep=True)
        self.add_line('page-4', (50, 62), (14, 62))
        self.add_arc('page-5', (14, 62), (10, 58), radius_x=4, radius_y=4, sweep=True)
        self.add_line('page-6', (10, 58), (10, 6))
        self.add_arc('page-7', (10, 6), (14, 2), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('page', 'page-0', 'page-1', 'page-2', 'page-3', 'page-4', 'page-5', 'page-6', 'page-7', closed=True)
