"""caravan-trailer: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b1dccdf-5c5f-4038-9afe-6ed2a5d15b99'
SOURCE_PATH = 'pictographic-primitives/transportation/trailer_7b1dccdf-5c5f-4038-9afe-6ed2a5d15b99.svg'
AUTHOR = 'gpt-6'


class CaravanTrailer(Solo48):
    icon_id = 'caravan-trailer'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('caravan', 'trailer', 'camper', 'rv', 'travel', 'camping', 'tow', 'holiday')

    def build(self) -> None:

        # Rounded shell, single window and a wheel meeting the lower edge.
        self.add_line('roof',(8,8),(24,8))
        self.add_arc('front-curve',(24,8),(34,18),radius_x=10)
        self.add_polyline('front',(34,18),(34,32),(18,32))
        self.add_polyline('rear',(18,32),(6,32),(6,12))
        self.add_arc('rear-curve',(6,12),(8,8),radius_x=4)
        self.add_contour('shell','roof','front-curve','front-1','front-2','rear-1','rear-2','rear-curve',closed=True)
        self.contours=[c for c in self.contours if c.contour_id not in ('front','rear')]
        self.add_line('window',(13,20),(24,20))
        self.add_line('tow-bar',(34,32),(42,32))
        self.add_arc('wheel-right',(18,32),(18,40),radius_x=4)
        self.add_arc('wheel-left',(18,40),(18,32),radius_x=4)
        self.add_contour('wheel','wheel-right','wheel-left',closed=True)
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
