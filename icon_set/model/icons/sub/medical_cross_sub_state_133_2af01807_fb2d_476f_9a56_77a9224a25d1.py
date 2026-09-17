"""Medical Cross: An outlined medical cross has four equal broad arms with square ends and an empty interior. Generate this component alone; exclude House Frame.

Construction: The small outlined cross retains its hollow centre and stepped arms.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2af01807-fb2d-476f-9a56-77a9224a25d1'
SOURCE_PATH = 'pictographic-primitives/state/home medical cross 1_2af01807-fb2d-476f-9a56-77a9224a25d1.svg'
AUTHOR = 'gpt-6'


class MedicalCrossSubState133(Sub32):
    icon_id = 'medical-cross-sub-state-133'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('medical', 'cross', 'outlined', 'four', 'equal', 'broad', 'arms', 'square')

    def build(self):
        lo,hi,a,b = 2,30,12,20
        self.add_polyline('outline',(a,lo),(b,lo),(b,a),(hi,a),(hi,b),(b,b),(b,hi),(a,hi),(a,b),(lo,b),(lo,a),(a,a),closed=True)
