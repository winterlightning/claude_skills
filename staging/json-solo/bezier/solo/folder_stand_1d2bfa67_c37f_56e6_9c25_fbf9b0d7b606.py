"""Folder stand (folders), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d2bfa67-c37f-56e6-9c25-fbf9b0d7b606'
SOURCE_PATH = 'icons-json/folders/folder stand_1d2bfa67-c37f-56e6-9c25-fbf9b0d7b606.json'
AUTHOR = 'json_to_solo'

class FolderStand1d2bfa67(Solo48):
    icon_id = 'folder-stand-1d2bfa67'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'stand', 'folders')

    def build(self):
        self.add_line('e0', (24, 42), (24, 33))
        self.add_line('e1', (15, 42), (33, 42))
        self.add_line('e2', (6, 31), (6, 8))
        self.add_line('e3', (9, 6), (17, 6))
        self.add_line('e4', (22, 12), (40, 12))
        self.add_line('e5', (42, 13), (42, 31))
        self.add_line('e6', (39, 33), (8, 33))
        self.add_bezier('e7', (8, 33), ((6.585, 33), (6.54, 32.309), (6, 31)))
        self.add_bezier('e8', (6, 8), ((6, 7.935), (6, 8.324), (6, 8.258)), ((6, 6.99), (7.514, 6.008), (8.659, 6.008)), ((8.733, 6.008), (8.798, 6), (8.864, 6)), ((9.003, 6), (8.861, 6), (9, 6)))
        self.add_bezier('e9', (17, 6), ((17.155, 6), (16.947, 6.008), (17.103, 6.008)), ((19.255, 6.008), (19.901, 8.446), (20.686, 10.017)), ((20.85, 10.345), (21.014, 10.819), (21.292, 11.081)), ((21.603, 11.384), (21.624, 11.804), (22, 12)))
        self.add_bezier('e10', (40, 12), ((41.047, 12), (42, 11.666), (42, 13)))
        self.add_bezier('e11', (42, 31), ((42, 31.123), (42, 30.791), (41.992, 30.914)), ((41.992, 32.133), (40.765, 32.984), (39.66, 33.074)), ((39.333, 33.098), (39.311, 33), (39, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e7', 'e2', 'e8', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
