"""Fire Engine, re-authored from its reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '31f8b08a-6a09-5ddf-b750-a5c59e1c4ea2'
SOURCE_PATH = 'pictographic-primitives/transportation/firefighter truck_31f8b08a-6a09-5ddf-b750-a5c59e1c4ea2.svg'
AUTHOR = 'gpt-6'

class FireEngine(Solo48):
    icon_id = 'fire-engine'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('fire engine', 'fire truck', 'firefighter', 'emergency', 'ladder', 'truck', 'rescue', 'vehicle')

    def build(self) -> None:
        # Current contract centerline extremes: (6,8)-(42,40).
        for i,x in enumerate((10,38)):
            self.add_arc(f'wheel-{i}-a',(x-4,36),(x+4,36),radius_x=4)
            self.add_arc(f'wheel-{i}-b',(x+4,36),(x-4,36),radius_x=4)
            self.add_contour(f'wheel-{i}',f'wheel-{i}-a',f'wheel-{i}-b',closed=True)
        self.add_polyline('body',(6,36),(6,36),(6,20),(12,20),(20,20),(28,20),(28,16),(36,16),(42,26),(42,36),(42,36))
        self.add_line('sill',(14,36),(34,36))
        for i in range(2):
            self.relate('connect','body',f'wheel-{i}')
            self.relate('connect','sill',f'wheel-{i}')
        self.add_polyline('ladder-rail',(6,8),(12,8),(20,8),(28,8))
        for x in (12,20):
            self.add_line(f'ladder-rung-{x}',(x,8),(x,20))
            self.relate('connect',f'ladder-rung-{x}','ladder-rail')
            self.relate('connect',f'ladder-rung-{x}','body')
        self.add_line('beacon',(36,8),(36,16))
        self.relate('connect','beacon','body')
