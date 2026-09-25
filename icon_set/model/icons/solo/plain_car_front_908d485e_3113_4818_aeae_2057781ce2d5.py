"""A car front with an unmarked face and straight wheel stubs. SQUARE ink (6,6)-(42,42). Lucide car-front informed mirrored geometry; the reference light and wheel treatment remains distinct."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '908d485e-3113-4818-aeae-2057781ce2d5'
SOURCE_PATH = 'pictographic-primitives/transportation/car 1_908d485e-3113-4818-aeae-2057781ce2d5.svg'
SOURCE_REFERENCES = (('908d485e-3113-4818-aeae-2057781ce2d5', 'pictographic-primitives/transportation/car 1_908d485e-3113-4818-aeae-2057781ce2d5.svg'), ('8156415b-cbe0-4085-a1b2-de1314bf33de', 'pictographic-primitives/transportation/car_8156415b-cbe0-4085-a1b2-de1314bf33de.svg'), ('b90b17e9-30a0-4203-bb54-82de55a03dae', 'pictographic-primitives/transportation/car_b90b17e9-30a0-4203-bb54-82de55a03dae.svg'))
AUTHOR = 'gpt-6'

class PlainCarFront(Solo48):
    icon_id = 'plain-car-front'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('car', 'front', 'vehicle', 'automobile', 'simple', 'sedan', 'driving', 'head-on')

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

        for side,x in [('left',10),('right',38)]:
            self.add_line(side+'-wheel',(x,36),(x,42))
            self.relate('connect',side+'-wheel','body')
