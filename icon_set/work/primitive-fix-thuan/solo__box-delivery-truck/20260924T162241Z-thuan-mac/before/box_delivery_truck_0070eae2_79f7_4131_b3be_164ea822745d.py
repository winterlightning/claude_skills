"""Delivery truck with separated wheels. HRECT_L supports a broad side view.
Lucide truck contributes cargo/cab hierarchy; reference gives cargo/cab proportions.
Omit separate windshield bar and detach wheels to keep clear wheel arches. Paired wheels share radius and axle height."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "0070eae2-79f7-4131-b3be-164ea822745d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_10/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "box-delivery-truck"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ["Delivery Truck"]
    keywords = ["truck", "delivery", "cargo", "vehicle", "box", "cab", "wheels"]
    def build(self):
        self.add_polyline("body",(4,25),(4,8),(24,8),(24,16),(34,16),(44,25),(24,25),closed=True)
        self.add_line("divider",(24,16),(24,25))
        self.relate("connect","body","divider")
        for name,x in [("rear",12),("front",36)]:
            self.add_arc(name+"-top",(x-3,37),(x+3,37),radius_x=3)
            self.add_arc(name+"-bottom",(x+3,37),(x-3,37),radius_x=3)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
