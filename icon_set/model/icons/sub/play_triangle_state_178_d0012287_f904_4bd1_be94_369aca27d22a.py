"""Play Triangle: A right-pointing triangle has a vertical left edge, gently rounded corners, and an empty interior. Generate this component alone; exclude Phone Frame.

Construction: An outlined right play triangle is isolated from the phone frame.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd0012287-f904-4bd1-be94-369aca27d22a'
SOURCE_PATH = 'pictographic-primitives/state/mobile phone control play_d0012287-f904-4bd1-be94-369aca27d22a.svg'
AUTHOR = 'gpt-6'


class PlayTriangleState178(Sub32):
    icon_id = 'play-triangle-state-178'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('play', 'triangle', 'right', 'pointing', 'vertical', 'left', 'edge', 'gently')

    def build(self):
        self.add_polyline('play',(6,2),(26,16),(6,30),closed=True)
