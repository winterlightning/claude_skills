"""Disability oc (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '381f9f82-7e66-5183-9655-c64492f3bacc'
SOURCE_PATH = 'icons-json/wayfinding/disability oc_381f9f82-7e66-5183-9655-c64492f3bacc.json'
AUTHOR = 'json_to_solo'

class DisabilityOc(Solo48):
    icon_id = 'disability-oc'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('disability', 'oc', 'wayfinding')

    def build(self):
        self.add_line('e0', (30, 16), (30, 33))
        self.add_line('e1', (19, 31), (19, 16))
        self.add_line('e2', (4, 17), (4, 31))
        self.add_arc('e3-1', (44, 13), (38, 8), radius_x=7, sweep=False)
        self.add_arc('e3-2', (38, 8), (30, 16), radius_x=8, sweep=False)
        self.add_arc('e4-1', (30, 33), (37, 40), radius_x=8, sweep=False)
        self.add_arc('e4-2', (37, 40), (44, 35), radius_x=8, sweep=False)
        self.add_arc('e5-1', (4, 31), (7, 38), radius_x=10, sweep=False)
        self.add_line('e5-2', (7, 38), (12, 40))
        self.add_arc('e5-3', (12, 40), (19, 31), radius_x=8, sweep=False)
        self.add_arc('e6-1', (19, 16), (12, 8), radius_x=8, sweep=False)
        self.add_line('e6-2', (12, 8), (8, 9))
        self.add_arc('e6-3', (8, 9), (6, 11), radius_x=8, sweep=False)
        self.add_arc('e6-4', (6, 11), (4, 17), radius_x=10, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e0', 'e4-1', 'e4-2')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e2', closed=True)
