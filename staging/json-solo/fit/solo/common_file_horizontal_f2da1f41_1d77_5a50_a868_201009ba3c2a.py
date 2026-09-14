"""Common file horizontal (files), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2da1f41-1d77-5a50-a868-201009ba3c2a'
SOURCE_PATH = 'icons-json/files/common file horizontal_f2da1f41-1d77-5a50-a868-201009ba3c2a.json'
AUTHOR = 'json_to_solo'

class CommonFileHorizontalFiles(Solo48):
    icon_id = 'common-file-horizontal-files'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('common', 'file', 'horizontal', 'files')

    def build(self):
        self.add_line('e0', (4, 38), (4, 11))
        self.add_line('e1', (6, 8), (35, 8))
        self.add_line('e2', (44, 18), (44, 37))
        self.add_line('e3', (42, 40), (7, 40))
        self.add_arc('e4-1', (7, 40), (5, 40), radius_x=4, sweep=False)
        self.add_arc('e4-2', (5, 40), (4, 38), radius_x=4)
        self.add_line('e5-1', (4, 11), (5, 8))
        self.add_arc('e5-2', (5, 8), (6, 8), radius_x=1, sweep=False)
        self.add_arc('e6', (35, 8), (44, 18), radius_x=19)
        self.add_arc('e7', (44, 37), (42, 40), radius_x=4)
        self.add_contour('c0', 'e4-1', 'e4-2', 'e0', 'e5-1', 'e5-2', 'e1', 'e6', 'e2', 'e7', 'e3', closed=True)
