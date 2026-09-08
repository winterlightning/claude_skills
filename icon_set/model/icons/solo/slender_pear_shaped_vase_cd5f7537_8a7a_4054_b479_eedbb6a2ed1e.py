"""A pear-shaped vase with mirrored curved shoulders, an inward neck and a flared mouth."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd5f7537-8a7a-4054-b479-eedbb6a2ed1e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_cd5f7537-8a7a-4054-b479-eedbb6a2ed1e.svg'
AUTHOR = 'gpt-6'


class SlenderPearShapedVase(Solo48):
    icon_id = 'slender-pear-shaped-vase'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'bottle', 'ceramic', 'vessel', 'decor', 'flared lip', 'pear shape')

    def build(self) -> None:
        self.add_line('lip', (16,2), (32,2))
        self.add_arc('neck-right', (32,2), (32,18), radius_x=4, radius_y=8, sweep=False)
        self.add_arc('shoulder-right', (32,18), (37,32), radius_x=5, radius_y=14)
        self.add_arc('base-right', (37,32), (24,46), radius_x=13, radius_y=14)
        self.add_arc('base-left', (24,46), (11,32), radius_x=13, radius_y=14)
        self.add_arc('shoulder-left', (11,32), (16,18), radius_x=5, radius_y=14)
        self.add_arc('neck-left', (16,18), (16,2), radius_x=4, radius_y=8, sweep=False)
        self.add_contour('vase', 'lip','neck-right','shoulder-right','base-right','base-left','shoulder-left','neck-left', closed=True)
