"""News Article Page. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'd2ec8c43-9e6d-4059-8823-4ce004c7a076'
SOURCE_PATH = 'pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'news-article-page-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    tags = ('sub icon',)
    keywords = ('sub icon', 'news article page')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        self.add_polyline('page',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        self.add_polyline('picture',(17,17),(29,17),(29,25),(17,25),closed=True)
        self.add_line('text',(17,34),(31,34))
