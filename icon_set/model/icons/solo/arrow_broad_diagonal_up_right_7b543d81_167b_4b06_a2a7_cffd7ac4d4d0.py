"""Arrow Broad Diagonal Up Right. Square envelope; one closed arrow contour symmetric about the rising diagonal. Shaft edges share a 16-unit offset sum; omit thin source stroke styling.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '7b543d81-167b-4b06-a2a7-cffd7ac4d4d0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow diagonal 1_7b543d81-167b-4b06-a2a7-cffd7ac4d4d0.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-broad-diagonal-up-right'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Diagonal Up Right Arrow',)
    keywords = ('arrow', 'up', 'right', 'diagonal', 'outline', 'direction', 'pointer')

    def build(self):
        self.add_polyline('outline', (6,34), (14,42), (32,24), (42,34), (42,6), (14,6), (24,16), closed=True)
