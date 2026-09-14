"""Folder empty (folders), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7d8b7227-dc25-5b0c-b0c7-40e77eaa84e6'
SOURCE_PATH = 'icons-json/folders/folder empty_7d8b7227-dc25-5b0c-b0c7-40e77eaa84e6.json'
AUTHOR = 'json_to_solo'

class FolderEmpty7d8b7227(Solo48):
    icon_id = 'folder-empty-7d8b7227'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'empty', 'folders')

    def build(self):
        self.add_line('e0', (18, 8), (7, 8))
        self.add_line('e1', (4, 10), (4, 37))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 38), (44, 16))
        self.add_line('e4', (42, 13), (23, 13))
        self.add_bezier('e5', (7, 8), ((6.818, 8), (6.364, 8), (6.182, 8)), ((5.418, 8), (4.6, 8.472), (4.2, 9.061)), ((4.064, 9.263), (4.091, 9.781), (4, 10)))
        self.add_bezier('e6', (4, 37), ((4, 37.084), (4, 37.634), (4, 37.718)), ((4, 39.116), (5.573, 40), (7, 40)))
        self.add_bezier('e7', (41, 40), ((41.1, 40), (41.464, 39.992), (41.564, 39.992)), ((42.455, 39.992), (43.473, 39.587), (43.864, 38.787)), ((43.936, 38.636), (43.927, 38.152), (44, 38)))
        self.add_bezier('e8', (44, 16), ((44, 15.907), (44, 15.402), (44, 15.309)), ((44, 13.996), (43.191, 13.488), (42, 13)))
        self.add_bezier('e9', (23, 13), ((20.255, 13), (20.555, 8.008), (17.882, 8.008)), ((17.8, 8.008), (18.082, 8), (18, 8)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
