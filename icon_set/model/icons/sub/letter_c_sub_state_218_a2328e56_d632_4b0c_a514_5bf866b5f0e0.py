"""Letter C: A tall uppercase C has rounded top and bottom curves joined by a straight left side, opening to the right. Generate this component alone; exclude Prohibition Frame.

Construction: The source tall C has a straight left side and rounded top and bottom ends.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a2328e56-d632-4b0c-a514-5bf866b5f0e0'
SOURCE_PATH = 'pictographic-primitives/state/prohitbition content_a2328e56-d632-4b0c-a514-5bf866b5f0e0.svg'
AUTHOR = 'gpt-6'


class LetterCSubState218(Sub32):
    icon_id = 'letter-c-sub-state-218'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('letter', 'c', 'tall', 'uppercase', 'rounded', 'top', 'bottom', 'curves')

    def build(self):
        self.add_arc('top',(26,10),(6,10),radius_x=10,radius_y=8,sweep=False)
        self.add_line('side',(6,10),(6,22))
        self.add_arc('bottom',(6,22),(26,22),radius_x=10,radius_y=8,sweep=False)
        self.add_contour('c','top','side','bottom')
