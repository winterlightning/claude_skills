"""wifi-networks: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7c0d52e-b021-59e3-b8ec-b0ebdccb7598'
SOURCE_PATH = 'pictographic-primitives/networks/wifi_b7c0d52e-b021-59e3-b8ec-b0ebdccb7598.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WifiNetworks(Solo48):
    icon_id = 'wifi-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('wifi', 'networks')

    def build(self):
        # Plan: HRECT_L; three coherent mirrored crests with evenly separated apices.
        # Reference: Geometric repeated arcs with shared symmetry.
        def crown(name,left,edge_y,top):
            right=48-left;half=(right-left)/2
            self.add_bezier(name,(left,edge_y),((left+half*.35,edge_y-(edge_y-top)*.7),(24-half*.4,top),(24,top)),((24+half*.4,top),(right-half*.35,edge_y-(edge_y-top)*.7),(right,edge_y)))

        crown('outer',4,16,8)
        crown('middle',10,24,18)
        crown('inner',17,31,28)
        self.add_dot('signal',(24,40))
