"""smart: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = 'pictographic-primitives/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Smart(Solo48):
    icon_id = 'smart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('smart', 'state')

    def build(self):
        # Plan: HRECT_L; three mirrored crowns, no tiny cusp at the outer apex.
        # Reference: Geometric repeated crests.
        def crown(name,left,edge_y,top):
            right=48-left;half=(right-left)/2
            self.add_bezier(name,(left,edge_y),((left+half*.35,edge_y-(edge_y-top)*.7),(24-half*.4,top),(24,top)),((24+half*.4,top),(right-half*.35,edge_y-(edge_y-top)*.7),(right,edge_y)))

        crown('outer',4,19,8)
        crown('middle',10,30,23)
        crown('inner',18,40,37)
