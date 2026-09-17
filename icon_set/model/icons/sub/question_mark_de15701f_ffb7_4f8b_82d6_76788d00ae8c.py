"""Question Mark: A rounded upper hook curves into a short descending stem, with a detached tiny dot below. Generate this component alone; exclude Circle Frame.

Construction: A broad rounded question hook descends into a short stem above its detached dot.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'de15701f-ffb7-4f8b-82d6-76788d00ae8c'
SOURCE_PATH = 'pictographic-primitives/state/state question_de15701f-ffb7-4f8b-82d6-76788d00ae8c.svg'
AUTHOR = 'gpt-6'


class QuestionMark(Sub32):
    icon_id = 'question-mark'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('question', 'mark', 'rounded', 'upper', 'hook', 'curves', 'short', 'descending')

    def build(self):
        self.add_arc('top',(6,10),(26,10),radius_x=10,radius_y=8)
        self.add_arc('turn',(26,10),(21,17),radius_x=8,radius_y=8)
        self.add_arc('neck',(21,17),(16,23),radius_x=8,radius_y=8,sweep=False)
        self.add_contour('hook','top','turn','neck')
        self.add_dot('dot',(16,30))
