"""Archway (_uncategorized_04), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '726d709a-1fc5-42e8-b357-8d83c0bb1293'
SOURCE_PATH = 'icons-json/_uncategorized_04/archway_726d709a-1fc5-42e8-b357-8d83c0bb1293.json'
AUTHOR = 'json_to_solo'

class ArchwayUncategorized04(Solo48):
    icon_id = 'archway-uncategorized-04'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_04'
    aliases = ()
    keywords = ('archway', '_uncategorized_04')

    def build(self):
        self.add_line('e0', (13, 42), (7, 42))
        self.add_line('e1', (6, 41), (6, 22))
        self.add_line('e2', (42, 22), (42, 41))
        self.add_line('e3', (41, 42), (35, 42))
        self.add_line('e4', (34, 41), (34, 23))
        self.add_line('e5', (14, 23), (14, 41))
        self.add_bezier('e6', (7, 42), ((6.885, 41.975), (6.597, 41.943), (6.483, 41.918)), ((6.115, 41.755), (6.172, 41.254), (6, 41)))
        self.add_bezier('e7', (6, 22), ((6, 20.585), (6.507, 19.312), (7.006, 17.986)), ((9.494, 11.326), (15.794, 6.008), (23.141, 6.008)), ((23.262, 6.008), (23.383, 6), (23.503, 6)), ((23.505, 6), (23.507, 6), (23.509, 6)), ((23.82, 6), (24.123, 6.008), (24.434, 6.008)), ((31.724, 6.008), (38.408, 11.056), (40.92, 17.782)), ((41.435, 19.173), (42, 20.503), (42, 22)))
        self.add_bezier('e8', (42, 41), ((41.967, 41.123), (41.935, 41.427), (41.902, 41.55)), ((41.771, 41.885), (41.254, 41.836), (41, 42)))
        self.add_bezier('e9', (35, 42), ((34.91, 42), (35.266, 42), (35.176, 42)), ((34.587, 42), (34.401, 41.335), (34, 41)))
        self.add_bezier('e10', (34, 23), ((34, 22.165), (33.237, 20.605), (32.918, 19.803)), ((29.727, 11.752), (18.387, 11.727), (15.065, 19.778)), ((14.648, 20.776), (14, 21.912), (14, 23)))
        self.add_bezier('e11', (14, 41), ((13.689, 41.286), (13.552, 42), (13.045, 42)), ((12.881, 42), (12.836, 42), (13, 42)))
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', closed=True)
