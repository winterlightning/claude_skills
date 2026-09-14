# Review candidate; original preserved.
"""Star-labelled decorative bottle with a deeper cap opening. VRECT_L preserves the bottle proportions and intrinsic label."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/decoration bottle_e0f7f6c1-f633-5b90-9f71-aac0f4ec1dce.svg'
AUTHOR = 'gpt-6'

class StarLabelledBottle(Solo48):
    icon_id = 'star-labelled-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('bottle', 'star', 'cap', 'container', 'label', 'decor', 'vessel')

    def build(self) -> None:
        """Opening repair: Deepened the cap band, moving both shoulder junctions together and retaining the star label."""
        self.add_polyline('neck', (16, 14), (16, 6), (32, 6), (32, 14))
        self.add_line('cap-bottom', (16, 14), (32, 14))
        self.add_arc('shoulder-right', (32, 14), (40, 22), radius_x=8)
        self.add_line('body-right', (40, 22), (40, 40))
        self.add_arc('base-right', (40, 40), (34, 42), radius_x=6)
        self.add_line('base', (34, 42), (14, 42))
        self.add_arc('base-left', (14, 42), (8, 40), radius_x=6)
        self.add_line('body-left', (8, 40), (8, 22))
        self.add_arc('shoulder-left', (8, 22), (16, 14), radius_x=8)
        self.add_contour('body', 'shoulder-right', 'body-right', 'base-right', 'base', 'base-left', 'body-left', 'shoulder-left')
        self.relate('connect', 'neck', 'body')
        self.relate('connect', 'neck', 'cap-bottom')
        self.add_polyline('star', (24, 21), (27, 27), (33, 28), (29, 33), (30, 39), (24, 36), (18, 39), (19, 33), (15, 28), (21, 27), closed=True)
