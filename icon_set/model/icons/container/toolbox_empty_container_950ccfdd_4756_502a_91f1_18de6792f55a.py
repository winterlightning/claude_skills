"""A wide rectangular toolbox with softly rounded corners, a centered top handle and small stepped tabs on both upper side edges. Exclude the crossed tools.

Plan: Rounded case with a centered handle and paired upper side steps. Bounds (2,6)-(62,58).
Hosting at the standard slot: add-sub32: invalid, heart-state-63: invalid, check-mark: invalid.
Construction reference: Lucide briefcase-business: centered handle and consistent rounded case corners."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '950ccfdd-4756-502a-91f1-18de6792f55a'
SOURCE_PATH = 'pictographic-primitives/other/amazon web service tools and sdk_950ccfdd-4756-502a-91f1-18de6792f55a.svg'
SOURCE_ICON_IDS = ('950ccfdd-4756-502a-91f1-18de6792f55a',)
AUTHOR = 'gpt-6'

class ToolboxEmptyContainer(Container64):
    icon_id = 'toolbox-empty-container'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('toolbox', 'empty', 'container')

    def build(self) -> None:
        self.add_polyline('handle',(20,16),(20,6),(44,6),(44,16))
        self.add_polyline('upper',(6,16),(58,16),(62,20),(62,30),(58,30),(58,50))
        self.add_arc('corner-right',(58,50),(50,58),radius_x=8)
        self.add_line('base',(50,58),(14,58))
        self.add_arc('corner-left',(14,58),(6,50),radius_x=8)
        self.add_polyline('left',(6,50),(6,30),(2,30),(2,20),(6,16))
        self.add_contour('case',*[f'upper-{i}' for i in range(1,6)],'corner-right','base','corner-left',*[f'left-{i}' for i in range(1,5)],closed=True)
        # The polylines above already own contours; retain their connected parts instead.
        self.contours=[c for c in self.contours if c.contour_id not in ('upper','left')]
        self.relate('connect','handle','case')
