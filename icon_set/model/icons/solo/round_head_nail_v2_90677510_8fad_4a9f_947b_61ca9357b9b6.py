"""An upright nail with a true semicircular domed cap and pointed shank; reoriented to preserve a smooth readable round head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90677510-8fad-4a9f-947b-61ca9357b9b6'
SOURCE_PATH = 'pictographic-primitives/tools/hardware nail round head_90677510-8fad-4a9f-947b-61ca9357b9b6.svg'
AUTHOR = 'gpt-6'

class RoundHeadNailVariant2(Solo48):
    icon_id = 'round-head-nail-v2'
    variant_of = 'round-head-nail'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('nail', 'round head', 'hardware', 'fastener', 'pin', 'construction', 'carpentry', 'metal')

    def build(self) -> None:
        self.add_arc('dome', (8, 20), (40, 20), radius_x=16)
        self.add_line('cap-base', (40, 20), (8, 20))
        self.add_contour('cap', 'dome', 'cap-base', closed=True)
        self.add_polyline('shank', (20, 20), (20, 36), (24, 44), (28, 36), (28, 20))
        self.relate('connect', 'shank', 'cap')
