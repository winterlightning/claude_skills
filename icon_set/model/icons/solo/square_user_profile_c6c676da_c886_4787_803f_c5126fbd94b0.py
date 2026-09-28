from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6c676da-c886-4787-803f-c5126fbd94b0'
SOURCE_PATH = 'pictographic-primitives/other/square man_c6c676da-c886-4787-803f-c5126fbd94b0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """A square profile tile containing a detached circular head and open shoulders.

    Plan: Symmetric frame radius2 centered24,24. Head center24,18 radius3; body top29 gives exact 8 centerline/4 ink gap from head bottom21. Shoulder width12 is twice head diameter6, following shared human proportions.
    References: Supplied complete profile tile; icon_set/references/human_ref/user.svg owns circular head, open smooth shoulders and 1:2 head/shoulder width ratio. Lucide square-user-round original and atoms inform rounded frame only; source detached composition retained.
    """
    icon_id = 'square-user-profile-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases = ()
    keywords = ()

    def build(self):
        axis, left, right, top, bottom, r = 24, 6, 42, 6, 42, 2
        self.add_line("top", (left+r,top), (right-r,top))
        self.add_arc("tr", (right-r,top), (right,top+r), radius_x=r)
        self.add_line("right", (right,top+r), (right,bottom-r))
        self.add_arc("br", (right,bottom-r), (right-r,bottom), radius_x=r)
        self.add_line("bottom", (right-r,bottom), (left+r,bottom))
        self.add_arc("bl", (left+r,bottom), (left,bottom-r), radius_x=r)
        self.add_line("left", (left,bottom-r), (left,top+r))
        self.add_arc("tl", (left,top+r), (left+r,top), radius_x=r)
        self.add_contour("frame", "top", "tr", "right", "br", "bottom", "bl", "left", "tl", closed=True)
        head_cy, head_r = 18, 3
        self.add_arc("head-upper", (axis-head_r,head_cy), (axis+head_r,head_cy), radius_x=head_r)
        self.add_arc("head-lower", (axis+head_r,head_cy), (axis-head_r,head_cy), radius_x=head_r)
        self.add_contour("head", "head-upper", "head-lower", closed=True)
        body_top = head_cy + head_r + 8
        self.add_arc("shoulders", (axis-6,body_top+4), (axis+6,body_top+4), radius_x=6, radius_y=4)
