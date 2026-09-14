"""Line (diagrams), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa89b836-c375-48b3-bb41-fcec99fa6e14'
SOURCE_PATH = 'icons-json/diagrams/line_fa89b836-c375-48b3-bb41-fcec99fa6e14.json'
AUTHOR = 'json_to_solo'

class LineFa89b836(Solo48):
    icon_id = 'line-fa89b836'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'diagrams'
    aliases = ()
    keywords = ('line', 'diagrams')

    def build(self):
        self.add_line('e0', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
