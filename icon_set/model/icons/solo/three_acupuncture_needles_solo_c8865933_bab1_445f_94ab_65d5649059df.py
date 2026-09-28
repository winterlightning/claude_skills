"""Three Acupuncture Needles. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'c8865933-bab1-445f-94ab-65d5649059df'
SOURCE_PATH = 'pictographic-primitives/other/needles three_c8865933-bab1-445f-94ab-65d5649059df.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-acupuncture-needles-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'three acupuncture needles')
    def build(self):
        for j,(y,end) in enumerate(((12,44),(24,26),(36,44))):
         self.add_line('needle-'+str(j),(4,y),(end-8,y))
         circle(self,'handle-'+str(j),end-4,y,4)
         self.relate('connect','needle-'+str(j),'handle-'+str(j))
