"""Christmas sock (holidays), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2717434c-419a-5ee7-81cd-f47a96b06ddc'
SOURCE_PATH = 'icons-json/holidays/christmas sock_2717434c-419a-5ee7-81cd-f47a96b06ddc.json'
AUTHOR = 'json_to_solo'

class ChristmasSock(Solo48):
    icon_id = 'christmas-sock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'holidays'
    aliases = ()
    keywords = ('christmas', 'sock', 'holidays')

    def build(self):
        self.add_line('e0', (37, 13), (37, 31))
        self.add_line('e1', (29, 41), (17, 44))
        self.add_line('e2', (20, 21), (20, 13))
        self.add_line('e3', (21, 13), (36, 13))
        self.add_line('e4', (37, 4), (20, 4))
        self.add_arc('e5', (37, 31), (29, 41), radius_x=9)
        self.add_arc('e6-1', (17, 44), (8, 35), radius_x=9)
        self.add_arc('e6-2', (8, 35), (10, 29), radius_x=10)
        self.add_line('e6-3', (10, 29), (17, 25))
        self.add_arc('e6-4', (17, 25), (20, 21), radius_x=5, sweep=False)
        self.add_arc('e7-1', (36, 13), (39, 12), radius_x=4, sweep=False)
        self.add_line('e7-2', (39, 12), (40, 7))
        self.add_arc('e7-3', (40, 7), (37, 4), radius_x=3, sweep=False)
        self.add_arc('e8-1', (20, 4), (17, 11), radius_x=5, sweep=False)
        self.add_arc('e8-2', (17, 11), (21, 13), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e2')
        self.add_contour('c1', 'e3', 'e7-1', 'e7-2', 'e7-3', 'e4', 'e8-1', 'e8-2', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
