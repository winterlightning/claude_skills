"""panel-van: reconstructed on SOLO48 from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3179d20f-4838-4c26-a054-f8bbabbc255f'
SOURCE_PATH = 'pictographic-primitives/transportation/truck_3179d20f-4838-4c26-a054-f8bbabbc255f.svg'
AUTHOR = 'gpt-6'


class PanelVan(Solo48):
    icon_id = 'panel-van'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('van', 'panel van', 'delivery van', 'vehicle', 'transport', 'cargo', 'courier', 'side view')

    def build(self) -> None:

        # Continuous van body with a lowered front roof; no separate cargo bulkhead.
        self.add_polyline('body-rear',(8,36),(6,36),(6,8),(26,8),(26,14),(32,14))
        self.add_arc('nose',(32,14),(42,26),radius_x=12)
        self.add_polyline('body-front',(42,26),(42,36),(40,36))
        self.add_line('chassis',(16,36),(32,36))

        for side,cx in [('rear',12),('front',36)]:
            self.add_arc(side+'-top',(cx-4,36),(cx+4,36),radius_x=4)
            self.add_arc(side+'-bottom',(cx+4,36),(cx-4,36),radius_x=4)
            self.add_contour(side+'-wheel',side+'-top',side+'-bottom',closed=True)
        # Declare only genuine shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
