"""Al (text u) (text), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2306778-41d5-4836-93a4-7175608aabed'
SOURCE_PATH = 'icons-json/text/al (text u)_c2306778-41d5-4836-93a4-7175608aabed.json'
AUTHOR = 'json_to_solo'

class AlTextUText(Solo48):
    icon_id = 'al-text-u-text'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'text'
    aliases = ()
    keywords = ('al', 'text', 'u')

    def build(self):
        self.add_line('e0', (22, 27), (16, 6))
        self.add_line('e1', (14, 5), (8, 27))
        self.add_line('e2', (11, 19), (20, 19))
        self.add_line('e3', (32, 4), (32, 21))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5-1', (16, 6), (15, 4), radius_x=2, sweep=False)
        self.add_arc('e5-2', (15, 4), (14, 5), radius_x=1, sweep=False)
        self.add_arc('e6', (32, 21), (40, 25), radius_x=5, sweep=False)
        self.add_contour('c0', 'e0', 'e5-1', 'e5-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e6')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
