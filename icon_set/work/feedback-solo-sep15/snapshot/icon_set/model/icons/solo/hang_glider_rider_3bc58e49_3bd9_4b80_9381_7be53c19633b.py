"""A hang glider with a prone rider and curved trailing line. HRECT_L extremes (4,8)-(44,40). No useful exact Lucide glider match; use a geometric triangular wing and round head. Preserve flight direction, hanging support and trailing curve while widening the head clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3bc58e49-3bd9-4b80-9381-7be53c19633b'
SOURCE_PATH = 'pictographic-primitives/symbol/paragliding_3bc58e49-3bd9-4b80-9381-7be53c19633b.svg'
AUTHOR = 'gpt-6'


class HangGliderRider(Solo48):
    icon_id = 'hang-glider-rider'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('hang-glider', 'paragliding', 'gliding', 'flying', 'sport', 'adventure', 'sky', 'extreme')

    def build(self) -> None:
        self.add_polyline('wing',(4,8),(44,8),(30,15),(16,22),(4,8),closed=True)
        self.add_polyline('support',(30,15),(28,30),(32,40))
        self.relate('connect','wing','support')
        self.add_arc('trail',(4,36),(20,34),radius_x=24,radius_y=8,sweep=False)
        self.add_line('body',(20,34),(28,30))
        self.add_contour('rider','trail','body')
        self.relate('connect','rider','support')
        cx, cy, radius = 41, 25, 3
        self.add_arc('head-top', (cx-radius, cy), (cx+radius, cy), radius_x=radius)
        self.add_arc('head-bottom', (cx+radius, cy), (cx-radius, cy), radius_x=radius)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
