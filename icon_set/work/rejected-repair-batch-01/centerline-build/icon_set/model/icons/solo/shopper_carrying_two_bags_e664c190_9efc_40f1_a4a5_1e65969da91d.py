"""Lucide user-round and shopping-bag principles. Mirrored bags held by a central person form one natural scene. Torso reduced to a single stroke; loop handles omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e664c190-9efc-40f1-a4a5-1e65969da91d'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag carry_e664c190-9efc-40f1-a4a5-1e65969da91d.svg'
AUTHOR = 'gpt-6'

class ShopperCarryingTwoBags(Solo48):
    icon_id = 'shopper-carrying-two-bags'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('shopper', 'person', 'bags', 'shopping', 'carry', 'retail', 'purchase')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42); body reduced to a central human figure with equal bags.
        self.add_arc('head-a',(18,12),(30,12),radius_x=6)
        self.add_arc('head-b',(30,12),(18,12),radius_x=6)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_polyline('arms',(10,32),(24,27),(38,32))
        self.add_line('body',(24,27),(24,42))
        self.relate('connect','body','arms')
        for side,x in [('left',6),('right',34)]:
            self.add_polyline(f'bag-{side}',(x,32),(x+4,32),(x+8,32),(x+8,42),(x,42),(x,32),closed=True)
            self.relate('connect',f'bag-{side}','arms')
