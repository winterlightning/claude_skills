"""Envelope sealed (emails), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '112eab3f-fcce-46df-828b-9f90813d86e3'
SOURCE_PATH = 'icons-json/emails/envelope sealed_112eab3f-fcce-46df-828b-9f90813d86e3.json'
AUTHOR = 'gpt-6'

class EnvelopeSealed(Solo48):
    icon_id = 'envelope-sealed'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('envelope', 'sealed', 'emails')

    def build(self):
        self.add_line('sym-e0', (40, 4), (8, 4))
        self.add_line('sym-e3', (8, 4), (8, 44))
        self.add_arc('sym-e4', (8, 44), (10, 44), radius_x=22, radius_y=22, large_arc=False, sweep=True)
        self.add_line('sym-e5', (10, 44), (39, 44))
        self.add_arc('sym-e6-2', (39, 44), (40, 44), radius_x=39, radius_y=39, large_arc=False, sweep=True)
        self.add_line('sym-e7', (40, 44), (40, 4))
        self.add_line('sym-e8', (40, 4), (32, 12))
        self.add_line('sym-e10', (32, 12), (24, 12))
        self.add_line('sym-e11', (24, 12), (24, 36))
        self.add_line('sym-e12', (24, 36), (32, 36))
        self.add_line('sym-e13', (32, 36), (33, 38))
        self.add_line('sym-e14', (33, 38), (40, 44))
        self.add_line('sym-e15', (8, 4), (16, 12))
        self.add_line('sym-e17', (16, 12), (24, 12))
        self.add_line('sym-e18', (24, 36), (16, 36))
        self.add_line('sym-e19', (16, 36), (15, 38))
        self.add_line('sym-e20', (15, 38), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6-2', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', closed=False)
        self.add_contour('sym-c1', 'sym-e15', 'sym-e17', closed=False)
        self.add_contour('sym-c2', 'sym-e18', 'sym-e19', 'sym-e20', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
