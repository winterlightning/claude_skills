"""Play Triangle: A right-facing triangle has a vertical back edge and two equal sloping sides enclosing an empty centre. Generate this component alone; exclude Circle Frame.

Construction: An outlined right triangle retains a vertical rear edge and empty centre.
Keyshape: VRECT_L; final SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '19c25b61-6678-43f8-aae6-dc07a9ea8291'
SOURCE_PATH = 'pictographic-primitives/state/circle play_19c25b61-6678-43f8-aae6-dc07a9ea8291.svg'
AUTHOR = 'gpt-6'


class PlayTriangleState74(Sub32):
    icon_id = 'play-triangle-state-74'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('play', 'triangle', 'right', 'facing', 'vertical', 'back', 'edge', 'equal')

    def build(self):
        self.add_polyline('play',(6,2),(26,16),(6,30),closed=True)
