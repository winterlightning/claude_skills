"""Less than (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d5125ac-33a7-436c-b327-3e7fc0960a33'
SOURCE_PATH = 'icons-json/_uncategorized_25/less than_9d5125ac-33a7-436c-b327-3e7fc0960a33.json'
AUTHOR = 'json_to_solo'

class LessThan(Solo48):
    icon_id = 'less-than'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('less', 'than', '_uncategorized')

    def build(self):
        self.add_line('e0', (40, 4), (8, 24))
        self.add_line('e1', (8, 24), (40, 44))
        self.add_contour('c0', 'e0', 'e1')
