"""Phone call split (phones), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da651079-1a68-521c-96b2-dd86719598e6'
SOURCE_PATH = 'icons-json/phones/phone call split_da651079-1a68-521c-96b2-dd86719598e6.json'
AUTHOR = 'json_to_solo'

class PhoneCallSplitPhones(Solo48):
    icon_id = 'phone-call-split-phones'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'phones'
    aliases = ()
    keywords = ('phone', 'call', 'split', 'phones')

    def build(self):
        self.add_line('sym-e0', (24, 42), (24, 37))
        self.add_bezier('sym-e1', (24, 37), ((24, 34.308), (22.777, 31.569), (22, 29)))
        self.add_bezier('sym-e2', (22, 29), ((20.184, 22.986), (17.214, 17.688), (13, 13)))
        self.add_bezier('sym-e3', (13, 13), ((12.206, 12.108), (11.916, 10.769), (11, 10)))
        self.add_line('sym-e4', (11, 10), (6, 6))
        self.add_line('sym-e5', (6, 6), (6, 17))
        self.add_line('sym-e6', (24, 35), (24, 31))
        self.add_line('sym-e7', (6, 6), (16, 6))
        self.add_bezier('sym-e8', (24, 37), ((24, 34.308), (25.223, 31.569), (26, 29)))
        self.add_bezier('sym-e9', (26, 29), ((27.816, 22.986), (30.786, 17.688), (35, 13)))
        self.add_bezier('sym-e10', (35, 13), ((35.794, 12.108), (36.084, 10.769), (37, 10)))
        self.add_line('sym-e11', (37, 10), (42, 6))
        self.add_line('sym-e12', (42, 6), (42, 17))
        self.add_line('sym-e13', (42, 6), (32, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6')
        self.add_contour('sym-c2', 'sym-e7')
        self.add_contour('sym-c3', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c4', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c4')
