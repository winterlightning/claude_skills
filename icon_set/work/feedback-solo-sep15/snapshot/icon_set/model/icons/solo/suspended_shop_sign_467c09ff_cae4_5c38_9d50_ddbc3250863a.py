"""Lucide signpost: rounded board with integral suspension. SHOP lettering omitted; board and rail retain the named subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '467c09ff-cae4-5c38-9d50-ddbc3250863a'
SOURCE_PATH = 'pictographic-primitives/shopping/shop street sign_467c09ff-cae4-5c38-9d50-ddbc3250863a.svg'
AUTHOR = 'gpt-6'

class SuspendedShopSign(Solo48):
    icon_id = 'suspended-shop-sign'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('shop', 'sign', 'signboard', 'hanging', 'lettering', 'retail', 'store')

    def build(self) -> None:
        # HRECT_L (4,8)-(44,40). Shared supports x=14 and 34.
        self.add_polyline('rail',(4,8),(14,8),(34,8),(44,8))
        for x in (14,34):
            self.add_line(f'support-{x}',(x,8),(x,20))
            self.relate('connect',f'support-{x}','rail')
        self.add_line('top-1',(8, 20),(14, 20))
        self.add_line('top-2',(14, 20),(34, 20))
        self.add_line('top-3',(34, 20),(40, 20))
        self.add_arc('tr',(40,20),(44,24),radius_x=4)
        self.add_line('right',(44,24),(44,36))
        self.add_arc('br',(44,36),(40,40),radius_x=4)
        self.add_line('bottom',(40,40),(8,40))
        self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,24))
        self.add_arc('tl',(4,24),(8,20),radius_x=4)
        self.add_contour('board','top-1','top-2','top-3','tr','right','br','bottom','bl','left','tl',closed=True)
        for x in (14,34):self.relate('connect',f'support-{x}','board')
