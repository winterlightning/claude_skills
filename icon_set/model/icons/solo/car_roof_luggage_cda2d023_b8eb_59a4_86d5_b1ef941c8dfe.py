"""A hatchback carrying a roof box, with split side windows and round wheels. Square keyshape provides cargo height. Lucide bus and car-front informed shared joins; luggage handle and straps omitted for clarity."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cda2d023-b8eb-59a4-86d5-b1ef941c8dfe'
SOURCE_PATH = 'pictographic-primitives/transportation/car luggage_cda2d023-b8eb-59a4-86d5-b1ef941c8dfe.svg'
SOURCE_REFERENCES = (('cda2d023-b8eb-59a4-86d5-b1ef941c8dfe', 'pictographic-primitives/transportation/car luggage_cda2d023-b8eb-59a4-86d5-b1ef941c8dfe.svg'),)
AUTHOR = 'gpt-6'

class CarRoofLuggage(Solo48):
    icon_id = 'car-roof-luggage'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'luggage', 'roof rack', 'travel', 'road trip', 'vacation', 'baggage', 'vehicle')

    def build(self) -> None:
        self.add_line('back',(6,36),(6,28))
        self.add_arc('back-corner',(6,28),(10,24),radius_x=4)
        self.add_line('top-a',(10,24),(22,24))
        self.add_line('top-b',(22,24),(36,24))
        self.add_line('top-c',(36,24),(38,24))
        self.add_arc('nose',(38,24),(42,28),radius_x=4)
        self.add_line('front',(42,28),(42,36))
        self.add_contour('body','back','back-corner','top-a','top-b','top-c','nose','front')
        self.add_polyline('cabin',(10,24),(14,16),(16,16),(22,16),(28,16),(30,16),(36,24))
        self.add_polyline('luggage',(16,16),(16,6),(28,6),(28,16))
        self.add_line('pillar',(22,16),(22,24))
        for a,b in [('cabin','body'),('luggage','cabin'),('pillar','cabin'),('pillar','body')]:
            self.relate('connect',a,b)

        for side,x in [('rear',12),('front',36)]:
            self.add_arc(side+'-upper',(x-6,36),(x+6,36),radius_x=6)
            self.add_arc(side+'-lower',(x+6,36),(x-6,36),radius_x=6)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('chassis',(18,36),(30,36))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)
