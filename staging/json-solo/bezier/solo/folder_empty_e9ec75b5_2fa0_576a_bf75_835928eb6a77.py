"""Folder empty (folders), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e9ec75b5-2fa0-576a-bf75-835928eb6a77'
SOURCE_PATH = 'icons-json/folders/folder empty_e9ec75b5-2fa0-576a-bf75-835928eb6a77.json'
AUTHOR = 'json_to_solo'

class FolderEmptyE9ec75b5(Solo48):
    icon_id = 'folder-empty-e9ec75b5'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'empty', 'folders')

    def build(self):
        self.add_line('e0', (19, 8), (7, 8))
        self.add_line('e1', (4, 11), (4, 37))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (44, 37), (44, 16))
        self.add_line('e4', (41, 13), (23, 13))
        self.add_bezier('e5', (7, 8), ((6.945, 8), (6.618, 8), (6.564, 8.008)), ((5.018, 8.008), (4.009, 9.516), (4.009, 10.804)), ((4.009, 10.888), (4, 10.981), (4, 11.065)), ((4, 11.166), (4, 10.899), (4, 11)))
        self.add_bezier('e6', (4, 37), ((4, 37.135), (4, 37.743), (4.009, 37.878)), ((4.009, 38.989), (4.9, 39.992), (6.118, 39.992)), ((6.182, 39.992), (6.255, 40), (6.318, 40)), ((6.455, 40), (6.864, 40), (7, 40)))
        self.add_bezier('e7', (41, 40), ((41.073, 40), (41.409, 40), (41.482, 40)), ((42.509, 40), (43.982, 39.107), (43.982, 38.055)), ((43.991, 37.987), (43.991, 37.928), (44, 37.861)), ((44, 37.735), (44, 37.126), (44, 37)))
        self.add_bezier('e8', (44, 16), ((44, 15.933), (44, 15.444), (44, 15.377)), ((44, 14.383), (43.164, 13.255), (42.1, 13.027)), ((41.8, 12.968), (41.291, 13), (41, 13)))
        self.add_bezier('e9', (23, 13), ((21.682, 11.577), (20.764, 9.095), (19.245, 8.168)), ((19.036, 8.042), (19.227, 8.076), (19, 8)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2', 'e7', 'e3', 'e8', 'e4', 'e9', closed=True)
