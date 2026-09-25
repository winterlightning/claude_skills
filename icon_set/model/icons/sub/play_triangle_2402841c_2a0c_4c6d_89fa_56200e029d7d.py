"""Play Triangle: An outlined triangle points right, with a vertical left edge and two sloping sides meeting at the tip. Generate this component alone; exclude Open Circle Frame.

Construction: A right-facing triangle with mirrored diagonals encloses a clear centre.
Keyshape: VRECT_L; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '2402841c-2a0c-4c6d-89fa-56200e029d7d'
SOURCE_PATH = 'pictographic-primitives/state/circle play connect_2402841c-2a0c-4c6d-89fa-56200e029d7d.svg'
AUTHOR = 'gpt-6'


class PlayTriangle(Sub32):
    icon_id = 'play-triangle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('play', 'triangle', 'outlined', 'points', 'right', 'vertical', 'left', 'edge')

    def build(self):
        self.add_polyline('play',(6,2),(26,16),(6,30),closed=True)
