"""Fishing line (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd931a080-b0aa-5280-b50e-074e997cbca4'
SOURCE_PATH = 'icons-json/outdoors/fishing line_d931a080-b0aa-5280-b50e-074e997cbca4.json'
AUTHOR = 'json_to_solo'

class FishingLine(Solo48):
    icon_id = 'fishing-line'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('fishing', 'line', 'outdoors')

    def build(self):
        self.add_line('e0', (33, 4), (33, 13))
        self.add_line('e1', (13, 34), (8, 30))
        self.add_line('e2', (8, 30), (8, 37))
        self.add_line('e3', (33, 37), (33, 20))
        self.add_arc('e4-top', (26, 17), (40, 17), radius_x=7, radius_y=4)
        self.add_arc('e4-bottom', (40, 17), (26, 17), radius_x=7, radius_y=4)
        self.add_arc('e5-1', (8, 37), (12, 42), radius_x=6, sweep=False)
        self.add_arc('e5-2', (12, 42), (20, 44), radius_x=18, sweep=False)
        self.add_line('e5-3', (20, 44), (27, 43))
        self.add_arc('e5-4', (27, 43), (33, 37), radius_x=7, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
