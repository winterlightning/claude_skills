"""24 (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3ef1255-7230-466e-a0e3-b1897407d9eb'
SOURCE_PATH = 'icons-json/other/24 (text)_e3ef1255-7230-466e-a0e3-b1897407d9eb.json'
AUTHOR = 'json_to_solo'

class Icon24TextOther(Solo48):
    icon_id = 'icon-24-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('e0', (16, 24), (4, 40))
        self.add_line('e1', (4, 40), (19, 40))
        self.add_line('e2', (44, 32), (29, 32))
        self.add_line('e3', (29, 32), (41, 8))
        self.add_line('e4', (41, 8), (41, 40))
        self.add_bezier('e5', (5, 14), ((6.418, 11.406), (8.464, 8.011), (11.218, 8.011)), ((11.373, 8.011), (11.527, 8), (11.682, 8)), ((11.764, 8), (11.845, 8.011), (11.927, 8.011)), ((12.718, 8.011), (13.564, 8.366), (14.282, 8.766)), ((18.873, 11.314), (19.127, 19.76), (16, 24)))
        self.add_contour('c0', 'e5', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3', 'e4')
