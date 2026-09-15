"""A wide oval speech bubble with a small pointed tail curling out at its lower left.

Plan: Elliptical bubble with an intrinsic lower-left tail and smooth crest.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: message-circle: coherent bubble and tail contour.
Simplification: No additional marks; directional tail retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a392865-4569-47ef-8d05-e46454c31157'
SOURCE_PATH = 'pictographic-primitives/logos/google talk logo_1a392865-4569-47ef-8d05-e46454c31157.svg'
AUTHOR = 'gpt-6'


class GoogleTalkLogo(Solo48):
    icon_id = 'google-talk-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-talk', 'gtalk', 'google', 'chat', 'speech-bubble', 'logo', 'brand')

    def build(self):
        self.add_arc('top',(4,24),(44,24),radius_x=20,radius_y=16)
        self.add_bezier('right',(44,24),((44,34),(33,37),(22,36)))
        self.add_line('tail-bottom',(22,36),(8,40))
        self.add_line('tail-rise',(8,40),(12,32))
        self.add_bezier('left',(12,32),((7,30),(4,27),(4,24)))
        self.add_contour('bubble','top','right','tail-bottom','tail-rise','left',closed=True)
