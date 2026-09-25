"""Dipped Beam Headlight, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b71e3293-bfe9-526b-befc-92e473ba2f28'
SOURCE_PATH = 'pictographic-primitives/transportation/dribbed beam_b71e3293-bfe9-526b-befc-92e473ba2f28.svg'
AUTHOR = 'gpt-6'

class DippedBeamHeadlight(Solo48):
    icon_id = 'dipped-beam-headlight'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('dipped beam', 'low beam', 'headlight', 'lamp', 'car', 'dashboard', 'lighting', 'indicator')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_line('lamp-back',(28,8),(28,40))
        self.add_arc('lamp-face',(28,40),(28,8),radius_x=16,sweep=False)
        self.add_contour('lamp','lamp-back','lamp-face',closed=True)
        for i in range(3):
            y=10+i*11
            self.add_line(f'beam-{i}',(18,y),(4,y+7))
