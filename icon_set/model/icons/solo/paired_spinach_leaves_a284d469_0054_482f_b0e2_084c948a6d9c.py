"""Fresh Spinach Leaves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a284d469-0054-482f-b0e2-084c948a6d9c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/spinash_a284d469-0054-482f-b0e2-084c948a6d9c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-spinach-leaves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('spinach', 'leaf', 'greens', 'vegetable', 'vein', 'produce', 'food')

    def build(self):
        # Plan: Two overlapping spinach leaves joined to a basal stem. Lucide leaf smooth outlines; smaller branching veins omitted. Taller right leaf and left lean preserved. Envelope (6,6)-(42,42).
        self.add_bezier('right-leaf',(26,34),((22,29),(22,24),(24,20)),((25,12),(28,6),(34,6)),((42,6),(42,16),(42,22)),((42,30),(34,34),(26,34)))
        self.add_contour('right','right-leaf',closed=True)
        self.add_bezier('left',(26,34),((12,38),(6,30),(6,20)),((6,10),(15,8),(24,20)))
        self.relate('connect','left','right')
        self.add_line('stem',(26,34),(24,42));self.relate('connect','stem','left');self.relate('connect','stem','right')
        self.add_line('vein',(26,34),(34,16));self.relate('connect','vein','right');self.relate('connect','vein','left');self.relate('connect','vein','stem')
