"""An upright rectangular profile frame with softly rounded top corners, two long vertical sides, and no bottom edge. Exclude the avatar.

Plan: One continuous open U frame, top corner radius six; no bottom edge. Bounds (6,2)-(58,62).
Hosting at the standard slot: add-sub32: valid, heart-state-63: valid, check-mark: valid.
Construction reference: Lucide briefcase-business: tangent quarter-circle corners."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '4dfb2fe8-1589-4417-bd9c-f41f41f96d93'
SOURCE_PATH = 'pictographic-primitives/other/rectangle user_4dfb2fe8-1589-4417-bd9c-f41f41f96d93.svg'
SOURCE_ICON_IDS = ('4dfb2fe8-1589-4417-bd9c-f41f41f96d93',)
AUTHOR = 'gpt-6'

class OpenBottomProfileFrame(Container64):
    icon_id = 'open-bottom-profile-frame'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ('open', 'bottom', 'profile', 'frame')

    def build(self) -> None:
        left,right,top,bottom,r=6,58,2,62,6
        self.add_line('left',(left,bottom),(left,top+r))
        self.add_arc('top-left',(left,top+r),(left+r,top),radius_x=r)
        self.add_line('top',(left+r,top),(right-r,top))
        self.add_arc('top-right',(right-r,top),(right,top+r),radius_x=r)
        self.add_line('right',(right,top+r),(right,bottom))
        self.add_contour('frame','left','top-left','top','top-right','right')
