"""2p (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fae72b07-c1a6-4e50-8a37-203afbd51530'
SOURCE_PATH = 'icons-json/other/2P (text)_fae72b07-c1a6-4e50-8a37-203afbd51530.json'
AUTHOR = 'json_to_solo'

class Icon2pText(Solo48):
    icon_id = 'icon-2p-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('2p', 'text', 'other')

    def build(self):
        self.add_line('e0', (16, 24), (4, 40))
        self.add_line('e1', (4, 40), (19, 40))
        self.add_line('e2', (29, 25), (38, 25))
        self.add_line('e3', (38, 8), (29, 8))
        self.add_line('e4', (29, 8), (29, 40))
        self.add_bezier('e5', (5, 14), ((6.373, 11.46), (8.436, 8.01), (11.464, 8.01)), ((11.536, 8), (11.609, 8), (11.691, 8)), ((11.764, 8), (11.836, 8), (11.918, 8)), ((12.855, 8), (13.818, 8.43), (14.627, 8.93)), ((19.164, 11.7), (18.9, 20.08), (16, 24)))
        self.add_bezier('e6', (38, 25), ((38.355, 25), (38.509, 24.77), (38.864, 24.67)), ((42.073, 23.75), (43.991, 20.5), (43.991, 16.93)), ((43.991, 16.851), (44, 16.763), (44, 16.684)), ((44, 16.683), (44, 16.681), (44, 16.68)), ((44, 16.6), (43.991, 16.52), (43.991, 16.44)), ((43.991, 12.94), (42.491, 9.46), (39.282, 8.37)), ((38.745, 8.18), (38.564, 8), (38, 8)))
        self.add_contour('c0', 'e5', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e4')
