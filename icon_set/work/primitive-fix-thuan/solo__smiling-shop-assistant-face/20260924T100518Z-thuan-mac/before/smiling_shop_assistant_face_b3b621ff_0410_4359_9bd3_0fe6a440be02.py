"""No exact Lucide smile match locally; smooth oval face, equal eyes, shallow smile. Deliberately off-centre hair parting."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b3b621ff-0410-4359-9bd3-0fe6a440be02'
SOURCE_PATH = 'pictographic-primitives/shopping/shop assistant_b3b621ff-0410-4359-9bd3-0fe6a440be02.svg'
AUTHOR = 'gpt-6'

class SmilingShopAssistantFace(Solo48):
    icon_id = 'smiling-shop-assistant-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/shopping"
    aliases = ()
    keywords = ('assistant', 'face', 'smile', 'person', 'hair', 'shop', 'staff')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42).
        self.add_arc('hair-cap',(6,14),(42,14),radius_x=18,radius_y=8)
        self.add_arc('face',(42,14),(6,14),radius_x=18,radius_y=28)
        self.add_contour('outline','hair-cap','face',closed=True)
        self.add_polyline('parting',(6,14),(20,14),(27,10),(34,14),(42,14))
        self.relate('connect','parting','outline')
        for x in (18,30):self.add_dot(f'eye-{x}',(x,24))
        self.add_arc('smile',(22,33),(26,33),radius_x=4,radius_y=2,sweep=False)
