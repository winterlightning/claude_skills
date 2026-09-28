"""Arrow Dashed Stepped Descent. Square envelope; three descending runs preserve the upper left start, horizontal middle and downward right terminal. Reduce tiny source dashes for legibility; shared tip and symmetric head arms.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '92d71861-1ee8-422d-81f5-cc5700c86ade'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram fall fast dash large head_92d71861-1ee8-422d-81f5-cc5700c86ade.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-dashed-stepped-descent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Dashed Downward Path',)
    keywords = ('arrow', 'dashed', 'down', 'step', 'path', 'bend', 'direction')

    def build(self):
        self.add_line('start',(6,6),(6,12))
        self.add_bezier('first-bend',(6,21),((6,24),(10,24),(14,24)))
        self.add_arc('last-bend',(24,24),(34,34),radius_x=10,sweep=True)
        tip=(34,42)
        self.add_line('terminal',(34,34),tip)
        self.add_contour('end','last-bend','terminal')
        self.add_polyline('head',(26,34),tip,(42,34))
        self.relate('connect','end','head')
