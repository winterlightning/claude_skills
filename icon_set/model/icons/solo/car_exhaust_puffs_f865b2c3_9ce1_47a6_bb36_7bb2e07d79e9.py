"""Car with Exhaust Puffs, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f865b2c3-9ce1-47a6-bb36-7bb2e07d79e9'
SOURCE_PATH = 'pictographic-primitives/transportation/low emission zone_f865b2c3-9ce1-47a6-bb36-7bb2e07d79e9.svg'
AUTHOR = 'gpt-6'

class CarExhaustPuffs(Solo48):
    icon_id = 'car-exhaust-puffs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('low emission zone', 'emissions', 'exhaust', 'pollution', 'car', 'smog', 'environment', 'traffic')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        self.add_line('cloud-top',(8,8),(12,8))
        self.add_arc('cloud-right',(12,8),(12,16),radius_x=4)
        self.add_line('cloud-bottom',(12,16),(8,16))
        self.add_arc('cloud-left',(8,16),(8,8),radius_x=4)
        self.add_contour('cloud','cloud-top','cloud-right','cloud-bottom','cloud-left',closed=True)
        self.add_arc('puff-a',(8,25),(8,31),radius_x=3)
        self.add_arc('puff-b',(8,31),(8,25),radius_x=3)
        self.add_contour('puff','puff-a','puff-b',closed=True)
        self.add_polyline('car',(20,28),(24,18),(40,18),(44,28),(44,38),(40,38),(24,38),(20,38),closed=True)
        self.add_line('windscreen-base',(20,28),(44,28))
        self.relate('connect','windscreen-base','car')
        for x in (24,40):
            self.add_line(f'wheel-{x}',(x,38),(x,40))
            self.relate('connect',f'wheel-{x}','car')
