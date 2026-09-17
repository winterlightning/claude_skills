"""Play Triangle: A right-facing outlined triangle has a vertical left edge and two sloping sides meeting at a central right tip. Generate this component alone; exclude Clapperboard Frame.

Construction: The single right-pointing triangle is isolated from the clapperboard.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '0f21b953-38cf-4876-b8d5-ba4c1dec18c3'
SOURCE_PATH = 'pictographic-primitives/state/clapper board_0f21b953-38cf-4876-b8d5-ba4c1dec18c3.svg'
AUTHOR = 'gpt-6'


class PlayTriangleState95(Sub32):
    icon_id = 'play-triangle-state-95'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('play', 'triangle', 'right', 'facing', 'outlined', 'vertical', 'left', 'edge')

    def build(self):
        self.add_polyline('play',(6,2),(26,16),(6,30),closed=True)
