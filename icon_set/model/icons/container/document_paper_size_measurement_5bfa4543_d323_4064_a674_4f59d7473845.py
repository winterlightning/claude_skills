"""Two differently sized clipped documents share a baseline above a single width marker. Common rounded page construction and cap spans are shared; intentional size difference follows the reference. Lucide files informed page contour.
Hosting probes using plus-sign-state-131, heart-state-63, check-mark: invalid, review, review. Full content occupies the slot; see batch hosting report.
Whole subject explicitly authorized by user; preserve saved family.
Keyshape: HRECT_XL; fine source details simplified only for native readability.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (document-paper-size-measurement HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '5bfa4543-d323-4064-a674-4f59d7473845'
SOURCE_PATH = 'pictographic-primitives/files/paper sizes two document measure 1_5bfa4543-d323-4064-a674-4f59d7473845.svg'
AUTHOR = 'claude-opus-5-5'


class Icon(Container64):
    icon_id = 'document-paper-size-measurement'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ('Document Paper Size Measurement',)
    keywords = ('document', 'paper', 'size', 'measurement')

    def build(self) -> None:
        self.add_line('small-upper-1', (7, 21), (19, 21))
        self.add_line('small-upper-2', (19, 21), (27, 29))
        self.add_line('small-upper-3', (27, 29), (27, 36))
        self.add_arc('small-br', (27, 36), (24, 39), radius_x=3)
        self.add_line('small-bottom', (24, 39), (7, 39))
        self.add_arc('small-bl', (7, 39), (4, 36), radius_x=3)
        self.add_line('small-left', (4, 36), (4, 24))
        self.add_arc('small-tl', (4, 24), (7, 21), radius_x=3)
        self.add_line('large-upper-1', (38, 10), (51, 10))
        self.add_line('large-upper-2', (51, 10), (60, 19))
        self.add_line('large-upper-3', (60, 19), (60, 36))
        self.add_arc('large-br', (60, 36), (57, 39), radius_x=3)
        self.add_line('large-bottom', (57, 39), (38, 39))
        self.add_arc('large-bl', (38, 39), (35, 36), radius_x=3)
        self.add_line('large-left', (35, 36), (35, 13))
        self.add_arc('large-tl', (35, 13), (38, 10), radius_x=3)
        self.add_line('dimension', (4, 50), (60, 50))
        self.add_line('cap-0-a', (4, 47), (4, 50))
        self.add_line('cap-0-b', (4, 50), (4, 54))
        self.add_line('cap-1-a', (60, 47), (60, 50))
        self.add_line('cap-1-b', (60, 50), (60, 54))
        self.add_contour('small', 'small-upper-1', 'small-upper-2', 'small-upper-3', 'small-br', 'small-bottom', 'small-bl', 'small-left', 'small-tl', closed=True)
        self.add_contour('large', 'large-upper-1', 'large-upper-2', 'large-upper-3', 'large-br', 'large-bottom', 'large-bl', 'large-left', 'large-tl', closed=True)
        self.relate('connect', 'dimension', 'cap-0-a', 'cap-0-b')
        self.relate('connect', 'dimension', 'cap-1-a', 'cap-1-b')
