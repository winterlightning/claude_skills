"""Volume control medium (audio), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '341717b2-8a95-48bf-83d5-4321e85be4b7'
SOURCE_PATH = 'icons-json/audio/volume control medium_341717b2-8a95-48bf-83d5-4321e85be4b7.json'
AUTHOR = 'json_to_solo'

class VolumeControlMediumAudio(Solo48):
    icon_id = 'volume-control-medium-audio'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'medium', 'audio')

    def build(self):
        self.add_line('sym-e0', (14, 31), (14, 17))
        self.add_line('sym-e1', (14, 17), (7, 17))
        self.add_arc('sym-e2', (7, 17), (4, 20), radius_x=3, sweep=False)
        self.add_line('sym-e4', (4, 20), (4, 24))
        self.add_line('sym-e5', (4, 24), (4, 28))
        self.add_arc('sym-e7', (4, 28), (7, 31), radius_x=3, sweep=False)
        self.add_line('sym-e8', (7, 31), (14, 31))
        self.add_line('sym-e9', (14, 31), (28, 40))
        self.add_arc('sym-e12', (28, 40), (29, 40), radius_x=31)
        self.add_arc('sym-e14', (29, 40), (30, 38), radius_x=2, sweep=False)
        self.add_line('sym-e15', (30, 38), (30, 24))
        self.add_line('sym-e16', (30, 24), (30, 10))
        self.add_arc('sym-e17', (30, 10), (29, 8), radius_x=2, sweep=False)
        self.add_arc('sym-e19', (29, 8), (28, 8), radius_x=55)
        self.add_line('sym-e22', (28, 8), (14, 17))
        self.add_arc('sym-e23', (39, 35), (44, 24), radius_x=15, sweep=False)
        self.add_arc('sym-e26', (44, 24), (39, 13), radius_x=15, sweep=False)
        self.add_arc('sym-e27', (38, 24), (36, 30), radius_x=10)
        self.add_arc('sym-e28', (38, 24), (36, 18), radius_x=10, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e22')
        self.add_contour('sym-c1', 'sym-e23', 'sym-e26')
        self.add_contour('sym-c2', 'sym-e27')
        self.add_contour('sym-c3', 'sym-e28')
        self.relate('connect', 'sym-c2', 'sym-c3')
