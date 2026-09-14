"""Pacman (video-games), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea992b74-1d7b-5d1a-9380-854e5151b7ed'
SOURCE_PATH = 'icons-json/video-games/pacman_ea992b74-1d7b-5d1a-9380-854e5151b7ed.json'
AUTHOR = 'json_to_solo'

class PacmanVideoGames(Solo48):
    icon_id = 'pacman-video-games'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pacman', 'video-games')

    def build(self):
        self.add_line('e0', (40, 35), (27, 24))
        self.add_line('e1', (27, 24), (40, 14))
        self.add_bezier('e2', (40, 14), ((39.688, 13.482), (40, 14.055), (39.848, 13.555)), ((39.629, 13.127), (39.217, 12.736), (38.956, 12.327)), ((36.598, 8.691), (33.802, 6.118), (29.836, 4.773)), ((28.556, 4.345), (27.107, 4), (25.76, 4)), ((25.759, 4), (25.758, 4), (25.757, 4)), ((25.691, 4), (25.633, 4), (25.566, 4)), ((25.305, 4), (25.053, 4.018), (24.792, 4.018)), ((15.234, 4.018), (8.017, 13.555), (8.017, 23.464)), ((8.017, 23.764), (8, 24.064), (8, 24.373)), ((8, 24.378), (8, 24.382), (8, 24.387)), ((8, 24.691), (8.008, 24.996), (8.008, 25.3)), ((8.008, 26.245), (8.227, 27.245), (8.379, 28.173)), ((9.533, 34.845), (13.811, 40.536), (19.731, 42.9)), ((21.255, 43.509), (22.947, 43.982), (24.581, 43.982)), ((24.682, 43.991), (24.775, 43.991), (24.867, 44)), ((24.87, 44), (24.872, 44), (24.875, 44)), ((25.033, 44), (25.198, 43.991), (25.356, 43.991)), ((31.537, 43.991), (36.345, 39.982), (40, 35)))
        self.add_contour('c0', 'e2', 'e0', 'e1', closed=True)
