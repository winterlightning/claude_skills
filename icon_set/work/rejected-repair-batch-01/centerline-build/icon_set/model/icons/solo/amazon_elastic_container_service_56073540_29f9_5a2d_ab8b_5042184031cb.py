"""Widen the hexagon to the square envelope while retaining the original mark. Independent feedback revision; parent preserved."""
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
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'elastic', 'container', 'service', 'programing')

    def build(self):
        """Symbol plan: Widen the hexagon to the square envelope while retaining the original mark. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_line('sym-e0', (24, 42), (42, 33))
        self.add_line('sym-e1', (42, 33), (42, 15))
        self.add_line('sym-e2', (42, 15), (27, 6))
        self.add_line('sym-e3', (24, 42), (6, 33))
        self.add_line('sym-e4', (6, 33), (6, 15))
        self.add_line('sym-e5', (6, 15), (21, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3', 'sym-e4', 'sym-e5')
        self.relate('connect', 'sym-c0', 'sym-c1')
