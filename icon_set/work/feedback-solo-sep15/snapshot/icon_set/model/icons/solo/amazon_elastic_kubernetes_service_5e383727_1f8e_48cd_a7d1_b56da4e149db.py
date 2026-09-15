"""amazon-elastic-kubernetes-service: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e383727-1f8e-48cd-a7d1-b56da4e149db'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon elastic kubernetes service_5e383727-1f8e-48cd-a7d1-b56da4e149db.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class AmazonElasticKubernetesService(Solo48):
    icon_id = 'amazon-elastic-kubernetes-service'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'elastic', 'kubernetes', 'service', '_uncategorized_02')

    def build(self):
        # Plan: VRECT_L (8,4)-(40,44); six clean sides mirrored around both axes; K arms share one stem node.
        # Reference: Lucide hexagon: common vertices and equal opposite sides.
        axis = 24
        left, right = axis-16, axis+16
        self.add_polyline('hexagon',(axis,4),(right,14),(right,34),(axis,44),(left,34),(left,14),closed=True)
        self.add_polyline('stem',(20,16),(20,24),(20,32))
        self.add_polyline('arms',(28,17),(20,24),(28,31))
        self.relate('connect','stem','arms')
