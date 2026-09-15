"""A rounded square chip with two pins on each side. SQUARE centerline extremes (6,6)-(42,42). Lucide microchip informs the rounded body and regular connected leads; retain all eight source pins and blank body."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b5c422f-8509-4a8c-b6e7-26b6c0d4494b'
SOURCE_PATH = 'pictographic-primitives/symbol/microchip_2b5c422f-8509-4a8c-b6e7-26b6c0d4494b.svg'
AUTHOR = 'gpt-6'


class Microchip(Solo48):
    icon_id = 'microchip'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('microchip', 'chip', 'processor', 'cpu', 'hardware', 'electronics', 'circuit', 'semiconductor')

    def build(self) -> None:
        self.add_polyline('top',(16,12),(18,12),(30,12),(32,12))
        self.add_arc('tr',(32,12),(36,16),radius_x=4)
        self.add_line('right-a',(36,16),(36,18))
        self.add_line('right-b',(36,18),(36,30))
        self.add_line('right-c',(36,30),(36,32))
        self.add_arc('br',(36,32),(32,36),radius_x=4)
        self.add_polyline('bottom',(32,36),(30,36),(18,36),(16,36))
        self.add_arc('bl',(16,36),(12,32),radius_x=4)
        self.add_line('left-a',(12,32),(12,30))
        self.add_line('left-b',(12,30),(12,18))
        self.add_line('left-c',(12,18),(12,16))
        self.add_arc('tl',(12,16),(16,12),radius_x=4)
        for a,b in [('top','tr'),('tr','right-a'),('right-a','right-b'),('right-b','right-c'),('right-c','br'),('br','bottom'),('bottom','bl'),('bl','left-a'),('left-a','left-b'),('left-b','left-c'),('left-c','tl'),('tl','top')]:
            self.relate('connect',a,b)
        for x in [18,30]:
            self.add_line(f'pin-top-{x}',(x,6),(x,12))
            self.add_line(f'pin-bottom-{x}',(x,36),(x,42))
            self.relate('connect','top',f'pin-top-{x}')
            self.relate('connect','bottom',f'pin-bottom-{x}')
        for y in [18,30]:
            self.add_line(f'pin-left-{y}',(6,y),(12,y))
            self.add_line(f'pin-right-{y}',(36,y),(42,y))
            self.relate('connect','left-b',f'pin-left-{y}')
            self.relate('connect','right-b',f'pin-right-{y}')
