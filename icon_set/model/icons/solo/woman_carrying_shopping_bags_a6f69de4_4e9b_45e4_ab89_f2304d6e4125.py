"""Woman Carrying Shopping Bags. Lucide user-round and shopping-bag: central figure with mirrored held bags. V neckline retained; tapered torso reduced to a stroke and tiny handles omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a6f69de4-4e9b-45e4-ab89-f2304d6e4125'
SOURCE_PATH = 'pictographic-primitives/shopping/shopping bag woman carry_a6f69de4-4e9b-45e4-ab89-f2304d6e4125.svg'
AUTHOR = 'gpt-6'

class WomanCarryingShoppingBags(Solo48):
    icon_id = 'woman-carrying-shopping-bags'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    aliases = ()
    keywords = ('woman', 'shopper', 'bags', 'shopping', 'carry', 'retail', 'purchase')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42); reflected arms and bags.
        self.add_arc('head-a',(19,11),(29,11),radius_x=5)
        self.add_arc('head-b',(29,11),(19,11),radius_x=5)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_polyline('neckline',(18,26),(24,32),(30,26))
        self.add_line('torso',(24,32),(24,42))
        self.relate('connect','neckline','torso')
        for side,x,shoulder in [('left',6,18),('right',34,30)]:
            self.add_line(f'arm-{side}',(shoulder,26),(x+4,32))
            self.relate('connect',f'arm-{side}','neckline')
            self.add_polyline(f'bag-{side}',(x,32),(x+4,32),(x+8,32),(x+8,42),(x,42),(x,32),closed=True)
            self.relate('connect',f'arm-{side}',f'bag-{side}')
