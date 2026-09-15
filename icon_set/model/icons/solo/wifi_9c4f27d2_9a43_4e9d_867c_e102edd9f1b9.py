"""wifi: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c4f27d2-9a43-4e9d-867c-e102edd9f1b9'
SOURCE_PATH = 'pictographic-primitives/networks/wifi_9c4f27d2-9a43-4e9d-867c-e102edd9f1b9.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Wifi(Solo48):
    icon_id = 'wifi'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wifi', 'networks')

    def build(self):
        # Plan: HRECT_L; mirror each crest from one shared definition, retaining two bands.
        # Reference: Geometric repeated arcs with shared symmetry.
        def crown(name,left,edge_y,top):
            right=48-left;half=(right-left)/2
            self.add_bezier(name,(left,edge_y),((left+half*.35,edge_y-(edge_y-top)*.7),(24-half*.4,top),(24,top)),((24+half*.4,top),(right-half*.35,edge_y-(edge_y-top)*.7),(right,edge_y)))

        crown('outer',4,17,8)
        crown('inner',14,27,23)
        self.add_dot('signal',(24,40))
