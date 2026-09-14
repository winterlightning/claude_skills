"""App window small (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '24d6bd4c-8a53-420d-b8a5-e8c7793b7868'
SOURCE_PATH = 'icons-json/_uncategorized_03/app window small_24d6bd4c-8a53-420d-b8a5-e8c7793b7868.json'
AUTHOR = 'json_to_solo'

class AppWindowSmallUncategorized03(Solo48):
    icon_id = 'app-window-small-uncategorized-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('app', 'window', 'small', '_uncategorized_03')

    def build(self):
        self.add_line('sym-e0', (4, 18), (44, 18))
        self.add_line('sym-e1', (44, 18), (44, 36))
        self.add_arc('sym-e2', (44, 36), (40, 40), radius_x=5)
        self.add_line('sym-e3', (40, 40), (24, 40))
        self.add_line('sym-e4', (24, 40), (8, 40))
        self.add_arc('sym-e5', (8, 40), (4, 36), radius_x=5)
        self.add_line('sym-e6', (4, 36), (4, 18))
        self.add_line('sym-e7', (4, 18), (4, 12))
        self.add_arc('sym-e8', (4, 12), (8, 8), radius_x=5)
        self.add_line('sym-e9', (8, 8), (24, 8))
        self.add_line('sym-e10', (24, 8), (40, 8))
        self.add_arc('sym-e11', (40, 8), (44, 12), radius_x=5)
        self.add_line('sym-e12', (44, 12), (44, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
