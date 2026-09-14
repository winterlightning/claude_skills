"""Navigation left (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b695362f-8f85-5627-b657-8b5759cfc345'
SOURCE_PATH = 'icons-json/interface-essential/navigation left_b695362f-8f85-5627-b657-8b5759cfc345.json'
AUTHOR = 'json_to_solo'

class NavigationLeft(Solo48):
    icon_id = 'navigation-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'left', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 8), (4, 20))
        self.add_line('e1', (5, 23), (14, 34))
        self.add_bezier('e2', (4, 20), ((4, 20.283), (4.009, 20.886), (4.009, 21.169)), ((4.009, 21.994), (4.591, 22.545), (5, 23)))
        self.add_bezier('e3', (13, 22), ((17.473, 21.2), (22.109, 20.025), (26.627, 19.938)), ((34.391, 19.791), (40.409, 20.714), (43.055, 32.234)), ((43.4, 33.748), (43.573, 35.298), (43.764, 36.849)), ((43.827, 37.342), (44, 37.871), (44, 38.375)), ((44, 38.917), (44, 39.458), (44, 40)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3')
