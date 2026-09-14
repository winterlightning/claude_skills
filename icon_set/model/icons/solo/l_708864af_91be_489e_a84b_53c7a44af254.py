"""L (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '708864af-91be-489e-a84b-53c7a44af254'
SOURCE_PATH = 'icons-json/typeface/l_708864af-91be-489e-a84b-53c7a44af254.json'
AUTHOR = 'json_to_solo'

class LTypeface(Solo48):
    icon_id = 'l-typeface'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('l', 'typeface')

    def build(self):
        self.add_line('e0', (8, 4), (8, 36))
        self.add_bezier('e1', (8, 36), ((8, 36.255), (8.018, 36.327), (8.018, 36.591)), ((8.018, 39.855), (10.08, 42.273), (16.338, 43.418)), ((17.813, 43.691), (19.467, 43.982), (21.049, 43.982)), ((21.404, 43.982), (21.742, 44), (22.098, 44)), ((22.101, 44), (22.103, 44), (22.106, 44)), ((22.281, 44), (22.456, 44), (22.631, 43.991)), ((27.236, 43.991), (31.982, 43), (36.196, 42.118)), ((37.351, 41.873), (38.524, 41.627), (39.662, 41.355)), ((39.68, 41.345), (39.982, 41.291), (39.982, 41.273)), ((39.982, 41.273), (40, 41), (40, 41)))
        self.add_contour('c0', 'e0', 'e1')
