"""A right-facing convertible headrests with an open top and equal wheels. HRECT_L ink (6,6)-(42,42). Lucide bus and car-front informed the body/wheel relationship; direction and windscreen rake remain asymmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85ddde90-3454-5c65-9d3d-9b0de881db43'
SOURCE_PATH = 'pictographic-primitives/transportation/car convertible_85ddde90-3454-5c65-9d3d-9b0de881db43.svg'
SOURCE_REFERENCES = (('85ddde90-3454-5c65-9d3d-9b0de881db43', 'pictographic-primitives/transportation/car convertible_85ddde90-3454-5c65-9d3d-9b0de881db43.svg'),)
AUTHOR = 'gpt-6'

class ConvertibleHeadrests(Solo48):
    icon_id = 'convertible-headrests'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('convertible', 'cabriolet', 'sports car', 'car', 'open top', 'headrest', 'vehicle', 'side view')

    def build(self) -> None:
        for side,x in [('rear',11),('front',37)]:
            self.add_arc(side+'-upper',(x-7,33),(x+7,33),radius_x=7)
            self.add_arc(side+'-lower',(x+7,33),(x-7,33),radius_x=7)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_line('body-rear',(6,33),(6,20))
        self.add_line('body-top-a',(6,20),(6,20))
        self.add_line('body-top-a1',(6,20),(14,20))
        self.add_line('body-top-a2',(14,20),(23,20))
        self.add_line('body-top-b',(23,20),(34,20))
        self.add_arc('body-nose',(34,20),(42,30),radius_x=10)
        self.add_line('body-front',(42,30),(42,33))
        self.add_contour('body','body-rear','body-top-a','body-top-a1','body-top-a2','body-top-b','body-nose','body-front')
        self.add_line('chassis',(18,33),(30,33))
        for wheel in ['rear-wheel','front-wheel']:
            self.relate('connect','body',wheel)
            self.relate('connect','chassis',wheel)

        self.add_polyline('windscreen',(23,20),(22,8),(34,20))
        self.relate('connect','windscreen','body')
        self.add_line('headrest-left',(6,20),(6,16))
        self.add_arc('headrest-top',(6,16),(14,16),radius_x=4)
        self.add_line('headrest-right',(14,16),(14,20))
        self.add_contour('headrest','headrest-left','headrest-top','headrest-right')
        self.relate('connect','headrest','body')
