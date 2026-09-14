"""Oc (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83b28959-2b38-492c-ac13-4b3442ce26af'
SOURCE_PATH = 'icons-json/symbol/OC (text)_83b28959-2b38-492c-ac13-4b3442ce26af.json'
AUTHOR = 'json_to_solo'

class OcTextSymbol(Solo48):
    icon_id = 'oc-text-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('oc', 'text', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (44, 13), (44, 12), radius_x=1)
        self.add_arc('sym-e1', (44, 12), (38, 8), radius_x=8, sweep=False)
        self.add_line('sym-e3', (38, 8), (37, 8))
        self.add_arc('sym-e4', (37, 8), (30, 16), radius_x=8, sweep=False)
        self.add_line('sym-e5', (30, 16), (30, 24))
        self.add_line('sym-e6', (30, 24), (30, 32))
        self.add_arc('sym-e7', (30, 32), (37, 40), radius_x=8, sweep=False)
        self.add_line('sym-e8', (37, 40), (38, 40))
        self.add_arc('sym-e10', (38, 40), (44, 36), radius_x=8, sweep=False)
        self.add_line('sym-e11', (44, 36), (44, 35))
        self.add_line('sym-e12', (19, 24), (19, 16))
        self.add_arc('sym-e13', (19, 16), (12, 8), radius_x=8, sweep=False)
        self.add_line('sym-e15', (12, 8), (11, 8))
        self.add_arc('sym-e16-1', (11, 8), (6, 11), radius_x=6, sweep=False)
        self.add_arc('sym-e16-2', (6, 11), (4, 17), radius_x=10, sweep=False)
        self.add_line('sym-e19', (4, 17), (4, 24))
        self.add_line('sym-e20', (4, 24), (4, 31))
        self.add_arc('sym-e23-1', (4, 31), (6, 37), radius_x=10, sweep=False)
        self.add_arc('sym-e23-2', (6, 37), (11, 40), radius_x=6, sweep=False)
        self.add_arc('sym-e24', (11, 40), (12, 40), radius_x=1)
        self.add_arc('sym-e26', (12, 40), (19, 32), radius_x=8, sweep=False)
        self.add_line('sym-e27', (19, 32), (19, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16-1', 'sym-e16-2', 'sym-e19', 'sym-e20', 'sym-e23-1', 'sym-e23-2', 'sym-e24', 'sym-e26', 'sym-e27', closed=True)
