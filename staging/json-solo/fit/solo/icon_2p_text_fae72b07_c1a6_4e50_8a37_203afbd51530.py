"""2p (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fae72b07-c1a6-4e50-8a37-203afbd51530'
SOURCE_PATH = 'icons-json/other/2P (text)_fae72b07-c1a6-4e50-8a37-203afbd51530.json'
AUTHOR = 'json_to_solo'

class Icon2pTextOther(Solo48):
    icon_id = 'icon-2p-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('2p', 'text', 'other')

    def build(self):
        self.add_line('e0', (16, 24), (4, 40))
        self.add_line('e1', (4, 40), (19, 40))
        self.add_line('e2', (29, 25), (38, 25))
        self.add_line('e3', (38, 8), (29, 8))
        self.add_line('e4', (29, 8), (29, 40))
        self.add_arc('e5-1', (5, 14), (12, 8), radius_x=8)
        self.add_arc('e5-2', (12, 8), (16, 24), radius_x=10)
        self.add_arc('e6-1', (38, 25), (43, 21), radius_x=7, sweep=False)
        self.add_line('e6-2', (43, 21), (44, 17))
        self.add_line('e6-3', (44, 17), (43, 12))
        self.add_arc('e6-4', (43, 12), (38, 8), radius_x=6, sweep=False)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e3', 'e4')
