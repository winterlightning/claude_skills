"""Lock (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '386cb547-821f-4d23-a0b8-bb7f43205473'
SOURCE_PATH = 'icons-json/interface-essential/lock_386cb547-821f-4d23-a0b8-bb7f43205473.json'
AUTHOR = 'json_to_solo'

class Lock386cb547(Solo48):
    icon_id = 'lock-386cb547'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('lock', 'interface-essential')

    def build(self):
        self.add_line('e0', (35, 19), (35, 15))
        self.add_line('e1', (14, 14), (14, 19))
        self.add_line('e2', (24, 34), (24, 29))
        self.add_line('e3', (37, 19), (11, 19))
        self.add_line('e4', (8, 25), (8, 40))
        self.add_line('e5', (11, 44), (36, 44))
        self.add_line('e6', (40, 42), (40, 22))
        self.add_bezier('e7', (35, 15), ((35, 9.255), (29.912, 4.018), (24.581, 4.018)), ((24.371, 4.018), (24.168, 4), (23.958, 4)), ((23.956, 4), (23.954, 4), (23.952, 4)), ((23.819, 4), (23.678, 4.009), (23.545, 4.009)), ((19.166, 4.009), (15.276, 7.291), (14.223, 11.845)), ((14.072, 12.518), (14, 13.309), (14, 14)))
        self.add_bezier('e8', (40, 22), ((39.983, 21.927), (39.966, 22.036), (39.949, 21.964)), ((39.907, 21.891), (39.865, 21.809), (39.832, 21.736)), ((39.116, 20.736), (38.229, 19), (37, 19)))
        self.add_bezier('e9', (11, 19), ((9.131, 20.191), (8, 21.882), (8, 24.245)), ((8, 24.464), (8, 24.782), (8, 25)))
        self.add_bezier('e10', (8, 40), ((8, 41.745), (9.392, 44), (11, 44)))
        self.add_bezier('e11', (36, 44), ((36.472, 44), (36.733, 43.982), (37.204, 43.982)), ((38.055, 43.982), (39.149, 43.282), (39.747, 42.673)), ((39.891, 42.527), (39.865, 42.164), (40, 42)))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
