"""A quad bike with dipped saddle, high front handlebar and equal wheels. HRECT_L ink (6,6)-(42,42). Lucide car-front informs coherent body contour; wheel hubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3f07500-0d8f-5bbb-b806-122fe5e29847'
SOURCE_PATH = 'pictographic-primitives/transportation/atv_b3f07500-0d8f-5bbb-b806-122fe5e29847.svg'
AUTHOR = 'gpt-6'

class QuadBike(Solo48):
    icon_id = 'quad-bike'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('atv', 'quad', 'quad bike', 'off-road', 'vehicle', 'four wheeler', 'offroad', 'motor')

    def build(self) -> None:
        wheel_y, radius = 34, 6
        for side,x in [('rear',10),('front',38)]:
            self.add_arc(side+'-upper',(x-radius,wheel_y),(x+radius,wheel_y),radius_x=radius)
            self.add_arc(side+'-lower',(x+radius,wheel_y),(x-radius,wheel_y),radius_x=radius)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_polyline('body',(6,19),(16,16),(16,20),(25,20),(28,18),(42,18))
        self.add_polyline('handlebar',(24,8),(31,8),(37,18))
        self.relate('connect','handlebar','body')
