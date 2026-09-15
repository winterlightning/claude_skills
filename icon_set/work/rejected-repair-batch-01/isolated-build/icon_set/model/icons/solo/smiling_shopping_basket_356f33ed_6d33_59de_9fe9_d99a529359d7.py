"""Smiling Shopping Basket. Lucide shopping-basket construction. Inward handles, two eyes and curved smile retained; symmetric facial spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '356f33ed-6d33-59de-9fe9-d99a529359d7'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping basket smile_356f33ed-6d33-59de-9fe9-d99a529359d7.svg'
AUTHOR = 'gpt-6'

class SmilingShoppingBasket(Solo48):
    icon_id = 'smiling-shopping-basket'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('basket', 'shopping', 'smile', 'face', 'handle', 'retail', 'mascot')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42); intrinsic mascot face, not a separate badge.
        self.add_line('rim-1',(6, 14),(14, 14))
        self.add_line('rim-2',(14, 14),(34, 14))
        self.add_line('rim-3',(34, 14),(42, 14))
        self.add_line('right',(42,14),(38,38))
        self.add_arc('br',(38,38),(34,42),radius_x=4)
        self.add_line('base',(34,42),(14,42))
        self.add_arc('bl',(14,42),(10,38),radius_x=4)
        self.add_line('left',(10,38),(6,14))
        self.add_contour('body','rim-1','rim-2','rim-3','right','br','base','bl','left',closed=True)
        for side,start,end in [('left',(14,14),(20,6)),('right',(34,14),(28,6))]:
            self.add_line(f'handle-{side}',start,end)
            self.relate('connect',f'handle-{side}','body')
        for x in (18,30):self.add_dot(f'eye-{x}',(x,23))
        self.add_arc('smile',(22,32),(26,32),radius_x=4,radius_y=2,sweep=False)
