"""Envelope sealed (emails), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '112eab3f-fcce-46df-828b-9f90813d86e3'
SOURCE_PATH = 'icons-json/emails/envelope sealed_112eab3f-fcce-46df-828b-9f90813d86e3.json'
AUTHOR = 'json_to_solo'

class EnvelopeSealedEmails(Solo48):
    icon_id = 'envelope-sealed-emails'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'emails'
    aliases = ()
    keywords = ('envelope', 'sealed', 'emails')

    def build(self):
        self.add_bezier('sym-e0', (40, 4), ((39.436, 4), (38.564, 4), (38, 4)))
        self.add_line('sym-e1', (38, 4), (10, 4))
        self.add_bezier('sym-e2', (10, 4), ((9.436, 4), (8.564, 4), (8, 4)))
        self.add_line('sym-e3', (8, 4), (8, 44))
        self.add_bezier('sym-e4', (8, 44), ((8.564, 44), (9.436, 44), (10, 44)))
        self.add_line('sym-e5', (10, 44), (38, 44))
        self.add_bezier('sym-e6', (38, 44), ((38.564, 44), (39.436, 44), (40, 44)))
        self.add_line('sym-e7', (40, 44), (40, 4))
        self.add_line('sym-e8', (40, 4), (33, 11))
        self.add_bezier('sym-e9', (33, 11), ((32.646, 11.382), (32.514, 12), (32, 12)))
        self.add_line('sym-e10', (32, 12), (24, 12))
        self.add_line('sym-e11', (24, 12), (24, 36))
        self.add_line('sym-e12', (24, 36), (32, 36))
        self.add_bezier('sym-e13', (32, 36), ((32.438, 36), (32.697, 37.709), (33, 38)))
        self.add_line('sym-e14', (33, 38), (40, 44))
        self.add_line('sym-e15', (8, 4), (15, 11))
        self.add_bezier('sym-e16', (15, 11), ((15.354, 11.382), (15.486, 12), (16, 12)))
        self.add_line('sym-e17', (16, 12), (24, 12))
        self.add_line('sym-e18', (24, 36), (16, 36))
        self.add_bezier('sym-e19', (16, 36), ((15.562, 36), (15.303, 37.709), (15, 38)))
        self.add_line('sym-e20', (15, 38), (8, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c2', 'sym-e18', 'sym-e19', 'sym-e20')
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
