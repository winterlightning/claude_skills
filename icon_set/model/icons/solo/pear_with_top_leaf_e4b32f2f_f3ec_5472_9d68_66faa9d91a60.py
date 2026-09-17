"""Fresh Pear Fruit With Leaf."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4b32f2f-f3ec-5472-9d68-66faa9d91a60'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pear_e4b32f2f-f3ec-5472-9d68-66faa9d91a60.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pear-with-top-leaf'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('pear', 'fruit', 'leaf', 'stem', 'produce', 'food', 'orchard')

    def build(self):
        # Plan: Pear with broad lower body, narrow neck and pointed top leaf. Lucide apple organic body and attached foliage; bent stem merged into leaf junction. Envelope (10,4)-(38,44).
        self.add_bezier('body',(24,14),((17,14),(20,21),(14,26)),((11,29),(10,31),(10,34)),((10,41),(17,44),(24,44)),((31,44),(38,41),(38,34)),((38,31),(37,29),(34,26)),((28,21),(31,14),(24,14)))
        self.add_contour('pear','body',closed=True)
        self.add_bezier('leaf',(24,14),((24,6),(30,4),(36,4)),((36,12),(30,14),(24,14)))
        self.add_contour('leaf-outline','leaf',closed=True);self.relate('connect','leaf-outline','pear')
