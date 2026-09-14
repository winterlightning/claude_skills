"""Office folder sealed (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '612a7027-d24a-5b4f-b90f-0091cbbdf60f'
SOURCE_PATH = 'icons-json/office/office folder sealed_612a7027-d24a-5b4f-b90f-0091cbbdf60f.json'
AUTHOR = 'json_to_solo'

class OfficeFolderSealedOffice(Solo48):
    icon_id = 'office-folder-sealed-office'
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
        self.add_bezier('e9', (4, 35), ((4, 35.724), (4.009, 36.404), (4.009, 37.128)), ((4.009, 38.728), (5.7, 40), (7.336, 40)), ((7.436, 40), (7.9, 40), (8, 40)))
        self.add_bezier('e10', (39, 40), ((39.218, 40), (39.882, 39.992), (40.1, 39.992)), ((40.245, 39.992), (40.391, 39.992), (40.536, 39.992)), ((40.609, 39.992), (40.682, 40), (40.755, 40)), ((40.827, 39.992), (40.9, 39.992), (40.973, 39.992)), ((42.3, 39.992), (43.982, 38.232), (43.982, 37.036)), ((43.991, 36.968), (43.991, 36.901), (44, 36.834)), ((44, 36.766), (44, 37.067), (44, 37)))
        self.add_bezier('e11', (44, 15), ((44, 14.756), (43.991, 14.248), (43.991, 14.004)), ((43.991, 12.362), (42.855, 11), (41, 11)))
        self.add_bezier('e12', (23, 11), ((22.6, 10.857), (22.282, 11.124), (21.909, 10.922)), ((20.282, 10.063), (19.055, 8.008), (16.991, 8.008)), ((16.9, 8.008), (17.091, 8), (17, 8)))
        self.add_bezier('e13', (8, 8), ((6.309, 8), (4.009, 9.541), (4.009, 11.166)), ((4.009, 11.234), (4, 10.933), (4, 11)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12', 'e7', 'e13', 'e8')
