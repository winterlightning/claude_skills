"""Broken Chain Link. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = '7fcc14bd-bf5e-41f1-97bb-f6b06da48c98'
SOURCE_PATH = 'pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broken-chain-link-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags = ('sub icon',)
    keywords = ('sub icon', 'broken chain link')
    def build(self):
        self.add_bezier('link-left',(21,33),((15,39),(13,42),(10,42)),((6,42),(6,36),(6,33)),((6,29),(9,27),(14,22)))
        self.add_bezier('link-right',(27,15),((33,9),(35,6),(38,6)),((42,6),(42,12),(42,15)),((42,19),(39,21),(34,26)))
        self.add_line('burst-a',(6,15),(9,15))
        self.add_line('burst-b',(17,6),(17,9))
