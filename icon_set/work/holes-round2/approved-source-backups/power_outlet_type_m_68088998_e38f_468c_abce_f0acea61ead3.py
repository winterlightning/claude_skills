"""Power outlet type m (electronics), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68088998-e38f-468c-abce-f0acea61ead3'
SOURCE_PATH = 'icons-json/electronics/power outlet type m_68088998-e38f-468c-abce-f0acea61ead3.json'
AUTHOR = 'json_to_solo'

class PowerOutletTypeM(Solo48):
    icon_id = 'power-outlet-type-m'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'm', 'electronics')

    def build(self):
        self.add_arc('sym-e0', (22, 18), (26, 18), radius_x=2)
        self.add_arc('sym-e1', (26, 18), (22, 18), radius_x=2)
        self.add_arc('sym-e2', (30, 30), (33, 30), radius_x=2)
        self.add_arc('sym-e3', (33, 30), (30, 30), radius_x=2)
        self.add_arc('sym-e4', (18, 30), (15, 30), radius_x=2, sweep=False)
        self.add_arc('sym-e5', (15, 30), (18, 30), radius_x=2, sweep=False)
        self.add_line('sym-e6', (37, 42), (24, 42))
        self.add_line('sym-e7', (24, 42), (11, 42))
        self.add_arc('sym-e9', (11, 42), (6, 37), radius_x=5)
        self.add_line('sym-e11', (6, 37), (6, 11))
        self.add_arc('sym-e12', (6, 11), (11, 6), radius_x=6)
        self.add_line('sym-e14', (11, 6), (24, 6))
        self.add_line('sym-e15', (24, 6), (37, 6))
        self.add_arc('sym-e17', (37, 6), (42, 11), radius_x=6)
        self.add_line('sym-e18', (42, 11), (42, 37))
        self.add_arc('sym-e20', (42, 37), (37, 42), radius_x=5)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e20', closed=True)
