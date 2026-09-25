"""An upright nail with a true semicircular domed cap and pointed shank; reoriented to preserve a smooth readable round head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90677510-8fad-4a9f-947b-61ca9357b9b6'
SOURCE_PATH = 'pictographic-primitives/tools/hardware nail round head_90677510-8fad-4a9f-947b-61ca9357b9b6.svg'
AUTHOR = 'gpt-6'

class RoundHeadNail(Solo48):
    icon_id = 'round-head-nail'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('nail', 'round head', 'hardware', 'fastener', 'pin', 'construction', 'carpentry', 'metal')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_arc('dome', (8, 20), (40, 20), radius_x=16)
        self.add_line('cap-base', (40, 20), (8, 20))
        self.add_contour('cap', 'dome', 'cap-base', closed=True)
        self.add_polyline('shank', (20, 20), (20, 36), (24, 44), (28, 36), (28, 20))
        self.relate('connect', 'shank', 'cap')
