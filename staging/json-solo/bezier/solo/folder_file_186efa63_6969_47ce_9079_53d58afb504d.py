"""Folder file (folders), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '186efa63-6969-47ce-9079-53d58afb504d'
SOURCE_PATH = 'icons-json/folders/folder file_186efa63-6969-47ce-9079-53d58afb504d.json'
AUTHOR = 'json_to_solo'

class FolderFileFolders(Solo48):
    icon_id = 'folder-file-folders'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'folders'
    aliases = ()
    keywords = ('folder', 'file', 'folders')

    def build(self):
        self.add_line('e0', (13, 22), (11, 22))
        self.add_line('e1', (8, 24), (8, 42))
        self.add_line('e2', (10, 44), (31, 44))
        self.add_line('e3', (32, 41), (32, 28))
        self.add_line('e4', (31, 26), (21, 26))
        self.add_line('e5', (15, 22), (13, 22))
        self.add_line('e6', (13, 22), (13, 6))
        self.add_line('e7', (15, 4), (38, 4))
        self.add_line('e8', (40, 6), (40, 39))
        self.add_line('e9', (38, 41), (32, 41))
        self.add_bezier('e10', (11, 22), ((10.057, 21.964), (8.017, 22), (8.017, 23.491)), ((8.017, 23.664), (8, 23.827), (8, 24)))
        self.add_bezier('e11', (8, 42), ((8, 42.055), (8.008, 42.291), (8.008, 42.336)), ((8.008, 43.355), (9.107, 44), (10, 44)))
        self.add_bezier('e12', (31, 44), ((32.322, 44), (32, 42.127), (32, 41)))
        self.add_bezier('e13', (32, 28), ((31.714, 27.091), (32.069, 26), (31, 26)))
        self.add_bezier('e14', (21, 26), ((18.019, 26), (17.869, 23.155), (15.731, 22.291)), ((15.427, 22.164), (15.32, 22.027), (15, 22)))
        self.add_bezier('e15', (13, 6), ((13, 5.164), (13.709, 4.009), (14.552, 4.009)), ((14.611, 4.009), (14.941, 4), (15, 4)))
        self.add_bezier('e16', (38, 4), ((38.059, 4), (38.442, 4.009), (38.501, 4.009)), ((39.217, 4.009), (39.992, 4.855), (39.992, 5.618)), ((39.992, 5.691), (40, 5.936), (40, 6)))
        self.add_bezier('e17', (40, 39), ((40, 39.064), (39.992, 39.582), (39.992, 39.655)), ((39.992, 40.564), (38.783, 41), (38, 41)))
        self.add_contour('c0', 'e0', 'e10', 'e1', 'e11', 'e2', 'e12', 'e3', 'e13', 'e4', 'e14', 'e5', 'e6', 'e15', 'e7', 'e16', 'e8', 'e17', 'e9')
