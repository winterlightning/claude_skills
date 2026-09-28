"""Butternut Squash Vegetable."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e2a3b90-793a-5161-aa41-5a7e08f9195c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/butternutsquash_0e2a3b90-793a-5161-aa41-5a7e08f9195c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-butternut-squash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('butternut', 'squash', 'gourd', 'vegetable', 'stem', 'produce', 'food')

    def build(self):
        # Plan: Bulb tapering into angled neck and curved stem. No exact Lucide match; smooth cubic silhouette. Intentional diagonal asymmetry, envelope (6,6)-(42,42).
        self.add_bezier('body',(14,19),((20,16),(23,14),(28,10)),((30,8),(32,8),(34,10)),((38,12),(39,16),(35,20)),((32,24),(30,27),(29,31)),((26,40),(24,42),(17,42)),((10,42),(6,37),(6,30)),((6,24),(9,21),(14,19)))
        self.add_contour('squash','body',closed=True)
        self.add_bezier('stem',(34,10),((39,14),(42,10),(42,6)));self.relate('connect','stem','squash')
