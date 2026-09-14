"""Tunnel diode (electronics), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '33846799-7c6c-4b49-8562-6e95155d2049'
SOURCE_PATH = 'icons-json/electronics/tunnel diode_33846799-7c6c-4b49-8562-6e95155d2049.json'
AUTHOR = 'json_to_solo'

class TunnelDiodeElectronics(Solo48):
    icon_id = 'tunnel-diode-electronics'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'electronics'
    aliases = ()
    keywords = ('tunnel', 'diode', 'electronics')

    def build(self):
        self.add_line('e0', (35, 8), (35, 24))
        self.add_line('e1', (4, 24), (11, 24))
        self.add_line('e2', (35, 40), (35, 24))
        self.add_line('e3', (44, 24), (35, 24))
        self.add_line('e4', (34, 24), (13, 9))
        self.add_line('e5', (11, 10), (11, 39))
        self.add_line('e6', (13, 40), (34, 24))
        self.add_bezier('e7', (13, 9), ((12.5, 8.975), (12.036, 8.935), (11.582, 9.477)), ((11.364, 9.748), (11.155, 9.729), (11, 10)))
        self.add_bezier('e8', (11, 39), ((11.355, 39.394), (11.8, 40), (12.391, 40)), ((12.618, 40), (12.764, 40), (13, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e7', 'e5', 'e8', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c4')
