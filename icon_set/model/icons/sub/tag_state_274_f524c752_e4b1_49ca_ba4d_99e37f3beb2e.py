"""Tag: A blank diagonal tag has rounded outer corners and a sloping pointed right end. A tiny attachment hole sits near the broad upper-left corner, inside the otherwise empty outline.

Construction: The blank diagonal tag retains its pointed right end, clipped lower corner and tiny attachment dot.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'f524c752-e4b1-49ca-ba4d-99e37f3beb2e'
SOURCE_PATH = 'pictographic-primitives/state/tag 1_f524c752-e4b1-49ca-ba4d-99e37f3beb2e.svg'
AUTHOR = 'gpt-6'


class TagState274(Sub32):
    icon_id = 'tag-state-274'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('tag', 'blank', 'diagonal', 'rounded', 'outer', 'corners', 'sloping', 'pointed')

    def build(self):
        self.add_polyline('outline',(2,2),(18,2),(30,14),(30,18),(18,30),(14,30),(2,18),closed=True)
        self.add_dot('attachment',(9,9))
