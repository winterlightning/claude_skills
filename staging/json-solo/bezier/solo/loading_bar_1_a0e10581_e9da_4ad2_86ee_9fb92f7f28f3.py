"""Loading bar 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0e10581-e9da-4ad2-86ee-9fb92f7f28f3'
SOURCE_PATH = 'icons-json/interface-essential/loading bar 1_a0e10581-e9da-4ad2-86ee-9fb92f7f28f3.json'
AUTHOR = 'json_to_solo'

class LoadingBar1InterfaceEssential(Solo48):
    icon_id = 'loading-bar-1-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'bar', 'interface-essential')

    def build(self):
        self.add_line('e0', (23, 8), (9, 40))
        self.add_line('e1', (39, 8), (25, 40))
        self.add_line('e2', (38, 40), (11, 40))
        self.add_line('e3', (10, 8), (37, 8))
        self.add_bezier('e4', (11, 40), ((10.391, 40), (10.064, 40), (9.455, 40)), ((6.755, 40), (4, 33.211), (4, 26.4)), ((4, 26.391), (4, 26.382), (4, 26.373)), ((4, 25.81), (4.009, 25.225), (4.009, 24.663)), ((4.009, 17.531), (6.1, 11.726), (8.636, 9.189)), ((9.182, 8.663), (9.409, 8), (10, 8)))
        self.add_bezier('e5', (37, 8), ((37.609, 8), (37.936, 8), (38.545, 8)), ((41.009, 8), (43.991, 16.023), (43.991, 22.08)), ((43.991, 22.423), (44, 22.766), (44, 23.086)), ((44, 23.089), (44, 23.091), (44, 23.094)), ((44, 23.274), (44, 23.431), (43.991, 23.589)), ((43.991, 30.789), (40.918, 40), (38, 40)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e4', 'e3', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
