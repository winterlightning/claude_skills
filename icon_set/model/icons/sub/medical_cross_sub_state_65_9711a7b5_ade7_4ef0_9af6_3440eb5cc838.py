"""Medical Cross: An outlined medical cross has four equal broad arms with square ends surrounding a central square junction. Generate this component alone; exclude Circle Frame.

Construction: The source outlined cross retains its four equally thick arms and hollow centre.
Keyshape: SQUARE; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '9711a7b5-ade7-4ef0-9af6-3440eb5cc838'
SOURCE_PATH = 'pictographic-primitives/state/circle medical cross 1_9711a7b5-ade7-4ef0-9af6-3440eb5cc838.svg'
AUTHOR = 'gpt-6'


class MedicalCrossSubState65(Sub32):
    icon_id = 'medical-cross-sub-state-65'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('medical', 'cross', 'outlined', 'four', 'equal', 'broad', 'arms', 'square')

    def build(self):
        lo,hi,a,b = 2,30,12,20
        self.add_polyline('outline',(a,lo),(b,lo),(b,a),(hi,a),(hi,b),(b,b),(b,hi),(a,hi),(a,b),(lo,b),(lo,a),(a,a),closed=True)
