"""Power outlet type m (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68088998-e38f-468c-abce-f0acea61ead3'
SOURCE_PATH = 'icons-json/electronics/power outlet type m_68088998-e38f-468c-abce-f0acea61ead3.json'
AUTHOR = 'json_to_solo'

class PowerOutletTypeMElectronics(Solo48):
    icon_id = 'power-outlet-type-m-electronics'
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
        self.add_bezier('sym-e8', (11, 42), ((10.975, 41.992), (11.025, 42), (11, 42)))
        self.add_bezier('sym-e9', (11, 42), ((8.93, 42), (6, 39.111), (6, 37)))
        self.add_bezier('sym-e10', (6, 37), ((6, 36.918), (6, 37.082), (6, 37)))
        self.add_line('sym-e11', (6, 37), (6, 11))
        self.add_bezier('sym-e12', (6, 11), ((6, 9.053), (9.012, 6), (11, 6)))
        self.add_bezier('sym-e13', (11, 6), ((11.041, 6), (10.959, 6), (11, 6)))
        self.add_line('sym-e14', (11, 6), (24, 6))
        self.add_line('sym-e15', (24, 6), (37, 6))
        self.add_bezier('sym-e16', (37, 6), ((37.041, 6), (36.959, 6), (37, 6)))
        self.add_bezier('sym-e17', (37, 6), ((38.988, 6), (42, 9.053), (42, 11)))
        self.add_line('sym-e18', (42, 11), (42, 37))
        self.add_bezier('sym-e19', (42, 37), ((42, 37.082), (42, 36.918), (42, 37)))
        self.add_bezier('sym-e20', (42, 37), ((42, 39.111), (39.07, 42), (37, 42)))
        self.add_bezier('sym-e21', (37, 42), ((36.975, 42), (37.025, 41.992), (37, 42)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', closed=True)
        self.add_contour('sym-c3', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', closed=True)
