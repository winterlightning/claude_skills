"""liras: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Liras(Solo48):
    icon_id = 'liras'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'money'
    categories = ('money', 'state', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('liras', 'money')

    def build(self):
        # Plan: VRECT_L; coherent rounded crest and foot, straight shared stem.
        # Reference: Geometric tangent crest and circular foot turn.
        self.add_bezier('crest',(40,12),((40,7),(35,4),(29,4)),((23,4),(18,7),(18,12)))
        self.add_line('stem',(18,12),(18,34))
        self.add_arc('foot-turn',(18,34),(8,44),radius_x=10)
        self.add_contour('run','crest','stem','foot-turn')
        self.add_line('foot',(8,44),(40,44))
        for i,y in enumerate((19,33)):
            self.add_line(f'bar-{i}',(9,y),(30,y))
            self.relate('connect',f'bar-{i}','run')
        self.relate('connect','foot','run')
