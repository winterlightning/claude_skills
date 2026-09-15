"""Volume control low (audio), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ed9ee46d-750c-4be7-ac8a-877c0320999d'
SOURCE_PATH = 'icons-json/audio/volume control low_ed9ee46d-750c-4be7-ac8a-877c0320999d.json'
AUTHOR = 'gpt-6'

class VolumeControlLow(Solo48):
    icon_id = 'volume-control-low'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('volume', 'control', 'low', 'audio')

    def build(self):
        self.add_line('sym-e0', (19, 32), (19, 16))
        self.add_line('sym-e1', (19, 16), (12, 16))
        self.add_line('sym-e2', (12, 16), (8, 17))
        self.add_line('sym-e3', (8, 17), (8, 31))
        self.add_line('sym-e7', (8, 31), (12, 32))
        self.add_line('sym-e8', (12, 32), (19, 32))
        self.add_arc('sym-e9', (19, 32), (25, 37), radius_x=69, radius_y=69, large_arc=False, sweep=False)
        self.add_line('sym-e10', (25, 37), (31, 41))
        self.add_arc('sym-e11', (31, 41), (36, 44), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('sym-e12', (36, 44), (37, 44))
        self.add_arc('sym-e14', (37, 44), (40, 41), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e16', (40, 41), (40, 7))
        self.add_arc('sym-e19', (40, 7), (37, 4), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('sym-e21', (37, 4), (36, 4))
        self.add_arc('sym-e22', (36, 4), (31, 7), radius_x=10, radius_y=10, large_arc=False, sweep=False)
        self.add_line('sym-e23', (31, 7), (25, 11))
        self.add_arc('sym-e24', (25, 11), (19, 16), radius_x=69, radius_y=69, large_arc=False, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e16', 'sym-e19', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', closed=False)
