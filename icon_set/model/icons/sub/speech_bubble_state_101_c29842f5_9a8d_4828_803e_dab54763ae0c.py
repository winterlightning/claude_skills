"""Speech Bubble: A smaller rounded rectangular speech bubble has an empty interior and a pointed tail projecting downward near its right edge. Generate this component alone; exclude Speech Bubble Frame.

Construction: Small source speech bubble is isolated from its outer bubble; retain bottom-right angular tail.
Keyshape: HRECT_XL; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c29842f5-9a8d-4828-803e-dab54763ae0c'
SOURCE_PATH = 'pictographic-primitives/state/comment box with message_c29842f5-9a8d-4828-803e-dab54763ae0c.svg'
AUTHOR = 'gpt-6'


class SpeechBubbleState101(Sub32):
    icon_id = 'speech-bubble-state-101'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('speech', 'bubble', 'smaller', 'rounded', 'rectangular', 'empty', 'interior', 'pointed')

    def build(self):
        self.add_polyline('bubble',(2,4),(30,4),(30,20),(24,20),(24,28),(16,20),(2,20),closed=True)
