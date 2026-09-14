# Variant of girl-pigtails; parent file remains unchanged.
"""Girl with round head, paired pigtails and an open arched body. Lucide user-round informs head and body; pigtails preserve source identity.

SOLO48 VRECT_L; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ddb0eed3-f53e-4197-a297-1e088901b5ff'
SOURCE_PATH = 'pictographic-primitives/symbol/primitive symbols human_ddb0eed3-f53e-4197-a297-1e088901b5ff.svg'
AUTHOR = 'gpt-6'

class GirlPigtailsVariant2(Solo48):
    icon_id = 'girl-pigtails-v2'
    variant_of = 'girl-pigtails'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('girl', 'woman', 'female', 'person', 'child', 'pigtails', 'figure', 'user')

    def build(self) -> None:
        self.add_arc('head-top', (15, 13), (33, 13), radius_x=9)
        self.add_arc('head-bottom', (33, 13), (15, 13), radius_x=9)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        for side, sign in [('left', -1), ('right', 1)]:
            self.add_arc('pigtail-' + side, (24 + sign * 9, 13), (24 + sign * 16, 21), radius_x=10, sweep=sign < 0)
            self.relate('connect', 'head', 'pigtail-' + side)
        self.add_line('body-left', (8, 42), (14, 37))
        self.add_arc('body-top', (14, 37), (34, 37), radius_x=12, radius_y=9)
        self.add_line('body-right', (34, 37), (40, 42))
        self.add_contour('body', 'body-left', 'body-top', 'body-right')
