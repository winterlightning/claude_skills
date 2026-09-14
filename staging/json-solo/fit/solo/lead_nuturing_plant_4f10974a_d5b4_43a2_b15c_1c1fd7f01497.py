"""Lead nuturing plant (nature), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f10974a-d5b4-43a2-b15c-1c1fd7f01497'
SOURCE_PATH = 'icons-json/nature/lead nuturing plant_4f10974a-d5b4-43a2-b15c-1c1fd7f01497.json'
AUTHOR = 'json_to_solo'

class LeadNuturingPlantNature(Solo48):
    icon_id = 'lead-nuturing-plant-nature'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('lead', 'nuturing', 'plant', 'nature')

    def build(self):
        self.add_line('e0', (23, 37), (25, 37))
        self.add_arc('e1', (36, 21), (29, 29), radius_x=44, sweep=False)
        self.add_arc('e2', (11, 18), (19, 28), radius_x=34)
        self.add_arc('e3', (9, 40), (23, 37), radius_x=36)
        self.add_arc('e4', (39, 40), (25, 37), radius_x=37, sweep=False)
        self.add_arc('e5', (23, 37), (19, 28), radius_x=47, sweep=False)
        self.add_arc('e6', (25, 37), (29, 29), radius_x=66)
        self.add_arc('e7-1', (29, 29), (30, 16), radius_x=9)
        self.add_arc('e7-2', (30, 16), (43, 9), radius_x=35)
        self.add_line('e7-3', (43, 9), (44, 16))
        self.add_line('e7-4', (44, 16), (43, 23))
        self.add_arc('e7-5', (43, 23), (41, 27), radius_x=13)
        self.add_arc('e7-6', (41, 27), (29, 29), radius_x=8)
        self.add_arc('e8-1', (19, 29), (20, 17), radius_x=12, sweep=False)
        self.add_arc('e8-2', (20, 17), (5, 8), radius_x=26, sweep=False)
        self.add_arc('e8-3', (5, 8), (4, 15), radius_x=39, sweep=False)
        self.add_line('e8-4', (4, 15), (5, 22))
        self.add_arc('e8-5', (5, 22), (7, 26), radius_x=11, sweep=False)
        self.add_arc('e8-6', (7, 26), (19, 28), radius_x=8, sweep=False)
        self.add_contour('c0', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e0')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', closed=True)
        self.add_contour('c8', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e8-5', 'e8-6')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
