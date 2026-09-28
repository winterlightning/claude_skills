"""Lucide signpost: one broad sign silhouette. Omitted redundant inset border; triangle cord retains hanging-sign identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '854860b1-f414-46e3-8493-5146f1cb376f'
SOURCE_PATH = 'pictographic-primitives/shopping/shop sign_854860b1-f414-46e3-8493-5146f1cb376f.svg'
AUTHOR = 'gpt-6'

class HangingShopSignSolo(Solo48):
    icon_id = 'hanging-shop-sign-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('sign', 'shop', 'hanging', 'board', 'cord', 'blank', 'retail')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Triangle cord and broad signboard.
        self.add_polyline('cord',(12,20),(24,6),(36,20))
        self.add_line('top',(10,20),(12,20))
        self.add_line('top-mid',(12,20),(36,20))
        self.add_line('top-end',(36,20),(38,20))
        self.add_arc('tr',(38,20),(42,24),radius_x=4)
        self.add_line('right',(42,24),(42,38))
        self.add_arc('br',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('bl',(10,42),(6,38),radius_x=4)
        self.add_line('left',(6,38),(6,24))
        self.add_arc('tl',(6,24),(10,20),radius_x=4)
        self.add_contour('board','top','top-mid','top-end','tr','right','br','bottom','bl','left','tl',closed=True)
        self.relate('connect','cord','board')
