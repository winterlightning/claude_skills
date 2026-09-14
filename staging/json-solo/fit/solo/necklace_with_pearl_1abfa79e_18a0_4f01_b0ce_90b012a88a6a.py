"""Batch-06/necklace with pearl (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1abfa79e-18a0-4f01-b0ce-90b012a88a6a'
SOURCE_PATH = 'icons-json/accessories/batch-06/necklace with pearl_1abfa79e-18a0-4f01-b0ce-90b012a88a6a.json'
AUTHOR = 'json_to_solo'

class Batch06NecklaceWithPearl(Solo48):
    icon_id = 'batch-06-necklace-with-pearl'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'necklace', 'with', 'pearl', 'accessories')

    def build(self):
        self.add_arc('sym-e0', (19, 39), (29, 39), radius_x=5)
        self.add_arc('sym-e1', (29, 39), (19, 39), radius_x=5)
        self.add_arc('sym-e2', (21, 34), (10, 24), radius_x=36)
        self.add_arc('sym-e3', (10, 24), (16, 17), radius_x=23)
        self.add_arc('sym-e4', (16, 17), (24, 15), radius_x=14)
        self.add_arc('sym-e5', (24, 15), (32, 17), radius_x=14)
        self.add_arc('sym-e6', (32, 17), (38, 24), radius_x=22)
        self.add_arc('sym-e7', (38, 24), (27, 34), radius_x=36)
        self.add_arc('sym-e8', (10, 24), (8, 18), radius_x=16)
        self.add_line('sym-e9', (8, 18), (8, 17))
        self.add_line('sym-e10', (8, 17), (8, 16))
        self.add_arc('sym-e11-1', (8, 16), (13, 7), radius_x=11)
        self.add_arc('sym-e11-2', (13, 7), (23, 4), radius_x=19)
        self.add_arc('sym-e12', (23, 4), (24, 4), radius_x=70, sweep=False)
        self.add_line('sym-e15', (24, 4), (25, 4))
        self.add_arc('sym-e16-1', (25, 4), (35, 7), radius_x=19)
        self.add_arc('sym-e16-2', (35, 7), (40, 16), radius_x=11)
        self.add_line('sym-e17', (40, 16), (40, 17))
        self.add_line('sym-e18', (40, 17), (40, 18))
        self.add_arc('sym-e19', (40, 18), (38, 24), radius_x=15)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11-1', 'sym-e11-2', 'sym-e12', 'sym-e15', 'sym-e16-1', 'sym-e16-2', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
