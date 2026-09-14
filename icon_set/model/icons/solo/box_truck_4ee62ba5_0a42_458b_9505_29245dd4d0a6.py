"""box-truck: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee62ba5-0a42-458b-9505-29245dd4d0a6'
SOURCE_PATH = 'pictographic-primitives/transportation/truck 2_4ee62ba5-0a42-458b-9505-29245dd4d0a6.svg'
AUTHOR = 'gpt-6'


class BoxTruck(Solo48):
    icon_id = 'box-truck'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('truck', 'box truck', 'delivery', 'lorry', 'cargo', 'shipping', 'logistics', 'vehicle')

    def build(self) -> None:

        # Cargo and cab share a bulkhead; wheel circles interrupt the chassis.
        self.add_polyline('cargo',(8,36),(6,36),(6,8),(26,8),(26,16),(26,36),(16,36))
        self.add_polyline('cab',(26,16),(34,16),(42,28),(42,36),(40,36))
        self.add_line('chassis',(26,36),(32,36))
        for side,cx in [('rear',12),('front',36)]:
            self.add_arc(side+'-top',(cx-4,36),(cx+4,36),radius_x=4)
            self.add_arc(side+'-bottom',(cx+4,36),(cx-4,36),radius_x=4)
            self.add_contour(side+'-wheel',side+'-top',side+'-bottom',closed=True)
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)

# Equivalent second supplied reference, retained for future source-ID lookup.
ADDITIONAL_SOURCE_ICON_ID = 'f2efc44d-db38-430e-95d2-cf55974a8afa'
ADDITIONAL_SOURCE_PATH = 'pictographic-primitives/transportation/truck 2_f2efc44d-db38-430e-95d2-cf55974a8afa.svg'
