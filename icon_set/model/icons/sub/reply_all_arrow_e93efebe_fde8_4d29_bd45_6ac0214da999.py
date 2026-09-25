"""Reply All Arrow: A curved arrow rises from lower right into a left-facing head, with a second left chevron beside its tip. Generate this component alone; exclude Circle Frame.

Construction: Two left heads precede one rounded return shaft; no extra arrow is introduced.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e93efebe-fde8-4d29-bd45-6ac0214da999'
SOURCE_PATH = 'pictographic-primitives/state/circle reply all_e93efebe-fde8-4d29-bd45-6ac0214da999.svg'
AUTHOR = 'gpt-6'


class ReplyAllArrow(Sub32):
    icon_id = 'reply-all-arrow'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('reply', 'all', 'arrow', 'curved', 'rises', 'lower', 'right', 'left')

    def build(self):
        self.add_polyline('outer-head',(8,4),(2,10),(8,16))
        self.add_polyline('head',(22,4),(16,10),(22,16))
        self.add_line('run',(16,10),(22,10))
        self.add_arc('bend',(22,10),(30,18),radius_x=8)
        self.add_line('stem',(30,18),(30,28))
        self.add_contour('shaft','run','bend','stem')
        self.relate('connect','head','shaft')
