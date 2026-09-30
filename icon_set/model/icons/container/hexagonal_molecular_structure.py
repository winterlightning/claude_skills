"""A wider hexagonal molecular enclosure with three alternating ring nodes.

SQUARE: centerline (2,2)-(62,62), visible (0,0)-(64,64). The wider keyshape
increases the bond-side separation from 38 to 46 while preserving the height
and all three radius-7 nodes. Lucide hexagon informs vertical sides and
mirrored diagonal bonds. No defining detail is removed; no asymmetry added.
The brief's archived v2 SVG matches revision 91e996c033918f6c36c1044a8bd8198910aaccdd7fc4bf36d82c7fc976ea82ef;
The accepted wider drawing now replaces the original registered icon.
Hosting measured with compose.py: check valid; plus and heart invalid because the top ring crowds the child.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (hexagonal-molecular-structure SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
FEEDBACK_PATHS = ('/Users/jakesdev/Downloads/feedback-briefs 2/container/155-container-hexagonal-molecular-structure-v2.md',)
AUTHOR = 'claude-opus-5-5'


class HexagonalMolecularStructure(Container64):
    icon_id = 'hexagonal-molecular-structure'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('hexagonal', 'molecular', 'structure', 'wide')

    def build(self) -> None:
        self.add_arc('top-0', (26, 12), (32, 6), radius_x=6)
        self.add_arc('top-1', (32, 6), (38, 12), radius_x=6)
        self.add_arc('top-2', (38, 12), (32, 18), radius_x=6)
        self.add_arc('top-3', (32, 18), (26, 12), radius_x=6)
        self.add_arc('left-0', (6, 42), (12, 36), radius_x=6)
        self.add_arc('left-1', (12, 36), (18, 42), radius_x=6)
        self.add_arc('left-2', (18, 42), (12, 48), radius_x=6)
        self.add_arc('left-3', (12, 48), (6, 42), radius_x=6)
        self.add_arc('right-0', (46, 42), (52, 36), radius_x=6)
        self.add_arc('right-1', (52, 36), (58, 42), radius_x=6)
        self.add_arc('right-2', (58, 42), (52, 48), radius_x=6)
        self.add_arc('right-3', (52, 48), (46, 42), radius_x=6)
        self.add_line('upper-left-1', (26, 12), (12, 23))
        self.add_line('upper-left-2', (12, 23), (12, 36))
        self.add_line('upper-right-1', (38, 12), (52, 23))
        self.add_line('upper-right-2', (52, 23), (52, 36))
        self.add_line('bottom-1', (12, 48), (32, 58))
        self.add_line('bottom-2', (32, 58), (52, 48))
        self.add_contour('top', 'top-0', 'top-1', 'top-2', 'top-3', closed=True)
        self.add_contour('left', 'left-0', 'left-1', 'left-2', 'left-3', closed=True)
        self.add_contour('right', 'right-0', 'right-1', 'right-2', 'right-3', closed=True)
        self.add_contour('upper-left', 'upper-left-1', 'upper-left-2')
        self.add_contour('upper-right', 'upper-right-1', 'upper-right-2')
        self.add_contour('bottom', 'bottom-1', 'bottom-2')
        self.relate('connect', 'top', 'upper-left')
        self.relate('connect', 'left', 'upper-left')
        self.relate('connect', 'top', 'upper-right')
        self.relate('connect', 'right', 'upper-right')
        self.relate('connect', 'left', 'bottom')
        self.relate('connect', 'right', 'bottom')
