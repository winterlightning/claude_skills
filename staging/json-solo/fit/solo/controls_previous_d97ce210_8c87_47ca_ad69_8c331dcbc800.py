"""Controls previous (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd97ce210-8c87-47ca-ad69-8c331dcbc800'
SOURCE_PATH = 'icons-json/video/controls previous_d97ce210-8c87-47ca-ad69-8c331dcbc800.json'
AUTHOR = 'json_to_solo'

class ControlsPreviousD97ce210(Solo48):
    icon_id = 'controls-previous-d97ce210'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'previous', 'video')

    def build(self):
        self.add_line('e0', (8, 4), (8, 44))
        self.add_line('e1', (40, 5), (40, 43))
        self.add_line('e2', (40, 43), (17, 26))
        self.add_line('e3', (17, 26), (16, 24))
        self.add_line('e4', (16, 24), (40, 5))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4', closed=True)
