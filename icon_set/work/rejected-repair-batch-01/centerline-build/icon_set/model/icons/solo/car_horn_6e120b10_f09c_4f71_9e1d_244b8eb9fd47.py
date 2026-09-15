"""Car Horn, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6e120b10-f09c-4f71-9e1d-244b8eb9fd47'
SOURCE_PATH = 'pictographic-primitives/transportation/horn_6e120b10-f09c-4f71-9e1d-244b8eb9fd47.svg'
AUTHOR = 'gpt-6'

class CarHorn(Solo48):
    icon_id = 'car-horn'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('horn', 'car horn', 'sound', 'honk', 'dashboard', 'trumpet', 'alert', 'vehicle')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_polyline('bell',(4,16),(18,24),(4,32),closed=True)
        self.add_polyline('tube',(18,24),(28,24),(40,24),(42,24))
        self.relate('connect','bell','tube')
        self.add_line('loop-left',(28,24),(28,34))
        self.add_arc('loop-bottom-left',(28,34),(34,40),radius_x=6,sweep=False)
        self.add_arc('loop-bottom-right',(34,40),(40,34),radius_x=6,sweep=False)
        self.add_line('loop-right',(40,34),(40,24))
        self.add_contour('loop','loop-left','loop-bottom-left','loop-bottom-right','loop-right')
        self.relate('connect','tube','loop')
        for i,x in enumerate((28,40)):self.add_line(f'sound-{i}',(x,8),(x+4,8))
