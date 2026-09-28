"""Eight Petal Star Anise."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a4fb38ea-9d46-4d87-93c6-0b06d6ba7b40'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__eight-point-star-anise/20260927T135945Z-thuan-mac-1/reference/star anise_a4fb38ea-9d46-4d87-93c6-0b06d6ba7b40.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'eight-point-star-anise'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('star anise', 'spice', 'pod', 'star', 'seed', 'seasoning', 'food')

    def build(self):
        # Plan: Eight pointed anise pods as one regular star silhouette. Center ring reduced to a seed dot, narrow pod seams omitted. No exact Lucide match; rotational repeated shape. Envelope (6,6)-(42,42).
        points=((24,6),(28,15),(37,11),(33,20),(42,24),(33,28),(37,37),(28,33),(24,42),(20,33),(11,37),(15,28),(6,24),(15,20),(11,11),(20,15))
        self.add_polyline('pods',*points,closed=True)
        self.add_dot('seed',(24,24))
