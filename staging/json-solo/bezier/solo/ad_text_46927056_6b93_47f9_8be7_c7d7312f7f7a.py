"""Ad (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46927056-6b93-47f9-8be7-c7d7312f7f7a'
SOURCE_PATH = 'icons-json/other/AD (text)_46927056-6b93-47f9-8be7-c7d7312f7f7a.json'
AUTHOR = 'json_to_solo'

class AdTextOther(Solo48):
    icon_id = 'ad-text-other'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('ad', 'text', 'other')

    def build(self):
        self.add_line('e0', (20, 40), (14, 10))
        self.add_line('e1', (10, 9), (4, 40))
        self.add_line('e2', (7, 29), (18, 29))
        self.add_line('e3', (29, 40), (37, 40))
        self.add_line('e4', (44, 26), (44, 20))
        self.add_line('e5', (35, 8), (29, 8))
        self.add_line('e6', (29, 8), (29, 40))
        self.add_bezier('e7', (14, 10), ((13.682, 8.535), (13.2, 8.025), (12.009, 8.025)), ((11.891, 8.012), (11.773, 8.012), (11.664, 8)), ((11, 8), (10.191, 8.102), (10, 9)))
        self.add_bezier('e8', (37, 40), ((37.555, 40), (37.873, 39.631), (38.382, 39.348)), ((41.691, 37.551), (43.982, 32.443), (43.982, 27.668)), ((43.991, 27.458), (43.991, 27.262), (44, 27.065)), ((44, 26.868), (44, 26.197), (44, 26)))
        self.add_bezier('e9', (44, 20), ((43.991, 19.902), (43.991, 20.111), (43.982, 20)), ((43.982, 14.338), (39.582, 8.012), (35.345, 8.012)), ((35.273, 8.012), (35.2, 8), (35.127, 8)), ((35.055, 8), (35.073, 8), (35, 8)))
        self.add_contour('c0', 'e0', 'e7', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e8', 'e4', 'e9', 'e5', 'e6', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
