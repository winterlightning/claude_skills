"""Full Beam Headlight, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a72fb797-0d03-574b-b30f-bf31db1a936f'
SOURCE_PATH = 'pictographic-primitives/transportation/full beam_a72fb797-0d03-574b-b30f-bf31db1a936f.svg'
AUTHOR = 'gpt-6'

class FullBeamHeadlight(Solo48):
    icon_id = 'full-beam-headlight'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('full beam', 'high beam', 'main beam', 'headlight', 'lamp', 'car', 'dashboard', 'indicator')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_line('lamp-back',(28,8),(28,40))
        self.add_arc('lamp-face',(28,40),(28,8),radius_x=16,sweep=False)
        self.add_contour('lamp','lamp-back','lamp-face',closed=True)
        for i in range(3):
            y=14+i*10
            self.add_line(f'beam-{i}',(4,y),(18,y))
