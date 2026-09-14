"""Cat bed (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc88911f-a19f-4219-a235-ea1c5db29485'
SOURCE_PATH = 'icons-json/pets/cat bed_fc88911f-a19f-4219-a235-ea1c5db29485.json'
AUTHOR = 'json_to_solo'

class CatBedPets(Solo48):
    icon_id = 'cat-bed-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('cat', 'bed', 'pets')

    def build(self):
        self.add_line('sym-e0', (24, 40), (25, 40))
        self.add_line('sym-e1-1', (25, 40), (34, 39))
        self.add_line('sym-e1-2', (34, 39), (40, 37))
        self.add_arc('sym-e2', (40, 37), (44, 32), radius_x=7, sweep=False)
        self.add_line('sym-e5', (44, 32), (44, 18))
        self.add_line('sym-e6', (44, 18), (41, 20))
        self.add_line('sym-e7', (41, 20), (37, 18))
        self.add_line('sym-e8', (37, 18), (24, 16))
        self.add_line('sym-e9', (24, 16), (11, 18))
        self.add_arc('sym-e10', (11, 18), (7, 20), radius_x=26, sweep=False)
        self.add_line('sym-e11', (7, 20), (4, 18))
        self.add_line('sym-e12', (4, 18), (4, 32))
        self.add_arc('sym-e15', (4, 32), (8, 37), radius_x=7, sweep=False)
        self.add_arc('sym-e16-1', (8, 37), (14, 39), radius_x=25, sweep=False)
        self.add_line('sym-e16-2', (14, 39), (23, 40))
        self.add_line('sym-e17', (23, 40), (24, 40))
        self.add_line('sym-e18', (44, 18), (44, 15))
        self.add_arc('sym-e19', (44, 15), (44, 14), radius_x=1)
        self.add_arc('sym-e20', (44, 14), (39, 11), radius_x=9, sweep=False)
        self.add_arc('sym-e21', (39, 11), (26, 8), radius_x=35, sweep=False)
        self.add_arc('sym-e22', (26, 8), (25, 8), radius_x=1)
        self.add_arc('sym-e23', (25, 8), (24, 8), radius_x=41)
        self.add_arc('sym-e24', (24, 8), (23, 8), radius_x=39)
        self.add_arc('sym-e25', (23, 8), (22, 8), radius_x=1)
        self.add_arc('sym-e26', (22, 8), (9, 11), radius_x=35, sweep=False)
        self.add_arc('sym-e27', (9, 11), (4, 14), radius_x=9, sweep=False)
        self.add_line('sym-e28', (4, 14), (4, 15))
        self.add_line('sym-e29', (4, 15), (4, 18))
        self.add_line('sym-e30', (24, 30), (30, 30))
        self.add_line('sym-e31', (30, 30), (32, 29))
        self.add_arc('sym-e32', (32, 29), (33, 24), radius_x=5, sweep=False)
        self.add_line('sym-e33', (33, 24), (34, 23))
        self.add_line('sym-e34', (34, 23), (39, 21))
        self.add_line('sym-e35', (39, 21), (41, 20))
        self.add_line('sym-e36', (24, 30), (18, 30))
        self.add_line('sym-e37', (18, 30), (16, 29))
        self.add_arc('sym-e38', (16, 29), (15, 24), radius_x=5)
        self.add_line('sym-e39', (15, 24), (14, 23))
        self.add_line('sym-e40', (14, 23), (9, 21))
        self.add_line('sym-e41', (9, 21), (7, 20))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1-1', 'sym-e1-2', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e15', 'sym-e16-1', 'sym-e16-2', 'sym-e17', closed=True)
        self.add_contour('sym-c1', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
        self.add_contour('sym-c2', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35')
        self.add_contour('sym-c3', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
