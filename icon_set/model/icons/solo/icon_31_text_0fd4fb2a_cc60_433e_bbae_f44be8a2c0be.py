"""31 (text) (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fd4fb2a-cc60-433e-bbae-f44be8a2c0be'
SOURCE_PATH = 'icons-json/symbol/31 (text)_0fd4fb2a-cc60-433e-bbae-f44be8a2c0be.json'
AUTHOR = 'json_to_solo'

class Icon31Text(Solo48):
    icon_id = 'icon-31-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('text', 'symbol')

    def build(self):
        self.add_line('e0', (44, 8), (44, 40))
        self.add_bezier('e1', (5, 13), ((6.173, 10.002), (9.355, 8.008), (12.836, 8.008)), ((13.009, 8.008), (13.182, 8), (13.355, 8)), ((13.527, 8), (13.691, 8.017), (13.864, 8.017)), ((19.764, 8.017), (23, 14.299), (21.073, 19.04)), ((20.173, 21.246), (18.036, 22.653), (15.673, 23.335)), ((14.918, 23.562), (14.136, 23.714), (13.345, 23.806)), ((13.109, 23.832), (12.864, 23.848), (12.618, 23.865)), ((12.536, 23.865), (12.455, 23.874), (12.373, 23.874)), ((12.327, 23.874), (12.273, 23.874), (12.227, 23.874)), ((15.545, 23.621), (20.445, 25.886), (21.655, 28.834)), ((22.482, 30.855), (22.309, 33.575), (21.255, 35.495)), ((19.891, 37.962), (16.682, 39.983), (13.645, 39.983)), ((13.455, 39.983), (13.273, 40), (13.082, 40)), ((12.955, 40), (12.827, 39.992), (12.709, 39.992)), ((9.909, 39.992), (4.009, 37.364), (4.009, 34.307)), ((4.009, 34.24), (4, 34.067), (4, 34)))
        self.add_bezier('e2', (36, 14), ((37.682, 13.259), (39.209, 12.371), (40.636, 11.251)), ((41.864, 10.282), (42.918, 9.103), (44, 8)))
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2', 'e0')
