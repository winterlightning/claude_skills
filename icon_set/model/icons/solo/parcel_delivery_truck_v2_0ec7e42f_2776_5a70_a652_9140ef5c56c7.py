# Variant of parcel-delivery-truck; parent file remains unchanged.
'Parcel delivery truck: independent spacing revision.\n\nUse the cargo box as the parcel; omit cramped tape and deepen cab bands.\nNative solo family, HRECT_L keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0ec7e42f-2776-5a70-a652-9140ef5c56c7'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_0ec7e42f-2776-5a70-a652-9140ef5c56c7.svg'
AUTHOR = 'gpt-6'

class ParcelDeliveryTruckVariant2(Solo48):
    icon_id = 'parcel-delivery-truck-v2'
    variant_of = 'parcel-delivery-truck'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('delivery truck', 'parcel', 'package', 'shipping', 'courier', 'logistics', 'truck', 'box')

    def build(self):
        self.add_polyline('cargo',(8, 36),(4, 36),(4, 8),(24, 8),(24, 16),(24, 24),(24, 36),(16, 36),closed=False)
        self.add_polyline('cab',(24, 16),(34, 16),(42, 24),(44, 26),(44, 36),(40, 36),closed=False)
        self.add_line('chassis',(24, 36),(32, 36))
        self.add_line('windscreen',(24, 24),(42, 24))
        self.add_arc('rear-wheela',(8, 36),(16, 36),radius_x=4,radius_y=4)
        self.add_arc('rear-wheelb',(16, 36),(8, 36),radius_x=4,radius_y=4)
        self.add_contour('rear-wheel','rear-wheela','rear-wheelb',closed=True)
        self.add_arc('front-wheela',(32, 36),(40, 36),radius_x=4,radius_y=4)
        self.add_arc('front-wheelb',(40, 36),(32, 36),radius_x=4,radius_y=4)
        self.add_contour('front-wheel','front-wheela','front-wheelb',closed=True)
        self.relate('connect','cargo','cab')
        self.relate('connect','cargo','chassis')
        self.relate('connect','cargo','windscreen')
        self.relate('connect','cab','windscreen')
        self.relate('connect','cargo','rear-wheel')
        self.relate('connect','cab','front-wheel')
        self.relate('connect','chassis','front-wheel')
