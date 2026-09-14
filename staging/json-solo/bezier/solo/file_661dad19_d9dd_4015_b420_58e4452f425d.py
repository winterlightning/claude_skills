"""File (files), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '661dad19-d9dd-4015-b420-58e4452f425d'
SOURCE_PATH = 'icons-json/files/file_661dad19-d9dd-4015-b420-58e4452f425d.json'
AUTHOR = 'json_to_solo'

class File661dad19(Solo48):
    icon_id = 'file-661dad19'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('file', 'files')

    def build(self):
        self.add_line('e0', (10, 4), (32, 4))
        self.add_line('e1', (32, 4), (39, 12))
        self.add_line('e2', (40, 13), (40, 42))
        self.add_line('e3', (38, 44), (10, 44))
        self.add_line('e4', (8, 42), (8, 5))
        self.add_bezier('e5', (39, 12), ((39.387, 12.418), (39.621, 12.318), (39.907, 12.773)), ((39.941, 12.882), (39.966, 12.891), (40, 13)))
        self.add_bezier('e6', (40, 42), ((39.537, 43.345), (39.213, 43.464), (38, 44)))
        self.add_bezier('e7', (10, 44), ((9.865, 43.927), (9.381, 43.955), (9.246, 43.891)), ((8.842, 43.691), (8.269, 43.082), (8.101, 42.636)), ((8.042, 42.5), (8.067, 42.136), (8, 42)))
        self.add_bezier('e8', (8, 5), ((8.051, 4.882), (8.093, 4.673), (8.143, 4.545)), ((8.328, 4.218), (9.171, 4.009), (9.516, 4.009)), ((9.575, 4), (9.941, 4), (10, 4)))
        self.add_contour('c0', 'e0', 'e1', 'e5', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', closed=True)
