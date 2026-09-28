"""Male Gender Symbol with Slash. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'cd720f08-5370-4624-9fe2-6fecc239b148'
SOURCE_PATH = 'pictographic-primitives/pets/male stablization_cd720f08-5370-4624-9fe2-6fecc239b148.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'male-gender-symbol-with-slash-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    tags = ('sub icon',)
    keywords = ('sub icon', 'male gender symbol with slash')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        circle(self,'ring',20,28,14)
        self.add_line('arrow',(30,18),(42,6))
        self.add_polyline('head',(31,6),(42,6),(42,17))
        self.add_line('slash',(6,6),(42,42))
        self.relate('connect','arrow','head','ring')
        self.relate('connect','slash','ring')
