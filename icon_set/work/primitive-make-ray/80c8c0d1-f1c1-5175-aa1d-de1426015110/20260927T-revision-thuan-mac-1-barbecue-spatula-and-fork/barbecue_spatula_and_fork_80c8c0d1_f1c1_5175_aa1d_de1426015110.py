"""Barbecue Spatula and Fork."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '80c8c0d1-f1c1-5175-aa1d-de1426015110'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__barbecue-spatula-and-fork/20260927T152212Z-thuan-mac-1/reference/barbecue set_80c8c0d1-f1c1-5175-aa1d-de1426015110.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'barbecue-spatula-and-fork'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('barbecue', 'spatula', 'fork', 'utensil', 'grilling', 'cooking', 'tool')

    def build(self):
        # A tapered slotted spatula and rounded two-prong fork share a baseline.
        self.add_polyline('spatula-head',(6,6),(24,6),(24,18),(22,24),(15,24),(8,24),(6,18),closed=True)
        self.add_line('spatula-slot',(15,14),(15,16))
        self.add_line('spatula-handle',(15,24),(15,42))
        self.relate('connect','spatula-head','spatula-handle')
        self.add_line('fork-left',(32,6),(32,20))
        self.add_arc('fork-bottom-left',(32,20),(37,25),radius_x=5,sweep=False)
        self.add_arc('fork-bottom-right',(37,25),(42,20),radius_x=5,sweep=False)
        self.add_line('fork-right',(42,20),(42,6))
        self.add_contour('fork','fork-left','fork-bottom-left','fork-bottom-right','fork-right')
        self.add_line('fork-handle',(37,25),(37,42))
        self.relate('connect','fork','fork-handle')
