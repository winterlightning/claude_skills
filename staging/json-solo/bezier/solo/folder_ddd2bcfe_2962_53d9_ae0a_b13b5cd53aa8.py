"""Folder (folders), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ddd2bcfe-2962-53d9-ae0a-b13b5cd53aa8'
SOURCE_PATH = 'icons-json/folders/folder_ddd2bcfe-2962-53d9-ae0a-b13b5cd53aa8.json'
AUTHOR = 'json_to_solo'

class Folder(Solo48):
    icon_id = 'folder'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'folders')

    def build(self):
        self.add_line('e0', (4, 37), (4, 12))
        self.add_line('e1', (8, 8), (16, 8))
        self.add_line('e2', (25, 14), (41, 14))
        self.add_line('e3', (44, 16), (44, 36))
        self.add_line('e4', (41, 40), (8, 40))
        self.add_bezier('e5', (4, 12), ((4, 11.8), (4.009, 11.59), (4.009, 11.39)), ((4.009, 9.42), (5.191, 8.02), (7.009, 8.02)), ((7.218, 8.02), (7.791, 8), (8, 8)))
        self.add_bezier('e6', (16, 8), ((16.191, 8), (16.191, 8.02), (16.382, 8.02)), ((18.782, 8.02), (19.736, 10.72), (21.155, 12.37)), ((22.218, 13.6), (23.482, 14), (25, 14)))
        self.add_bezier('e7', (41, 14), ((42.764, 14), (43.382, 14.21), (44, 16)))
        self.add_bezier('e8', (44, 36), ((44, 36.11), (44, 36.22), (44, 36.33)), ((44, 38.07), (42.782, 40), (41, 40)))
        self.add_bezier('e9', (8, 40), ((7.909, 39.99), (7.464, 39.99), (7.373, 39.98)), ((6.527, 39.98), (5.364, 39.57), (4.709, 39.02)), ((4.291, 38.66), (4, 37.57), (4, 37)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
