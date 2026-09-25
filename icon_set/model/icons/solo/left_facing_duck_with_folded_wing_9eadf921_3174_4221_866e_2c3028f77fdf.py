"""Left-facing duck with flat bill, curved neck, broad body and folded wing. HRECT_L x4..44 y8..40. Source supplies silhouette; Lucide bird teaches a continuous perimeter with wing attached at genuine endpoints. Eye omitted for open head."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '9eadf921-3174-4221-866e-2c3028f77fdf'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/drake_9eadf921-3174-4221-866e-2c3028f77fdf.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'left-facing-duck-with-folded-wing'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Left Facing Duck with Folded Wing']
    keywords = ['duck', 'bird', 'bill', 'wing', 'waterfowl', 'animal', 'tail']
    def build(self):
        self.add_bezier('head',(12,16),((12,8),(16,8),(20,8)),((29,8),(27,19),(26,24)))
        self.add_bezier('back',(26,24),((32,22),(38,28),(44,26)))
        self.add_bezier('belly',(44,26),((42,37),(36,40),(24,40)),((12,40),(6,40),(6,32)),((6,28),(16,28),(16,26)),((16,24),(8,24),(4,24)))
        self.add_line('bill-tip',(4,24),(4,16))
        self.add_line('bill-top',(4,16),(12,16))
        self.add_contour('duck','head','back','belly','bill-tip','bill-top',closed=True)
        self.add_bezier('wing',(26,24),((24,28),(24,31),(30,31)),((35,31),(40,31),(44,26)))
        self.relate('connect','duck','wing')
