"""Controls pause (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99180e7b-910b-4846-bb7f-7207185069f4'
SOURCE_PATH = 'icons-json/video/controls pause_99180e7b-910b-4846-bb7f-7207185069f4.json'
AUTHOR = 'json_to_solo'

class ControlsPause99180e7b(Solo48):
    icon_id = 'controls-pause-99180e7b'
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
