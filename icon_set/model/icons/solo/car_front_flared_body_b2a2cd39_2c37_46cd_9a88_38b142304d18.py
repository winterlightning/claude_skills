"""A head-on car with flared body sides, paired light slots and straight wheel stubs. Square envelope supports the cabin and face. Lucide car-front informed bilateral construction; no extra details."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b2a2cd39-2c37-46cd-9a88-38b142304d18'
SOURCE_PATH = 'pictographic-primitives/transportation/car_b2a2cd39-2c37-46cd-9a88-38b142304d18.svg'
SOURCE_REFERENCES = (('b2a2cd39-2c37-46cd-9a88-38b142304d18', 'pictographic-primitives/transportation/car_b2a2cd39-2c37-46cd-9a88-38b142304d18.svg'),)
AUTHOR = 'gpt-6'

class CarFrontFlaredBody(Solo48):
    icon_id = 'car-front-flared-body'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'front', 'vehicle', 'automobile', 'headlights', 'sedan', 'driving', 'head-on')

    def build(self) -> None:
        self.add_polyline('body',(10,18),(38,18),(42,26),(42,36),(38,36),(10,36),(6,36),(6,26),(10,18),closed=True)
        self.add_polyline('cabin',(10,18),(16,6),(32,6),(38,18))
        self.relate('connect','cabin','body')
        for x in (10,38):
            self.add_line(f'wheel-{x}',(x,36),(x,42))
            self.relate('connect',f'wheel-{x}','body')
        self.add_line('left-light',(16,27),(18,27))
        self.add_line('right-light',(30,27),(32,27))
