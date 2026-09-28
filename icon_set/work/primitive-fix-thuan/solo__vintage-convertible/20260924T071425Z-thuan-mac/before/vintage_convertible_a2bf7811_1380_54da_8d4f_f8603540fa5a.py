"""A right-facing vintage convertible with an open top and equal wheels. HRECT_L ink (6,6)-(42,42). Lucide bus and car-front informed the body/wheel relationship; direction and windscreen rake remain asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2bf7811-1380-54da-8d4f-f8603540fa5a'
SOURCE_PATH = 'pictographic-primitives/transportation/car convertible_a2bf7811-1380-54da-8d4f-f8603540fa5a.svg'
SOURCE_REFERENCES = (('a2bf7811-1380-54da-8d4f-f8603540fa5a', 'pictographic-primitives/transportation/car convertible_a2bf7811-1380-54da-8d4f-f8603540fa5a.svg'),)
AUTHOR = 'gpt-6'

class VintageConvertible(Solo48):
    icon_id = 'vintage-convertible'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('convertible', 'vintage', 'classic car', 'car', 'open top', 'roadster', 'vehicle', 'side view')

    def build(self) -> None:
        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-upper',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(side+'-lower',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('body-rear',(6,33),(6,20))
        self.add_line('body-top-a',(6,20),(24,20))
        self.add_line('body-top-b',(24,20),(34,20))
        self.add_arc('body-nose',(34,20),(42,30),radius_x=10)
        self.add_line('body-front',(42,30),(42,33))
        self.add_contour('body','body-rear','body-top-a','body-top-b','body-nose','body-front')
        self.add_line('chassis',(18,33),(30,33))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)

        self.add_polyline('windscreen',(24,20),(18,8),(15,8))
        self.relate('connect','windscreen','body')
