"""Area chart (business), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e5', (12, 25), ((14.482, 22.187), (17.109, 27.627), (19, 25)))
        self.add_bezier('e6', (24, 17), ((24.5, 16.309), (25.255, 15.663), (26.245, 15.629)), ((27.745, 15.579), (31.091, 18.846), (32.164, 19.646)), ((32.782, 20.101), (33.473, 20.632), (34.318, 20.573)), ((35.427, 20.497), (36.327, 19.707), (37, 19)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e5', 'e3', 'e6', 'e4')
        self.relate('connect', 'c1', 'c0')
