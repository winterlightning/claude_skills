"""Simple Monthly Calendar. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'a86ac0fa-cb10-444a-8f9c-cea48309d64f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/calendar_a86ac0fa-cb10-444a-8f9c-cea48309d64f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'simple-monthly-calendar-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    tags = ('sub icon',)
    keywords = ('sub icon', 'simple monthly calendar')
    def build(self):
        # Plan: Complete reference subject; shared named joins; direct 48px geometry.
        rounded_rect(self,'calendar',6,12,42,42,4)
        for x in (15,33):
         self.add_line('binding-'+str(x),(x,6),(x,16))
         self.relate('connect','calendar','binding-'+str(x))
        self.add_line('header',(6,24),(42,24))
        self.relate('connect','calendar','header')
