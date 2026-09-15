"""Amazon elastic container service (programing), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '56073540-29f9-5a2d-ab8b-5042184031cb'
SOURCE_PATH = 'pictographic-primitives/programing/amazon elastic container service_56073540-29f9-5a2d-ab8b-5042184031cb.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class AmazonElasticContainerService(Solo48):
    icon_id = 'amazon-elastic-container-service'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'elastic', 'container', 'service', 'programing')

    def build(self):
        self.add_line('sym-e0', (24, 44), (40, 33))
        self.add_line('sym-e1', (40, 33), (40, 13))
        self.add_line('sym-e2', (40, 13), (27, 4))
        self.add_line('sym-e3', (24, 44), (8, 33))
        self.add_line('sym-e4', (8, 33), (8, 13))
        self.add_line('sym-e5', (8, 13), (21, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5')
        self.relate('connect', 'sym-c0', 'sym-c1')
