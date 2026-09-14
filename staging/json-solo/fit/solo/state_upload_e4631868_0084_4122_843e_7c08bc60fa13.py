"""State upload (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4631868-0084-4122-843e-7c08bc60fa13'
SOURCE_PATH = 'icons-json/state/state upload_e4631868-0084-4122-843e-7c08bc60fa13.json'
AUTHOR = 'json_to_solo'

class StateUploadState(Solo48):
    icon_id = 'state-upload-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('state', 'upload')

    def build(self):
        self.add_line('e0', (17, 21), (24, 15))
        self.add_line('e1', (24, 33), (24, 15))
        self.add_line('e2', (31, 22), (24, 15))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
