"""Mountain bike; independently authored for SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa35ff1c-87d6-48ea-9de4-8d86f4664447'
SOURCE_PATH = 'pictographic-primitives/transportation/mountain bike_aa35ff1c-87d6-48ea-9de4-8d86f4664447.svg'
AUTHOR = 'gpt-6'

class MountainBike(Solo48):
    icon_id = 'mountain-bike'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('mountain bike', 'mtb', 'bicycle', 'cycling', 'off-road')

    def build(self) -> None:
        # HRECT_L (6,8)-(42,40); equal radius-8 wheels on a shared y=32 baseline.
        for name,cx in (('rear',12),('front',36)):
            self.add_arc(name+'-right', (cx,24), (cx,40), radius_x=8)
            self.add_arc(name+'-left', (cx,40), (cx,24), radius_x=8)
            self.add_contour(name+'-wheel', name+'-right', name+'-left', closed=True)
        self.add_polyline('rear-stay', (12,32), (12,24), (20,20))
        self.relate('connect','rear-stay','rear-wheel')
        self.add_polyline('seat-post', (20,20), (20,8))
        self.add_polyline('saddle', (16,8), (20,8), (24,8))
        self.relate('connect','saddle','seat-post')
        self.relate('connect','seat-post','rear-stay')
        self.add_line('top-tube',(20,20),(36,16))
        self.relate('connect','top-tube','rear-stay')
        self.relate('connect','top-tube','seat-post')
        self.add_polyline('fork',(36,8),(36,16),(36,24),(36,32))
        self.relate('connect','fork','top-tube')
        self.relate('connect','fork','front-wheel')
        self.add_polyline('handlebar',(32,8),(36,8),(40,8))
        self.relate('connect','handlebar','fork')
