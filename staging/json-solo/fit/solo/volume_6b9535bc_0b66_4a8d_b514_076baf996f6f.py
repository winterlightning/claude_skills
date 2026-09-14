"""Volume (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b9535bc-0b66-4a8d-b514-076baf996f6f'
SOURCE_PATH = 'icons-json/interface-essential/volume_6b9535bc-0b66-4a8d-b514-076baf996f6f.json'
AUTHOR = 'json_to_solo'

class Volume6b9535bc(Solo48):
    icon_id = 'volume-6b9535bc'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('volume', 'interface-essential')

    def build(self):
        self.add_line('e0', (26, 8), (13, 17))
        self.add_line('e1', (4, 21), (4, 27))
        self.add_line('e2', (7, 30), (12, 30))
        self.add_line('e3', (13, 30), (26, 40))
        self.add_line('e4', (26, 40), (26, 34))
        self.add_line('e5', (26, 34), (26, 11))
        self.add_line('e6', (26, 11), (26, 8))
        self.add_arc('e7-1', (39, 13), (44, 23), radius_x=15)
        self.add_line('e7-2', (44, 23), (43, 29))
        self.add_arc('e7-3', (43, 29), (40, 34), radius_x=18)
        self.add_arc('e8', (34, 29), (34, 19), radius_x=8, sweep=False)
        self.add_arc('e9-1', (13, 17), (7, 18), radius_x=21)
        self.add_arc('e9-2', (7, 18), (4, 21), radius_x=3, sweep=False)
        self.add_arc('e10', (4, 27), (7, 30), radius_x=3, sweep=False)
        self.add_arc('e11', (12, 30), (13, 30), radius_x=1)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e7-3')
        self.add_contour('c1', 'e8')
        self.add_contour('c2', 'e0', 'e9-1', 'e9-2', 'e1', 'e10', 'e2', 'e11', 'e3', 'e4', 'e5', 'e6', closed=True)
