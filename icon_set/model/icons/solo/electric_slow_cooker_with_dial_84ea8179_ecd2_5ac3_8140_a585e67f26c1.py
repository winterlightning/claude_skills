"""Electric Slow Cooker Appliance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '84ea8179-ecd2-5ac3-8140-a585e67f26c1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/appliances slow cooker_84ea8179-ecd2-5ac3-8140-a585e67f26c1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'electric-slow-cooker-with-dial'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('slow cooker', 'appliance', 'pot', 'lid', 'dial', 'kitchen', 'cooking')

    def build(self):
        # Plan: Broad slow cooker with flared lid knob and circular dial. Lucide cooking-pot curved vessel. Fine feet and lid seam omitted for open control space. Envelope (4,8)-(44,40). Dial rendered as a solid circular control.
        self.add_polyline('knob',(18,8),(24,8),(30,8));self.add_line('stem',(24,8),(24,16));self.relate('connect','knob','stem')
        self.add_bezier('body',(24,16),((14,16),(4,18),(4,24)),((4,28),(6,34),(8,36)),((10,40),(16,40),(24,40)),((32,40),(38,40),(40,36)),((42,34),(44,28),(44,24)),((44,18),(34,16),(24,16)))
        self.add_contour('pot','body',closed=True);self.relate('connect','stem','pot')
        self.add_dot('dial',(24,28))
