"""Pacman (video-games), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea992b74-1d7b-5d1a-9380-854e5151b7ed'
SOURCE_PATH = 'icons-json/video-games/pacman_ea992b74-1d7b-5d1a-9380-854e5151b7ed.json'
AUTHOR = 'json_to_solo'

class Pacman(Solo48):
    icon_id = 'pacman'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('pacman', 'video-games')

    def build(self):
        self.add_line('e0', (40, 35), (27, 24))
        self.add_line('e1', (27, 24), (40, 14))
        self.add_arc('e2-1', (40, 14), (26, 4), radius_x=18, sweep=False)
        self.add_line('e2-2', (26, 4), (24, 4))
        self.add_arc('e2-3', (24, 4), (16, 7), radius_x=15, sweep=False)
        self.add_arc('e2-4', (16, 7), (9, 17), radius_x=21, sweep=False)
        self.add_line('e2-5', (9, 17), (8, 24))
        self.add_arc('e2-6', (8, 24), (11, 35), radius_x=22, sweep=False)
        self.add_arc('e2-7', (11, 35), (20, 43), radius_x=18, sweep=False)
        self.add_arc('e2-8', (20, 43), (25, 44), radius_x=13, sweep=False)
        self.add_arc('e2-9', (25, 44), (40, 35), radius_x=18, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9', 'e0', 'e1', closed=True)
