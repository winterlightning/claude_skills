"""Wave (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3459233-4acf-5488-8964-ea188d1b0ae9'
SOURCE_PATH = 'icons-json/wayfinding/wave_e3459233-4acf-5488-8964-ea188d1b0ae9.json'
AUTHOR = 'json_to_solo'

class WaveE3459233(Solo48):
    icon_id = 'wave-e3459233'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('wave', 'wayfinding')

    def build(self):
        self.add_line('e0', (21, 11), (26, 16))
        self.add_arc('e1-1', (4, 16), (14, 8), radius_x=17)
        self.add_arc('e1-2', (14, 8), (21, 11), radius_x=12)
        self.add_arc('e2-1', (26, 16), (34, 19), radius_x=10, sweep=False)
        self.add_arc('e2-2', (34, 19), (44, 10), radius_x=17, sweep=False)
        self.add_arc('e3-1', (4, 37), (18, 30), radius_x=12)
        self.add_arc('e3-2', (18, 30), (26, 37), radius_x=27)
        self.add_arc('e3-3', (26, 37), (32, 40), radius_x=9, sweep=False)
        self.add_line('e3-4', (32, 40), (33, 40))
        self.add_arc('e3-5', (33, 40), (44, 30), radius_x=14, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e0', 'e2-1', 'e2-2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5')
