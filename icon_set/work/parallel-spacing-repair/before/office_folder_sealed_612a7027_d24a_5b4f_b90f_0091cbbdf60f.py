"""Office folder sealed (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '612a7027-d24a-5b4f-b90f-0091cbbdf60f'
SOURCE_PATH = 'icons-json/office/office folder sealed_612a7027-d24a-5b4f-b90f-0091cbbdf60f.json'
AUTHOR = 'json_to_solo'

class OfficeFolderSealed(Solo48):
    icon_id = 'office-folder-sealed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('office', 'folder', 'sealed')

    def build(self):
        self.add_line('e0', (44, 18), (40, 17))
        self.add_line('e1', (40, 17), (7, 17))
        self.add_line('e2', (7, 17), (4, 18))
        self.add_line('e3', (4, 18), (4, 35))
        self.add_line('e4', (8, 40), (39, 40))
        self.add_line('e5', (44, 37), (44, 15))
        self.add_line('e6', (41, 11), (23, 11))
        self.add_line('e7', (17, 8), (8, 8))
        self.add_line('e8', (4, 11), (4, 19))
        self.add_line('e9-1', (4, 35), (5, 39))
        self.add_line('e9-2', (5, 39), (7, 40))
        self.add_arc('e9-3', (7, 40), (8, 40), radius_x=20)
        self.add_line('e10-1', (39, 40), (41, 40))
        self.add_arc('e10-2', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_line('e11-1', (44, 15), (43, 12))
        self.add_line('e11-2', (43, 12), (41, 11))
        self.add_line('e12', (23, 11), (17, 8))
        self.add_line('e13-1', (8, 8), (5, 9))
        self.add_line('e13-2', (5, 9), (4, 11))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e4', 'e10-1', 'e10-2', 'e5', 'e11-1', 'e11-2', 'e6', 'e12', 'e7', 'e13-1', 'e13-2', 'e8')
