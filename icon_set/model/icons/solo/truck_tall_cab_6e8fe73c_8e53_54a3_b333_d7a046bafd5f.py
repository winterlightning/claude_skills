"""truck-tall-cab: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6e8fe73c-8e53-54a3-b333-d7a046bafd5f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck empty_6e8fe73c-8e53-54a3-b333-d7a046bafd5f.svg'
AUTHOR = 'gpt-6'


class TruckTallCab(Solo48):
    icon_id = 'truck-tall-cab'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('truck', 'lorry', 'delivery', 'cargo', 'empty truck', 'logistics', 'transport', 'vehicle')

    def build(self) -> None:

        # Cargo and cab share a bulkhead; wheel circles interrupt the chassis.
        self.add_polyline('cargo',(8,36),(4,36),(4,8),(26,8),(26,10),(26,36),(16,36))
        self.add_polyline('cab',(26,10),(36,10),(44,28),(44,36),(40,36))
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
