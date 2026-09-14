"""Controls pause (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '62e7b3dc-b846-5f70-8a55-d1419584bb3f'
SOURCE_PATH = 'icons-json/video/controls pause_62e7b3dc-b846-5f70-8a55-d1419584bb3f.json'
AUTHOR = 'json_to_solo'

class ControlsPause(Solo48):
    icon_id = 'controls-pause'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'pause', 'video')

    def build(self):
        self.add_line('e0', (40, 4), (40, 44))
        self.add_line('e1', (8, 4), (8, 44))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
