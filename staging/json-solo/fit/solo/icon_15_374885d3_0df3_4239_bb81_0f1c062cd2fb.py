"""15 (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '374885d3-0df3-4239-bb81-0f1c062cd2fb'
SOURCE_PATH = 'icons-json/other/15_374885d3-0df3-4239-bb81-0f1c062cd2fb.json'
AUTHOR = 'json_to_solo'

class Icon15Other(Solo48):
    icon_id = 'icon-15-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('other',)

    def build(self):
        self.add_line('e0', (12, 8), (12, 40))
        self.add_line('e1', (42, 8), (29, 8))
        self.add_line('e2', (29, 8), (27, 22))
        self.add_arc('e3', (4, 14), (12, 8), radius_x=20, sweep=False)
        self.add_arc('e4-1', (27, 22), (44, 29), radius_x=10)
        self.add_line('e4-2', (44, 29), (42, 36))
        self.add_arc('e4-3', (42, 36), (34, 40), radius_x=10)
        self.add_arc('e4-4', (34, 40), (26, 35), radius_x=9)
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4-1', 'e4-2', 'e4-3', 'e4-4')
