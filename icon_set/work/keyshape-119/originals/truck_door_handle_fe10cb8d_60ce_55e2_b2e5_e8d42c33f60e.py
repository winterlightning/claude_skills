"""truck-door-handle: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fe10cb8d-60ce-55e2-b2e5-e8d42c33f60e'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_fe10cb8d-60ce-55e2-b2e5-e8d42c33f60e.svg'
AUTHOR = 'gpt-6'


class TruckDoorHandle(Solo48):
    icon_id = 'truck-door-handle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('truck', 'delivery', 'lorry', 'cargo', 'moving', 'logistics', 'transport', 'vehicle')

    def build(self) -> None:

        # Rounded cargo corners and one vertical door handle distinguish this truck.
        self.add_polyline('cargo-rear',(8,36),(6,36),(6,12))
        self.add_arc('cargo-tl',(6,12),(8,8),radius_x=4)
        self.add_line('cargo-roof',(8,8),(22,8))
        self.add_arc('cargo-tr',(22,8),(26,12),radius_x=4)
        self.add_polyline('cargo-front',(26,12),(26,16),(26,36),(16,36))
        self.add_line('handle',(15,18),(15,23))

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
