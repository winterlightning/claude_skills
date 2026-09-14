"""parcel-delivery-truck: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ec7e42f-2776-5a70-a652-9140ef5c56c7'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_0ec7e42f-2776-5a70-a652-9140ef5c56c7.svg'
AUTHOR = 'gpt-6'


class ParcelDeliveryTruck(Solo48):
    icon_id = 'parcel-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('delivery truck', 'parcel', 'package', 'shipping', 'courier', 'logistics', 'truck', 'box')

    def build(self) -> None:

        # Cargo and cab share a bulkhead; wheel circles interrupt the chassis.
        self.add_polyline('cargo',(8,36),(6,36),(6,8),(12,8),(20,8),(26,8),(26,16),(26,24),(26,36),(16,36))
        self.add_polyline('cab',(26,16),(34,16),(40,24),(42,28),(42,36),(40,36))
        self.add_line('chassis',(26,36),(32,36))
        for side,cx in [('rear',12),('front',36)]:
            self.add_arc(side+'-top',(cx-4,36),(cx+4,36),radius_x=4)
            self.add_arc(side+'-bottom',(cx+4,36),(cx-4,36),radius_x=4)
            self.add_contour(side+'-wheel',side+'-top',side+'-bottom',closed=True)

        # The cargo box itself is the parcel; tape is intrinsic packaging detail.
        self.add_polyline('tape',(12,8),(12,18),(16,15),(20,18),(20,8))
        self.add_line('windscreen',(26,24),(40,24))
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
