"""Food Wrap Burrito."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5df15308-bb26-5ea4-8a8a-a4856af7eb41'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/wrap_5df15308-bb26-5ea4-8a8a-a4856af7eb41.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-topped-burrito-wrap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('wrap', 'burrito', 'tortilla', 'filling', 'sandwich', 'meal', 'food')

    def build(self):
        # Plan: Diagonal burrito with scalloped filling, long folded wrapper and open top seam. Lucide sandwich layered construction; small filling curls omitted. Exact seam nodes. Bounds (6,6)-(42,42).
        self.add_bezier('filling',(19,12),((19,8),(21,6),(24,6)),((28,6),(28,10),(30,10)),((32,10),(34,6),(36,8)),((38,10),(42,10),(42,14)),((42,16),(41,18),(40,20)))
        self.add_bezier('wrapper',(40,20),((40,21),(39,23),(38,24)),((35,31),(32,36),(28,40)),((27,42),(24,42),(22,42)),((18,42),(15,40),(14,39)),((7,36),(6,34),(6,31)),((6,27),(15,17),(19,12)))
        self.relate('connect','filling','wrapper')
        self.add_bezier('fold',(19,12),((22,16),(24,20),(24,24)),((24,30),(20,36),(14,39)));self.relate('connect','fold','wrapper');self.relate('connect','fold','filling')
        self.add_line('opening',(24,24),(38,24));self.relate('connect','opening','fold');self.relate('connect','opening','wrapper')
