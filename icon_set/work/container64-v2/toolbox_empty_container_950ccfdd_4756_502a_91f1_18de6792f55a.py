"""A wide rectangular toolbox with softly rounded corners, a centered top handle and small stepped tabs on both upper side edges. Exclude the crossed tools.

Plan: Rounded case with a centered handle and paired upper side steps. Bounds (2,6)-(62,58).
Hosting at the standard slot: add-sub32: invalid, heart-state-63: invalid, check-mark: invalid.
Construction reference: Lucide briefcase-business: centered handle and consistent rounded case corners.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (toolbox-empty-container HRECT_XL -> HRECT_L). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = '950ccfdd-4756-502a-91f1-18de6792f55a'
SOURCE_ICON_IDS = ('950ccfdd-4756-502a-91f1-18de6792f55a',)
SOURCE_PATH = 'pictographic-primitives/other/amazon web service tools and sdk_950ccfdd-4756-502a-91f1-18de6792f55a.svg'
AUTHOR = 'claude-opus-5-5'


class ToolboxEmptyContainer(Container64):
    icon_id = 'toolbox-empty-container'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('toolbox', 'empty', 'container')

    def build(self) -> None:
        self.add_line('handle-1', (22, 18), (22, 10))
        self.add_line('handle-2', (22, 10), (42, 10))
        self.add_line('handle-3', (42, 10), (42, 18))
        self.add_line('upper-1', (8, 18), (56, 18))
        self.add_line('upper-2', (56, 18), (60, 22))
        self.add_line('upper-3', (60, 22), (60, 30))
        self.add_line('upper-4', (60, 30), (56, 30))
        self.add_line('upper-5', (56, 30), (56, 48))
        self.add_arc('corner-right', (56, 48), (48, 54), radius_x=8, radius_y=6)
        self.add_line('base', (48, 54), (16, 54))
        self.add_arc('corner-left', (16, 54), (8, 48), radius_x=8, radius_y=6)
        self.add_line('left-1', (8, 48), (8, 30))
        self.add_line('left-2', (8, 30), (4, 30))
        self.add_line('left-3', (4, 30), (4, 22))
        self.add_line('left-4', (4, 22), (8, 18))
        self.add_contour('handle', 'handle-1', 'handle-2', 'handle-3')
        self.add_contour('case', 'upper-1', 'upper-2', 'upper-3', 'upper-4', 'upper-5', 'corner-right', 'base', 'corner-left', 'left-1', 'left-2', 'left-3', 'left-4', closed=True)
        self.relate('connect', 'handle', 'case')
