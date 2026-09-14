"""Volume control full 1 (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '329a09b2-92a3-4377-afbb-67608ff5d0ba'
SOURCE_PATH = 'icons-json/audio/volume control full 1_329a09b2-92a3-4377-afbb-67608ff5d0ba.json'
AUTHOR = 'json_to_solo'

class VolumeControlFull1(Solo48):
    icon_id = 'volume-control-full-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'full', 'audio')

    def build(self):
        self.add_line('e0', (26, 40), (16, 31))
        self.add_line('e1', (15, 30), (6, 30))
        self.add_line('e2', (4, 29), (4, 19))
        self.add_line('e3', (6, 17), (15, 17))
        self.add_line('e4', (16, 17), (26, 8))
        self.add_line('e5', (29, 10), (29, 38))
        self.add_arc('e6-1', (39, 14), (44, 24), radius_x=15)
        self.add_arc('e6-2', (44, 24), (39, 34), radius_x=13)
        self.add_arc('e7', (35, 18), (36, 30), radius_x=9)
        self.add_arc('e8', (16, 31), (15, 30), radius_x=22, sweep=False)
        self.add_arc('e9', (6, 30), (4, 29), radius_x=2)
        self.add_arc('e10', (4, 19), (6, 17), radius_x=2)
        self.add_arc('e11', (15, 17), (16, 17), radius_x=2, sweep=False)
        self.add_line('e12-1', (26, 8), (28, 8))
        self.add_line('e12-2', (28, 8), (29, 10))
        self.add_line('e13-1', (29, 38), (27, 40))
        self.add_line('e13-2', (27, 40), (26, 40))
        self.add_contour('c0', 'e6-1', 'e6-2')
        self.add_contour('c1', 'e7')
        self.add_contour('c2', 'e0', 'e8', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11', 'e4', 'e12-1', 'e12-2', 'e5', 'e13-1', 'e13-2', closed=True)
