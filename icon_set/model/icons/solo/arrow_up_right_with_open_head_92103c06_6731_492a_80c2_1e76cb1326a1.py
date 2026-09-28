"""Arrow Up Right with Open Head. Square envelope preserves the long diagonal shaft; head arms share a 20-unit length and one tip node. No source details omitted.
Reference supplies silhouette and direction; Lucide arrow-up-right supplies
shared shaft/head junction construction. Rebuilt on SOLO48; no traced coordinates.
"""
from ._base import Solo48
from ...keyshapes import Keyshape

SOURCE_ICON_ID = '92103c06-6731-492a-80c2-1e76cb1326a1'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram arrow up left corner_92103c06-6731-492a-80c2-1e76cb1326a1.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'arrow-up-right-with-open-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Arrow Pointing Up Right',)
    keywords = ('arrow', 'up', 'right', 'diagonal', 'direction', 'pointer', 'line')

    def build(self):
        tip = (42,6)
        self.add_line('head-top', (22,6), tip)
        self.add_line('head-right', tip, (42,26))
        self.add_contour('head','head-top','head-right')
        self.add_line('shaft',(6,42),tip)
        self.relate('connect','head','shaft')
