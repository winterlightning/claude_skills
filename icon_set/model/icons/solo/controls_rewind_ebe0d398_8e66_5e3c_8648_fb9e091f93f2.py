"""Controls rewind (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ebe0d398-8e66-5e3c-8648-fb9e091f93f2'
SOURCE_PATH = 'icons-json/video/controls rewind_ebe0d398-8e66-5e3c-8648-fb9e091f93f2.json'
AUTHOR = 'json_to_solo'

class ControlsRewindVideo(Solo48):
    icon_id = 'controls-rewind-video'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'rewind', 'video')

    def build(self):
        self.add_line('e0', (39, 4), (33, 8))
        self.add_line('e1', (33, 8), (9, 22))
        self.add_line('e2', (10, 27), (33, 40))
        self.add_line('e3', (40, 41), (40, 6))
        self.add_line('e4', (40, 6), (39, 4))
        self.add_line('e5-1', (9, 22), (8, 24))
        self.add_line('e5-2', (8, 24), (10, 27))
        self.add_arc('e6-1', (33, 40), (39, 44), radius_x=22, sweep=False)
        self.add_arc('e6-2', (39, 44), (40, 41), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e3', 'e4', closed=True)
