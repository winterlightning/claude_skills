"""Lucide shopping-bag: rounded base and single coherent body. Rail simplified to a stroke; lower band omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a55f556a-5001-40b0-9f32-40bb7ad413e5'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag hang_a55f556a-5001-40b0-9f32-40bb7ad413e5.svg'
AUTHOR = 'gpt-6'

class ShoppingBagOnHangingRail(Solo48):
    icon_id = 'shopping-bag-on-hanging-rail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('bag', 'hanging', 'rail', 'straps', 'shopping', 'carry', 'retail')

    def build(self) -> None:
        # HRECT_L (4,8)-(44,40); rail and straps share suspension point (24,8).
        self.add_polyline('rail',(4,8),(24,8),(44,8))
        self.add_polyline('straps',(14,24),(24,8),(34,24))
        self.relate('connect','rail','straps')
        self.add_line('top-1',(10, 24),(14, 24))
        self.add_line('top-2',(14, 24),(34, 24))
        self.add_line('top-3',(34, 24),(38, 24))
        self.add_line('right',(38,24),(38,32))
        self.add_arc('br',(38,32),(30,40),radius_x=8)
        self.add_line('base',(30,40),(18,40))
        self.add_arc('bl',(18,40),(10,32),radius_x=8)
        self.add_line('left',(10,32),(10,24))
        self.add_contour('bag','top-1','top-2','top-3','right','br','base','bl','left',closed=True)
        self.relate('connect','straps','bag')
