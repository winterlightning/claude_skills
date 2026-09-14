"""Ad (text) (other), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('e7-1', (14, 10), (12, 8), radius_x=2, sweep=False)
        self.add_line('e7-2', (12, 8), (10, 9))
        self.add_arc('e8-1', (37, 40), (41, 37), radius_x=7, sweep=False)
        self.add_arc('e8-2', (41, 37), (43, 33), radius_x=14, sweep=False)
        self.add_arc('e8-3', (43, 33), (44, 27), radius_x=19, sweep=False)
        self.add_arc('e8-4', (44, 27), (44, 26), radius_x=30)
        self.add_arc('e9-1', (44, 20), (42, 13), radius_x=14, sweep=False)
        self.add_arc('e9-2', (42, 13), (35, 8), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e7-1', 'e7-2', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e4', 'e9-1', 'e9-2', 'e5', 'e6', closed=True)
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
