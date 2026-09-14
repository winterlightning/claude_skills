"""Area chart (business), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6257590-657e-51af-a63e-8c11b469d3e0'
SOURCE_PATH = 'icons-json/business/area chart_a6257590-657e-51af-a63e-8c11b469d3e0.json'
AUTHOR = 'json_to_solo'

class AreaChartBusiness(Solo48):
    icon_id = 'area-chart-business'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('area', 'chart', 'business')

    def build(self):
        self.add_line('e0', (4, 8), (4, 40))
        self.add_line('e1', (4, 40), (44, 40))
        self.add_line('e2', (4, 34), (12, 25))
        self.add_line('e3', (19, 25), (24, 17))
        self.add_line('e4', (37, 19), (43, 12))
        self.add_arc('e5-1', (12, 25), (14, 24), radius_x=2)
        self.add_line('e5-2', (14, 24), (17, 26))
        self.add_line('e5-3', (17, 26), (19, 25))
        self.add_arc('e6-1', (24, 17), (27, 16), radius_x=2)
        self.add_arc('e6-2', (27, 16), (33, 20), radius_x=30)
        self.add_arc('e6-3', (33, 20), (37, 19), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e3', 'e6-1', 'e6-2', 'e6-3', 'e4')
        self.relate('connect', 'c1', 'c0')
