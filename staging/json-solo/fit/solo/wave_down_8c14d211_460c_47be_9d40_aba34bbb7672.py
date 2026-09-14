"""Wave down (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c14d211-460c-47be-9d40-aba34bbb7672'
SOURCE_PATH = 'icons-json/arrows/wave down_8c14d211-460c-47be-9d40-aba34bbb7672.json'
AUTHOR = 'json_to_solo'

class WaveDownArrows(Solo48):
    icon_id = 'wave-down-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'down', 'arrows')

    def build(self):
        self.add_line('e0', (4, 40), (4, 12))
        self.add_line('e1', (17, 12), (17, 36))
        self.add_line('e2', (27, 36), (27, 13))
        self.add_line('e3', (39, 13), (39, 27))
        self.add_line('e4', (35, 23), (39, 27))
        self.add_line('e5', (44, 23), (39, 27))
        self.add_arc('e6-1', (4, 12), (7, 9), radius_x=4)
        self.add_arc('e6-2', (7, 9), (11, 8), radius_x=15)
        self.add_line('e6-3', (11, 8), (12, 8))
        self.add_arc('e6-4', (12, 8), (17, 12), radius_x=6)
        self.add_arc('e7-1', (17, 36), (22, 40), radius_x=6, sweep=False)
        self.add_arc('e7-2', (22, 40), (27, 36), radius_x=6, sweep=False)
        self.add_arc('e8-1', (27, 13), (33, 8), radius_x=7)
        self.add_arc('e8-2', (33, 8), (39, 13), radius_x=7)
        self.add_contour('c0', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1', 'e7-1', 'e7-2', 'e2', 'e8-1', 'e8-2', 'e3')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
