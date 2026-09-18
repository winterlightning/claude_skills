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
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'simple bicycle icon')
    def build(self):
        # Plan: Two equal wheels, shared frame junctions and opposing seat/handlebar ends.
        circle(self,'rear-wheel',12,32,8)
        circle(self,'front-wheel',36,32,8)
        self.add_polyline('frame',(12,32),(22,32),(18,17),(12,32))
        self.add_polyline('top-tube',(18,17),(31,17),(22,32))
        self.add_polyline('fork',(36,32),(31,17),(28,8),(34,8))
        self.add_polyline('seat',(16,8),(22,8))
        self.add_line('seat-post',(19,8),(18,17))
        self.relate('connect','frame','top-tube','fork','seat-post')
        self.relate('connect','seat-post','seat')
        self.relate('connect','rear-wheel','frame')
        self.relate('connect','front-wheel','fork')
