"""motorhome: reconstructed on SOLO48 from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8555c3cc-efd6-5bfe-ab94-1368fb7045b6'
SOURCE_PATH = 'pictographic-primitives/transportation/truck rv_8555c3cc-efd6-5bfe-ab94-1368fb7045b6.svg'
AUTHOR = 'gpt-6'


class Motorhome(Solo48):
    icon_id = 'motorhome'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('rv', 'motorhome', 'camper', 'camper van', 'travel', 'camping', 'vehicle', 'road trip')

    def build(self) -> None:

        # Rear living section flows into the over-cab roof; wheels share radius and baseline.
        self.add_line('rear',(6,38),(6,10))
        self.add_arc('roof-rear',(6,10),(10,6),radius_x=4)
        self.add_line('roof',(10,6),(34,6))
        self.add_arc('overhang-top',(34,6),(38,10),radius_x=4)
        self.add_arc('overhang-bottom',(38,10),(34,14),radius_x=4)
        self.add_line('overhang-lip',(34,14),(30,14))
        self.add_polyline('cab',(34,14),(42,26),(42,38),(38,38))
        self.add_polyline('cab-window',(30,14),(30,26),(42,26))
        self.add_polyline('window',(14,15),(22,15),(22,23),(14,23),closed=True)
        self.add_line('floor-rear',(6,38),(8,38))
        self.add_line('floor-middle',(16,38),(30,38))
        for side,cx in [('rear',12),('front',34)]:
            self.add_arc(side+'-top',(cx-4,38),(cx+4,38),radius_x=4)
            self.add_arc(side+'-bottom',(cx+4,38),(cx-4,38),radius_x=4)
            self.add_contour(side+'-wheel',side+'-top',side+'-bottom',closed=True)
        # Record only actual shared-endpoint contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if a.start in (b.start,b.end) or a.end in (b.start,b.end):
                    self.relate('connect',a.element_id,b.element_id)
