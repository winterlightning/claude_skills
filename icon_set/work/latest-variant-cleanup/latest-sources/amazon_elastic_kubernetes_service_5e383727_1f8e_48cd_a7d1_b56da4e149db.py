"""Widen the hexagon to the square envelope while retaining the original mark. Independent feedback revision; parent preserved."""
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
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_02'
    aliases = ()
    keywords = ('amazon', 'elastic', 'kubernetes', 'service', '_uncategorized_02')

    def build(self):
        """Symbol plan: Widen the hexagon to the square envelope while retaining the original mark. Reference: inspected current parent; no useful exact Lucide match selected."""
        axis = 24
        left, right = (axis - 18, axis + 18)
        self.add_polyline('hexagon', (axis, 6), (right, 14), (right, 34), (axis, 42), (left, 34), (left, 14), closed=True)
        self.add_polyline('stem', (20, 16), (20, 24), (20, 32))
        self.add_polyline('arms', (28, 17), (20, 24), (28, 31))
        self.relate('connect', 'stem', 'arms')
