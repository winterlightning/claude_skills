"""Folder (folders), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ea310bb-7e10-465d-8803-e8bcc89546bc'
SOURCE_PATH = 'icons-json/folders/folder_9ea310bb-7e10-465d-8803-e8bcc89546bc.json'
AUTHOR = 'json_to_solo'

class Folder9ea310bb(Solo48):
    icon_id = 'folder-9ea310bb'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'folders')

    def build(self):
        self.add_line('e0', (41, 40), (7, 40))
        self.add_line('e1', (4, 36), (4, 11))
        self.add_line('e2', (8, 8), (17, 8))
        self.add_line('e3', (24, 13), (40, 13))
        self.add_line('e4', (44, 16), (44, 38))
        self.add_bezier('e5', (7, 40), ((6.855, 39.99), (6.436, 39.99), (6.3, 39.98)), ((5.109, 39.98), (4.009, 38.37), (4.009, 37.16)), ((4.009, 36.93), (4, 36.69), (4, 36.45)), ((4, 36.3), (4, 36.15), (4, 36)))
        self.add_bezier('e6', (4, 11), ((4.009, 10.84), (4.009, 10.68), (4.018, 10.53)), ((4.018, 8.95), (5.809, 8.01), (7, 8.01)), ((7.073, 8.01), (7.145, 8), (7.218, 8)), ((7.355, 8), (7.864, 8), (8, 8)))
        self.add_bezier('e7', (17, 8), ((17.064, 8), (16.855, 8), (16.918, 8)), ((20.145, 8), (20.827, 13), (24, 13)))
        self.add_bezier('e8', (40, 13), ((41.209, 13), (42.773, 12.87), (43.673, 13.99)), ((43.764, 14.1), (43.982, 14.36), (43.982, 14.52)), ((43.991, 14.59), (43.991, 14.65), (44, 14.72)), ((44, 14.79), (44, 14.85), (44, 14.92)), ((43.991, 15.06), (43.991, 15.2), (43.982, 15.34)), ((43.991, 15.41), (43.991, 15.49), (44, 15.56)), ((44, 15.71), (44, 15.85), (44, 16)))
        self.add_bezier('e9', (44, 38), ((43.282, 38.91), (42.209, 40), (41, 40)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
