"""Controls rewind (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2736daad-03fd-5c48-9a0d-f54eed191916'
SOURCE_PATH = 'icons-json/video/controls rewind_2736daad-03fd-5c48-9a0d-f54eed191916.json'
AUTHOR = 'json_to_solo'

class ControlsRewind2736daad(Solo48):
    icon_id = 'controls-rewind-2736daad'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'rewind', 'video')

    def build(self):
        self.add_line('e0', (39, 4), (8, 23))
        self.add_line('e1', (9, 25), (40, 44))
        self.add_line('e2', (40, 44), (40, 35))
        self.add_line('e3', (40, 35), (40, 7))
        self.add_line('e4', (40, 7), (39, 4))
        self.add_line('e5', (8, 23), (9, 25))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e2', 'e3', 'e4', closed=True)
