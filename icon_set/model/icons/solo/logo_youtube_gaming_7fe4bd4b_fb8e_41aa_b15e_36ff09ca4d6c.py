"""Logo youtube gaming (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fe4bd4b-fb8e-41aa-b15e-36ff09ca4d6c'
SOURCE_PATH = 'icons-json/video-games/logo youtube gaming_7fe4bd4b-fb8e-41aa-b15e-36ff09ca4d6c.json'
AUTHOR = 'json_to_solo'

class LogoYoutubeGaming(Solo48):
    icon_id = 'logo-youtube-gaming'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('logo', 'youtube', 'gaming', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (6, 27))
        self.add_arc('sym-e2', (6, 27), (4, 23), radius_x=7)
        self.add_line('sym-e3', (4, 23), (4, 16))
        self.add_arc('sym-e5', (4, 16), (13, 8), radius_x=10)
        self.add_line('sym-e6', (13, 8), (14, 8))
        self.add_line('sym-e8', (14, 8), (18, 9))
        self.add_line('sym-e9', (18, 9), (23, 13))
        self.add_arc('sym-e10', (23, 13), (24, 13), radius_x=2, sweep=False)
        self.add_arc('sym-e11', (24, 13), (25, 13), radius_x=2, sweep=False)
        self.add_line('sym-e12', (25, 13), (30, 9))
        self.add_line('sym-e13', (30, 9), (34, 8))
        self.add_arc('sym-e15', (34, 8), (35, 8), radius_x=78, sweep=False)
        self.add_arc('sym-e16', (35, 8), (44, 16), radius_x=10)
        self.add_line('sym-e18', (44, 16), (44, 23))
        self.add_arc('sym-e19', (44, 23), (42, 27), radius_x=6)
        self.add_line('sym-e20', (42, 27), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', closed=True)
