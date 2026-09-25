"""Eight Petal Star Anise."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4fb38ea-9d46-4d87-93c6-0b06d6ba7b40'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/star anise_a4fb38ea-9d46-4d87-93c6-0b06d6ba7b40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eight-point-star-anise'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('star anise', 'spice', 'pod', 'star', 'seed', 'seasoning', 'food')

    def build(self):
        # Plan: Eight pointed anise pods as one regular star silhouette. Center ring reduced to a seed dot, narrow pod seams omitted. No exact Lucide match; rotational repeated shape. Envelope (6,6)-(42,42).
        points=((24,6),(29,14),(37,11),(34,19),(42,24),(34,29),(37,37),(29,34),(24,42),(19,34),(11,37),(14,29),(6,24),(14,19),(11,11),(19,14))
        self.add_polyline('pods',*points,closed=True)
        self.add_dot('seed',(24,24))
