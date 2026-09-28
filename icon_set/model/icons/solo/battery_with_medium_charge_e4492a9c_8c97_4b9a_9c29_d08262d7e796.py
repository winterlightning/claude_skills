"""Battery with Medium Charge. Battery case owns an attached terminal and a rectangular medium-charge indicator. Mirrored across y=24. Shared case envelope (4,10)-(44,38); internal block retains source identity. Lucide battery-full contributes the simple battery silhouette. Small corner rounding omitted for clean openings."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'e4492a9c-8c97-4b9a-9c29-d08262d7e796'
SOURCE_PATH = 'pictographic-primitives/devices/charging battery almost full_e4492a9c-8c97-4b9a-9c29-d08262d7e796.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'battery-with-medium-charge'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ('Battery with Medium Charge',)
    keywords = ('battery', 'with', 'medium', 'charge')
    def build(self):
        self.add_polyline('case',(4,10),(36,10),(36,20),(44,20),(44,28),(36,28),(36,38),(4,38),closed=True)
        self.add_polyline('charge',(12,18),(24,18),(24,30),(12,30),closed=True)
