"""Logo youtube gaming (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fe4bd4b-fb8e-41aa-b15e-36ff09ca4d6c'
SOURCE_PATH = 'icons-json/video-games/logo youtube gaming_7fe4bd4b-fb8e-41aa-b15e-36ff09ca4d6c.json'
AUTHOR = 'json_to_solo'

class LogoYoutubeGamingVideoGames(Solo48):
    icon_id = 'logo-youtube-gaming-video-games'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('logo', 'youtube', 'gaming', 'video-games')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (6, 27))
        self.add_bezier('sym-e2', (6, 27), ((4.982, 26.293), (4, 24.171), (4, 23)))
        self.add_line('sym-e3', (4, 23), (4, 16))
        self.add_bezier('sym-e4', (4, 16), ((4, 15.933), (4, 16.067), (4, 16)))
        self.add_bezier('sym-e5', (4, 16), ((4, 11.907), (8.673, 8), (13, 8)))
        self.add_bezier('sym-e6', (13, 8), ((13.227, 8), (13.782, 8), (14, 8)))
        self.add_bezier('sym-e7', (14, 8), ((14.182, 8), (13.827, 8), (14, 8)))
        self.add_bezier('sym-e8', (14, 8), ((15.082, 8), (17.136, 8.335), (18, 9)))
        self.add_line('sym-e9', (18, 9), (23, 13))
        self.add_bezier('sym-e10', (23, 13), ((23.264, 13.059), (23.668, 13.044), (24, 13)))
        self.add_bezier('sym-e11', (24, 13), ((24.332, 13.044), (24.736, 13.059), (25, 13)))
        self.add_line('sym-e12', (25, 13), (30, 9))
        self.add_bezier('sym-e13', (30, 9), ((30.864, 8.335), (32.918, 8), (34, 8)))
        self.add_bezier('sym-e14', (34, 8), ((34.173, 8), (33.818, 8), (34, 8)))
        self.add_bezier('sym-e15', (34, 8), ((34.218, 8), (34.773, 8), (35, 8)))
        self.add_bezier('sym-e16', (35, 8), ((39.327, 8), (44, 11.907), (44, 16)))
        self.add_bezier('sym-e17', (44, 16), ((44, 16.067), (44, 15.933), (44, 16)))
        self.add_line('sym-e18', (44, 16), (44, 23))
        self.add_bezier('sym-e19', (44, 23), ((44, 24.171), (43.018, 26.293), (42, 27)))
        self.add_line('sym-e20', (42, 27), (24, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', closed=True)
