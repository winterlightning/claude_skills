"""Controls record (video), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cef3098e-17c6-5755-bef4-bbc2034d88e2'
SOURCE_PATH = 'icons-json/video/controls record_cef3098e-17c6-5755-bef4-bbc2034d88e2.json'
AUTHOR = 'json_to_solo'

class ControlsRecordVideo(Solo48):
    icon_id = 'controls-record-video'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    aliases = ()
    keywords = ('controls', 'record', 'video')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
