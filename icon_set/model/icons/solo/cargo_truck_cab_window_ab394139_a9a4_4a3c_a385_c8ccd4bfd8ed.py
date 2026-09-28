"""cargo-truck-cab-window: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab394139-a9a4-4a3c-a385-c8ccd4bfd8ed'
SOURCE_PATH = 'pictographic-primitives/transportation/truck cargo 1_ab394139-a9a4-4a3c-a385-c8ccd4bfd8ed.svg'
AUTHOR = 'gpt-6'


class CargoTruckCabWindow(Solo48):
    icon_id = 'cargo-truck-cab-window'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('cargo truck', 'truck', 'lorry', 'delivery', 'freight', 'logistics', 'shipping', 'vehicle')

    def build(self) -> None:

        # Cargo and cab share a bulkhead; wheel circles interrupt the chassis.
        self.add_polyline('cargo',(8,36),(4,36),(4,8),(26,8),(26,16),(26,24),(26,36),(16,36))
        self.add_polyline('cab',(26,16),(34,16),(40,24),(44,28),(44,36),(40,36))
        self.add_line('chassis',(26,36),(32,36))
        for side,cx in [('rear',12),('front',36)]:
            self.add_arc(side+'-top',(cx-4,36),(cx+4,36),radius_x=4)
            self.add_arc(side+'-bottom',(cx+4,36),(cx-4,36),radius_x=4)
            self.add_contour(side+'-wheel',side+'-top',side+'-bottom',closed=True)

        self.add_line('windscreen',(26,24),(40,24))
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
