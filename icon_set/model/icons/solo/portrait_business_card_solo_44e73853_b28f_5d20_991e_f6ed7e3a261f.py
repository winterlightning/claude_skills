"""Portrait business card.

Construction reference: human_ref/user.svg.
Head-to-shoulder ink gap exactly 4; shoulder base left open to preserve small portrait.
SOLO48 explicitly requested for this source main by the user.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
from ._side_main50_geometry import box, circle, path

SOURCE_ICON_ID = '44e73853-b28f-5d20-991e-f6ed7e3a261f'
SOURCE_PATH = 'pictographic-primitives/office/business card_44e73853-b28f-5d20-991e-f6ed7e3a261f.svg'
AUTHOR = 'gpt-6'


class SourceMain(Solo48):
    icon_id = 'portrait-business-card-solo-44e73853'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ('portrait-business-card',)
    keywords = ('portrait', 'business', 'card')

    def build(self):
        # Portrait and info line sit within a broad rounded card.
        box(self,'card',4,8,44,40,4)
        circle(self,'head',16,19,2)
        path(self,'shoulders',(13,31),[('A',(16,29),3,2,True),('A',(19,31),3,2,True)])
        self.add_line('info',(29,22),(35,22))
