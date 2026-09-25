"""Headlight with Four Beams, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25506043-91fb-42e4-a4f9-382190c8628c'
SOURCE_PATH = 'pictographic-primitives/transportation/front fog lamp_25506043-91fb-42e4-a4f9-382190c8628c.svg'
AUTHOR = 'gpt-6'

class HeadlightFourBeams(Solo48):
    icon_id = 'headlight-four-beams'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('fog lamp', 'front fog light', 'headlight', 'lamp', 'beam', 'car', 'dashboard', 'indicator')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_line('lamp-back',(28,8),(28,40))
        self.add_arc('lamp-face',(28,40),(28,8),radius_x=16,sweep=False)
        self.add_contour('lamp','lamp-back','lamp-face',closed=True)
        for i in range(4):
            y=8+i*9
            self.add_line(f'beam-{i}',(18,y),(4,y+5))
