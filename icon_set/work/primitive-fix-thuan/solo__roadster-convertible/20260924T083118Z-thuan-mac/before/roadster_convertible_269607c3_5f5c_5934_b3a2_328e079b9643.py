"""A right-facing roadster convertible with an open top and equal wheels. HRECT_L ink (6,6)-(42,42). Lucide bus and car-front informed the body/wheel relationship; direction and windscreen rake remain asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '269607c3-5f5c-5934-b3a2-328e079b9643'
SOURCE_PATH = 'pictographic-primitives/transportation/car convertible_269607c3-5f5c-5934-b3a2-328e079b9643.svg'
SOURCE_REFERENCES = (('269607c3-5f5c-5934-b3a2-328e079b9643', 'pictographic-primitives/transportation/car convertible_269607c3-5f5c-5934-b3a2-328e079b9643.svg'),)
AUTHOR = 'gpt-6'

class RoadsterConvertible(Solo48):
    icon_id = 'roadster-convertible'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('convertible', 'roadster', 'sports car', 'car', 'open top', 'cabriolet', 'vehicle', 'side view')

    def build(self) -> None:
        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-upper',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(side+'-lower',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('body-rear',(6,33),(6,20))
        self.add_line('body-top-a',(6,20),(22,20))
        self.add_line('body-top-b',(22,20),(34,20))
        self.add_arc('body-nose',(34,20),(42,30),radius_x=10)
        self.add_line('body-front',(42,30),(42,33))
        self.add_contour('body','body-rear','body-top-a','body-top-b','body-nose','body-front')
        self.add_line('chassis',(18,33),(30,33))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)

        self.add_polyline('windscreen',(22,20),(18,8),(34,20))
        self.relate('connect','windscreen','body')
