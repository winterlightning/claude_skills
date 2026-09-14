"""Diving boat (recreation), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204ae051-9164-4427-9aed-ae16980f534d'
SOURCE_PATH = 'icons-json/recreation/diving boat_204ae051-9164-4427-9aed-ae16980f534d.json'
AUTHOR = 'json_to_solo'

class DivingBoatRecreation(Solo48):
    icon_id = 'diving-boat-recreation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('diving', 'boat', 'recreation')

    def build(self):
        self.add_line('e0', (16, 8), (19, 15))
        self.add_line('e1', (19, 15), (14, 18))
        self.add_line('e2', (11, 33), (37, 18))
        self.add_line('e3', (23, 12), (19, 15))
        self.add_line('e4', (19, 15), (23, 26))
        self.add_line('e5', (4, 40), (6, 40))
        self.add_arc('e6', (37, 18), (35, 33), radius_x=25)
        self.add_line('e7-1', (6, 40), (9, 38))
        self.add_arc('e7-2', (9, 38), (13, 40), radius_x=5, sweep=False)
        self.add_line('e7-3', (13, 40), (17, 39))
        self.add_arc('e7-4', (17, 39), (19, 37), radius_x=9)
        self.add_arc('e7-5', (19, 37), (24, 40), radius_x=7, sweep=False)
        self.add_arc('e7-6', (24, 40), (29, 37), radius_x=6, sweep=False)
        self.add_line('e7-7', (29, 37), (30, 36))
        self.add_arc('e7-8', (30, 36), (35, 40), radius_x=6, sweep=False)
        self.add_arc('e7-9', (35, 40), (40, 37), radius_x=7, sweep=False)
        self.add_arc('e7-10', (40, 37), (44, 40), radius_x=8, sweep=False)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e7-1', 'e7-2', 'e7-3', 'e7-4', 'e7-5', 'e7-6', 'e7-7', 'e7-8', 'e7-9', 'e7-10')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
