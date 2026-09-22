"""Arrow Broad Diagonal Down Right. Square envelope; closed broad arrow derived by vertical reflection of the up-right construction, preserving diagonal symmetry and shaft width.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = 'bfff57f1-27c7-49c2-88d7-8c4f46f134b0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow down right corner_bfff57f1-27c7-49c2-88d7-8c4f46f134b0.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-broad-diagonal-down-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Diagonal Down Right Arrow',)
    keywords = ('arrow', 'down', 'right', 'diagonal', 'outline', 'direction', 'pointer')

    def build(self):
        points = ((6,34), (14,42), (32,24), (42,34), (42,6), (14,6), (24,16))
        self.add_polyline('outline', *((x,48-y) for x,y in points), closed=True)
