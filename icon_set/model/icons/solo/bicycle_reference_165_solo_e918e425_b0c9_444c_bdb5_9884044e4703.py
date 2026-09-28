"""Simple Bicycle Icon. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.
Two equal wheels, shared frame junctions and opposing seat/handlebar ends.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'e918e425-b0c9-444c-bdb5-9884044e4703'
SOURCE_PATH = 'pictographic-primitives/other/bike_e918e425-b0c9-444c-bdb5-9884044e4703.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bicycle-reference-165-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'simple bicycle icon')
    def build(self):
        # Compact equal wheels and elevated diamond frame; forks meet wheel tops.
        circle(self,'rear-wheel',12,36,6)
        circle(self,'front-wheel',36,36,6)
        self.add_polyline('frame',(18,14),(30,14),(24,26),(18,14))
        self.add_line('rear-fork',(18,14),(12,30))
        self.add_line('front-fork',(30,14),(36,30))
        self.add_line('seat-post',(18,6),(18,14))
        self.add_line('seat',(14,6),(22,6))
        self.add_polyline('handlebar',(30,14),(28,6),(36,6))
        self.relate('connect','rear-wheel','rear-fork')
        self.relate('connect','front-wheel','front-fork')
        self.relate('connect','frame','rear-fork','front-fork','seat-post','handlebar')
        self.relate('connect','seat-post','seat')
