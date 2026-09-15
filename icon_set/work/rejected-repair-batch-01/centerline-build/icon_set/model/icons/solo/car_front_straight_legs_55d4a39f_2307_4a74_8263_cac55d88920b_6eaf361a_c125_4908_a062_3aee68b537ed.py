"""A car front with slot headlights and straight wheel stubs. SQUARE ink (6,6)-(42,42). Lucide car-front informed mirrored geometry; the reference light and wheel treatment remains distinct."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55d4a39f-2307-4a74-8263-cac55d88920b'
SOURCE_PATH = 'pictographic-primitives/transportation/car 1_55d4a39f-2307-4a74-8263-cac55d88920b.svg'
SOURCE_REFERENCES = (('55d4a39f-2307-4a74-8263-cac55d88920b', 'pictographic-primitives/transportation/car 1_55d4a39f-2307-4a74-8263-cac55d88920b.svg'), ('6eaf361a-c125-4908-a062-3aee68b537ed', 'pictographic-primitives/transportation/car 1_6eaf361a-c125-4908-a062-3aee68b537ed.svg'))
AUTHOR = 'gpt-6'

class CarFrontStraightLegs(Solo48):
    icon_id = 'car-front-straight-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('car', 'front', 'vehicle', 'automobile', 'headlights', 'sedan', 'driving', 'head-on')

    def build(self) -> None:
        self.add_line('body-top-0',(8, 18),(10, 18))
        self.add_line('body-top-1',(10, 18),(38, 18))
        self.add_line('body-top-2',(38, 18),(40, 18))
        self.add_arc('body-top-corner',(40, 18),(42, 20),radius_x=2)
        self.add_line('body-right-0',(42, 20),(42, 27))
        self.add_line('body-right-1',(42, 27),(42, 34))
        self.add_arc('body-right-corner',(42, 34),(40, 36),radius_x=2)
        self.add_line('body-bottom-0',(40, 36),(38, 36))
        self.add_line('body-bottom-1',(38, 36),(32, 36))
        self.add_line('body-bottom-2',(32, 36),(16, 36))
        self.add_line('body-bottom-3',(16, 36),(10, 36))
        self.add_line('body-bottom-4',(10, 36),(8, 36))
        self.add_arc('body-bottom-corner',(8, 36),(6, 34),radius_x=2)
        self.add_line('body-left-0',(6, 34),(6, 27))
        self.add_line('body-left-1',(6, 27),(6, 20))
        self.add_arc('body-left-corner',(6, 20),(8, 18),radius_x=2)
        self.add_contour('body','body-top-0','body-top-1','body-top-2','body-top-corner','body-right-0','body-right-1','body-right-corner','body-bottom-0','body-bottom-1','body-bottom-2','body-bottom-3','body-bottom-4','body-bottom-corner','body-left-0','body-left-1','body-left-corner',closed=True)
        self.add_polyline('cabin',(10,18),(16,6),(32,6),(38,18))
        self.relate('connect','cabin','body')
        self.add_line('left-light',(15,27),(17,27))
        self.add_line('right-light',(31,27),(33,27))

        for side,x in [('left',10),('right',38)]:
            self.add_line(side+'-wheel',(x,36),(x,42))
            self.relate('connect',side+'-wheel','body')
