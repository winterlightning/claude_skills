"""Volume control (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2722b0f-fff4-493b-8f5d-619316ae89e6'
SOURCE_PATH = 'icons-json/audio/volume control_f2722b0f-fff4-493b-8f5d-619316ae89e6.json'
AUTHOR = 'json_to_solo'

class VolumeControlAudio(Solo48):
    icon_id = 'volume-control-audio'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'audio')

    def build(self):
        self.add_line('e0', (15, 31), (8, 31))
        self.add_line('e1', (4, 28), (4, 20))
        self.add_line('e2', (7, 17), (15, 17))
        self.add_line('e3', (15, 31), (15, 17))
        self.add_line('e4', (15, 31), (29, 40))
        self.add_line('e5', (32, 38), (32, 10))
        self.add_line('e6', (29, 9), (15, 17))
        self.add_line('e7-1', (8, 31), (5, 30))
        self.add_line('e7-2', (5, 30), (4, 28))
        self.add_arc('e8', (4, 20), (7, 17), radius_x=3)
        self.add_line('e9-1', (29, 40), (31, 40))
        self.add_arc('e9-2', (31, 40), (32, 38), radius_x=2, sweep=False)
        self.add_arc('e10-1', (32, 10), (30, 8), radius_x=2, sweep=False)
        self.add_line('e10-2', (30, 8), (29, 9))
        self.add_arc('e11-1', (39, 16), (44, 24), radius_x=11)
        self.add_arc('e11-2', (44, 24), (39, 32), radius_x=14)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1', 'e8', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4', 'e9-1', 'e9-2', 'e5', 'e10-1', 'e10-2', 'e6')
        self.add_contour('c3', 'e11-1', 'e11-2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
