"""small-delivery-truck: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cc6a052-bd85-4786-ad57-af8947d75c17'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_1cc6a052-bd85-4786-ad57-af8947d75c17.svg'
AUTHOR = 'gpt-6'


class SmallDeliveryTruck(Solo48):
    icon_id = 'small-delivery-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('truck', 'delivery', 'lorry', 'cargo', 'shipping', 'logistics', 'transport', 'vehicle')

    def build(self) -> None:

        # Long cargo box and a quarter-circle cab nose; equal wheels interrupt the chassis.
        self.add_polyline('cargo',(8,36),(6,36),(6,8),(26,8),(26,16),(26,36),(16,36))

        self.add_line('cab-roof',(26,16),(32,16))
        self.add_arc('cab-nose',(32,16),(42,28),radius_x=12)
        self.add_polyline('cab-bottom',(42,28),(42,36),(40,36))
        self.add_line('chassis',(26,36),(32,36))

        for side,cx in [('rear',12),('front',36)]:
            self.add_arc(side+'-top',(cx-4,36),(cx+4,36),radius_x=4)
            self.add_arc(side+'-bottom',(cx+4,36),(cx-4,36),radius_x=4)
            self.add_contour(side+'-wheel',side+'-top',side+'-bottom',closed=True)
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)

ADDITIONAL_SOURCE_ICON_ID_2 = '7fa4b356-9d73-4875-94fd-29e892bef9d8'
ADDITIONAL_SOURCE_PATH_2 = 'pictographic-primitives/transportation/truck_7fa4b356-9d73-4875-94fd-29e892bef9d8.svg'

ADDITIONAL_SOURCE_ICON_ID_3 = 'ee45281c-9d60-448b-b6b0-b5db76f72c3b'
ADDITIONAL_SOURCE_PATH_3 = 'pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
