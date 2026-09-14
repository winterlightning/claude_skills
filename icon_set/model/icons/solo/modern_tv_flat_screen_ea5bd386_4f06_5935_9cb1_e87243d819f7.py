"""Modern tv flat screen (tv), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea5bd386-4f06-5935-9cb1-e87243d819f7'
SOURCE_PATH = 'icons-json/tv/modern tv flat screen_ea5bd386-4f06-5935-9cb1-e87243d819f7.json'
AUTHOR = 'json_to_solo'

class ModernTvFlatScreen(Solo48):
    icon_id = 'modern-tv-flat-screen'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tv'
    aliases = ()
    keywords = ('modern', 'tv', 'flat', 'screen')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 34))
        self.add_line('sym-e1', (24, 34), (5, 34))
        self.add_line('sym-e2', (5, 34), (4, 33))
        self.add_line('sym-e3', (4, 33), (4, 32))
        self.add_line('sym-e4', (4, 32), (4, 9))
        self.add_arc('sym-e5', (4, 9), (5, 8), radius_x=1)
        self.add_line('sym-e6', (5, 8), (6, 8))
        self.add_line('sym-e7', (6, 8), (24, 8))
        self.add_line('sym-e8', (24, 8), (42, 8))
        self.add_line('sym-e9', (42, 8), (43, 8))
        self.add_arc('sym-e10', (43, 8), (44, 9), radius_x=1)
        self.add_line('sym-e11', (44, 9), (44, 32))
        self.add_arc('sym-e12', (44, 32), (44, 33), radius_x=34, sweep=False)
        self.add_line('sym-e13', (44, 33), (43, 34))
        self.add_line('sym-e14', (43, 34), (24, 34))
        self.add_line('sym-e15', (16, 40), (24, 40))
        self.add_line('sym-e16', (24, 40), (32, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.add_contour('sym-c1', 'sym-e15', 'sym-e16')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
