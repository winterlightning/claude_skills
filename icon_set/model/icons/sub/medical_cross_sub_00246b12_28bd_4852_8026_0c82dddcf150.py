"""Medical cross: a balanced outlined cross isolated from its magnifier.
Plan: one closed orthogonal contour, mirrored about both axes; arm width 8.
SQUARE centreline extremes are 2 and 30 on both axes.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '00246b12-28bd-4852-8026-0c82dddcf150'
SOURCE_PATH = 'pictographic-primitives/state/search medical cross 1_00246b12-28bd-4852-8026-0c82dddcf150.svg'
AUTHOR = 'gpt-6'
class MedicalCross(Sub32):
    icon_id = 'medical-cross-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ('medical-plus',)
    keywords = ('medical','health','hospital','cross','first-aid','care')
    def build(self):
        lo,hi,a,b = 2,30,12,20
        self.add_polyline('outline',(a,lo),(b,lo),(b,a),(hi,a),(hi,b),(b,b),(b,hi),(a,hi),(a,b),(lo,b),(lo,a),(a,a),closed=True)
