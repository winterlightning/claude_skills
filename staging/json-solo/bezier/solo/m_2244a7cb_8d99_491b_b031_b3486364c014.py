"""M (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2244a7cb-8d99-491b-b031-b3486364c014'
SOURCE_PATH = 'icons-json/typeface/m_2244a7cb-8d99-491b-b031-b3486364c014.json'
AUTHOR = 'json_to_solo'

class M2244a7cb(Solo48):
    icon_id = 'm-2244a7cb'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('m', 'typeface')

    def build(self):
        self.add_line('e0', (4, 9), (4, 40))
        self.add_line('e1', (24, 18), (24, 40))
        self.add_line('e2', (44, 18), (44, 40))
        self.add_bezier('e3', (4, 16), ((4, 15.99), (4.009, 15.97), (4.009, 15.96)), ((4.009, 15.27), (4.782, 13.87), (5.1, 13.3)), ((6.809, 10.2), (9.945, 8.02), (13.3, 8.02)), ((13.536, 8.02), (13.764, 8), (14, 8)), ((14.003, 8), (14.007, 8), (14.01, 8)), ((14.216, 8), (14.421, 8.01), (14.627, 8.01)), ((19.027, 8.01), (23.164, 11.12), (24, 16)), ((24.109, 16.66), (24, 17.33), (24, 18)))
        self.add_bezier('e4', (24, 16), ((25.382, 11.58), (28.827, 8.02), (33.3, 8.02)), ((33.536, 8.02), (33.764, 8), (34, 8)), ((34.209, 8), (34.418, 8.01), (34.627, 8.01)), ((39.418, 8.01), (43.982, 11.91), (43.982, 17.46)), ((43.982, 17.64), (44, 17.82), (44, 18)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e3', 'e1')
        self.add_contour('c2', 'e4', 'e2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c1')
