"""Lucide user-round: round head and mirrored shoulders. Square apron neckline retained; no facial detail."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '235da794-190c-5658-9446-31dd98beffe1'
SOURCE_PATH = 'pictographic-primitives/shopping/shop assistant_235da794-190c-5658-9446-31dd98beffe1.svg'
AUTHOR = 'gpt-6'

class ShopAssistantInApron(Solo48):
    icon_id = 'shop-assistant-in-apron'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('assistant', 'shop', 'apron', 'person', 'staff', 'retail', 'worker')

    def build(self) -> None:
        self.add_arc('head-a',(17,11),(31,11),radius_x=7)
        self.add_arc('head-b',(31,11),(17,11),radius_x=7)
        self.add_contour('head','head-a','head-b',closed=True)

        # Head and torso share the x=24 axis; VRECT_L (8,4)-(40,44).
        self.add_line('shoulders',(16,27),(32,27))
        self.add_arc('right-shoulder',(32,27),(40,35),radius_x=8)
        self.add_line('lower-1',(40, 35),(40, 44))
        self.add_line('lower-2',(40, 44),(32, 44))
        self.add_line('lower-3',(32, 44),(16, 44))
        self.add_line('lower-4',(16, 44),(8, 44))
        self.add_line('lower-5',(8, 44),(8, 35))
        self.add_arc('left-shoulder',(8,35),(16,27),radius_x=8)
        self.add_contour('body','shoulders','right-shoulder',*(f'lower-{i}' for i in range(1,6)),'left-shoulder',closed=True)
        self.add_polyline('neckline',(16,27),(16,35),(32,35),(32,27))
        self.relate('connect','neckline','body')
