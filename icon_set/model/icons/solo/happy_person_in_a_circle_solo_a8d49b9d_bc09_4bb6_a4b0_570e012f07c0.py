"""Happy Person in a Circle. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'a8d49b9d-bc09-4bb6-a4b0-570e012f07c0'
SOURCE_PATH = 'pictographic-primitives/other/person_a8d49b9d-bc09-4bb6-a4b0-570e012f07c0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'happy-person-in-a-circle-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'happy person in a circle')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'outline',24,24,20)
        circle(self,'head',24,18,4)
        self.add_bezier('arms',(15,27),((20,31),(28,31),(33,27)))
        self.add_line('torso',(24,30),(24,35))
        self.relate('connect','arms','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
