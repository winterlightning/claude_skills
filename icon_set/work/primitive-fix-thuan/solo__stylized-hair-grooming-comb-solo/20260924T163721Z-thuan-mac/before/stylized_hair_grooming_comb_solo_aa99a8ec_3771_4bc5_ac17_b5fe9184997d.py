"""Stylized Hair Grooming Comb. Authored directly on SOLO48 for later user-requested sub reuse.
Construction: local Lucide circle-check, triangle-alert, search, shield-plus,
smartphone and hand references inform coherent contours and shared joins.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._payments_batch01 import circle, rounded_rect
SOURCE_ICON_ID = 'aa99a8ec-3771-4bc5-ac17-b5fe9184997d'
SOURCE_PATH = 'pictographic-primitives/other/comb_aa99a8ec-3771-4bc5-ac17-b5fe9184997d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stylized-hair-grooming-comb-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    tags = ('sub icon',)
    keywords = ('sub icon', 'stylized hair grooming comb')
    def build(self):
        self.add_bezier('back',(4,40),((17,30),(30,20),(40,12)),((44,9),(44,8),(40,8)))
        self.add_line('tip',(40,8),(44,8))
        self.relate('connect','back','tip')
        self.add_line('tooth-a',(8,37),(4,31))
        self.add_line('tooth-b',(20,28),(16,22))
        self.add_line('tooth-c',(32,19),(28,13))
        for name in ('tooth-a','tooth-b','tooth-c'):self.relate('connect','back',name)
