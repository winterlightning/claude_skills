# Variant of star-labelled-bottle; parent file remains unchanged.
"""A capped decorative bottle carrying a five-pointed star on its broad body."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/decoration bottle_e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce.svg'
AUTHOR = 'gpt-6'

class StarLabelledBottleVariant4(Solo48):
    icon_id = 'star-labelled-bottle-v4'
    variant_of = 'star-labelled-bottle'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('bottle', 'star', 'cap', 'container', 'label', 'decor', 'vessel')

    def build(self) -> None:
        self.add_polyline('neck', (16, 12), (16, 6), (32, 6), (32, 12))
        self.add_line('cap-bottom', (16, 8), (32, 8))
        self.add_arc('shoulder-right', (32, 12), (40, 20), radius_x=8)
        self.add_line('body-right', (40, 20), (40, 40))
        self.add_arc('base-right', (40, 40), (34, 42), radius_x=6)
        self.add_line('base', (34, 42), (14, 42))
        self.add_arc('base-left', (14, 42), (8, 40), radius_x=6)
        self.add_line('body-left', (8, 40), (8, 20))
        self.add_arc('shoulder-left', (8, 20), (16, 12), radius_x=8)
        self.add_contour('body', 'shoulder-right', 'body-right', 'base-right', 'base', 'base-left', 'body-left', 'shoulder-left')
        self.relate('connect', 'neck', 'body')
        self.relate('connect', 'neck', 'cap-bottom')
        self.add_polyline('star', (24, 21), (27, 27), (33, 28), (29, 33), (30, 39), (24, 36), (18, 39), (19, 33), (15, 28), (21, 27), closed=True)
