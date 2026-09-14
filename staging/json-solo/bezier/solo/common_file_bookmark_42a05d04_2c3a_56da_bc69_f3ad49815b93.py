"""Common file bookmark (files), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42a05d04-2c3a-56da-bc69-f3ad49815b93'
SOURCE_PATH = 'icons-json/files/common file bookmark_42a05d04-2c3a-56da-bc69-f3ad49815b93.json'
AUTHOR = 'json_to_solo'

class CommonFileBookmarkFiles(Solo48):
    icon_id = 'common-file-bookmark-files'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('common', 'file', 'bookmark', 'files')

    def build(self):
        self.add_line('e0', (40, 20), (35, 17))
        self.add_line('e1', (35, 17), (31, 20))
        self.add_line('e2', (31, 20), (31, 4))
        self.add_line('e3', (40, 9), (40, 40))
        self.add_line('e4', (37, 44), (12, 44))
        self.add_line('e5', (8, 39), (8, 8))
        self.add_line('e6', (11, 4), (37, 4))
        self.add_bezier('e7', (40, 40), ((40, 40.082), (39.992, 40.527), (39.992, 40.609)), ((39.992, 42.309), (38.541, 44), (37, 44)))
        self.add_bezier('e8', (12, 44), ((11.596, 44), (11.411, 43.982), (11.006, 43.982)), ((9.811, 43.982), (8.017, 42.273), (8.017, 40.955)), ((8.017, 40.591), (8, 40.236), (8, 39.882)), ((8, 39.736), (8, 39.145), (8, 39)))
        self.add_bezier('e9', (8, 8), ((8, 7.918), (8, 7.464), (8, 7.382)), ((8, 5.545), (9.349, 4), (11, 4)))
        self.add_bezier('e10', (37, 4), ((37.101, 4), (36.825, 4.009), (36.926, 4.009)), ((38.543, 4.009), (39.992, 5.209), (39.992, 7.027)), ((39.992, 7.336), (40, 7.636), (40, 7.945)), ((40, 8.145), (40, 8.8), (40, 9)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
