"""A pear-shaped vase with mirrored curved shoulders, an inward neck and a flared mouth."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa457b72-c0c6-4f42-99fe-76451340672d'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/bottle_aa457b72-c0c6-4f42-99fe-76451340672d.svg'
AUTHOR = 'gpt-6'


class PearShapedVase(Solo48):
    icon_id = 'pear-shaped-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('vase', 'bottle', 'ceramic', 'vessel', 'decor', 'flared lip', 'pear shape')

    def build(self) -> None:
        self.add_line('lip', (16,2), (32,2))
        self.add_arc('neck-right', (32,2), (32,18), radius_x=4, radius_y=8, sweep=False)
        self.add_arc('shoulder-right', (32,18), (40,32), radius_x=8, radius_y=14)
        self.add_arc('base-right', (40,32), (24,46), radius_x=16, radius_y=14)
        self.add_arc('base-left', (24,46), (8,32), radius_x=16, radius_y=14)
        self.add_arc('shoulder-left', (8,32), (16,18), radius_x=8, radius_y=14)
        self.add_arc('neck-left', (16,18), (16,2), radius_x=4, radius_y=8, sweep=False)
        self.add_contour('vase', 'lip','neck-right','shoulder-right','base-right','base-left','shoulder-left','neck-left', closed=True)
