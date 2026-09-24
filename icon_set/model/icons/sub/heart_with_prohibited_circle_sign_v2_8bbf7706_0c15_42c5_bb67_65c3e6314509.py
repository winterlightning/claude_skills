"""Heart inside a prohibition circle with the source's two exposed slash ends."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ._compact_reference_helpers import circle

SOURCE_ICON_ID = "8bbf7706-0c15-42c5-bb67-65c3e6314509"
SOURCE_PATH = "pictographic-primitives/other/slash heart_8bbf7706-0c15-42c5-bb67-65c3e6314509.svg"
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('interrupted enclosing circle', 'two short diagonal marks', 'heart')
REPAIR_PLAN = {'concept': 'Heart With Prohibited Circle Sign', 'core_parts': ('interrupted enclosing circle', 'two short diagonal marks', 'heart'), 'flexible_parts': 'heart and slash proportions', 'ladder': 'Reduced the heart and joined the two visible slash ends'}



class DrawingVariant2(Sub32):
    icon_id = "heart-with-prohibited-circle-sign-v2"
    variant_label = 'Reduced the heart and joined the two visible slash ends'
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "state"
    category = "primitives/state"
    aliases = ("no-heart", "heart-prohibited")
    keywords = ("heart", "prohibited", "ban", "slash", "no")

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_line("slash-upper", (4, 9), (10, 13))
        self.add_line("slash-lower", (22, 16), (28, 23))
        self.add_bezier("heart", (16, 22), ((12, 19), (10, 16), (10, 13)), ((10, 10), (14, 9), (16, 12)), ((18, 9), (22, 10), (22, 13)), ((22, 16), (20, 19), (16, 22)))
        self.add_contour("heart-shape", "heart", closed=True)
        self.relate("connect", "frame", "slash-upper")
        self.relate("connect", "frame", "slash-lower")
        self.relate("connect", "heart-shape", "slash-upper")
        self.relate("connect", "heart-shape", "slash-lower")
