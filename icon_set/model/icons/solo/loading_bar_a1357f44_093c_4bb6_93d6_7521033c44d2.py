"""Loading bar (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1357f44-093c-4bb6-93d6-7521033c44d2'
SOURCE_PATH = 'icons-json/interface-essential/loading bar_a1357f44-093c-4bb6-93d6-7521033c44d2.json'
AUTHOR = 'json_to_solo'

class LoadingBar(Solo48):
    icon_id = 'loading-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'bar', 'interface-essential')

    def build(self):
        self.add_line('e0', (26, 40), (30, 8))
        self.add_line('e1', (14, 40), (19, 8))
        self.add_line('e2', (12, 8), (39, 8))
        self.add_line('e3', (38, 40), (10, 40))
        self.add_bezier('e4', (10, 40), ((9.864, 40), (10.082, 40), (9.945, 39.982)), ((7.209, 39.982), (4.809, 35.733), (4.191, 30.667)), ((4, 28.729), (4.018, 26.471), (4.018, 24.516)), ((4.018, 22.933), (4, 21.351), (4, 19.787)), ((4, 19.783), (4, 19.78), (4, 19.777)), ((4, 19.567), (4, 19.357), (4, 19.147)), ((4, 13.973), (6.082, 9.813), (8.509, 8.391)), ((9.182, 8), (10.009, 8.036), (10.709, 8.036)), ((11.2, 8.036), (11.509, 8), (12, 8)))
        self.add_bezier('e5', (39, 8), ((39.091, 8), (38.727, 8.018), (38.818, 8.018)), ((42.118, 8.018), (43.982, 13.76), (43.982, 19.627)), ((43.982, 21.493), (44, 23.378), (44, 25.244)), ((44, 25.258), (44, 25.272), (44, 25.286)), ((44, 26.161), (43.991, 27.018), (43.991, 27.876)), ((43.991, 33.529), (41.682, 39.982), (38.536, 39.982)), ((38.382, 39.982), (38.236, 40), (38.082, 40)), ((37.936, 40), (38.145, 40), (38, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e4', 'e2', 'e5', 'e3', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
