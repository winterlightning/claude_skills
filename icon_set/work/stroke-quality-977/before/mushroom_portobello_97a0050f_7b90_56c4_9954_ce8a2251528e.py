"""Mushroom portobello (food), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a0050f-7b90-56c4-9954-ce8a2251528e'
SOURCE_PATH = 'pictographic-primitives/food/mushroom portobello_97a0050f-7b90-56c4-9954-ce8a2251528e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class MushroomPortobello(Solo48):
    icon_id = 'mushroom-portobello'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('mushroom', 'portobello', 'food')

    def build(self):
        self.add_arc('sym-e0', (30, 25), (27, 40), radius_x=11)
        self.add_line('sym-e1', (27, 40), (25, 40))
        self.add_arc('sym-e2', (25, 40), (24, 40), radius_x=1, sweep=False)
        self.add_arc('sym-e5', (24, 40), (23, 40), radius_x=1, sweep=False)
        self.add_line('sym-e6', (23, 40), (21, 40))
        self.add_arc('sym-e7', (21, 40), (18, 25), radius_x=11)
        self.add_arc('sym-e8', (18, 25), (24, 25), radius_x=72)
        self.add_arc('sym-e9', (24, 25), (30, 25), radius_x=72)
        self.add_line('sym-e10', (30, 25), (34, 25))
        self.add_line('sym-e11', (34, 25), (41, 27))
        self.add_line('sym-e12', (41, 27), (42, 26))
        self.add_arc('sym-e13', (42, 26), (44, 24), radius_x=2, sweep=False)
        self.add_line('sym-e14', (44, 24), (44, 23))
        self.add_arc('sym-e15', (44, 23), (44, 21), radius_x=11)
        self.add_arc('sym-e16-1', (44, 21), (37, 12), radius_x=15, sweep=False)
        self.add_arc('sym-e16-2', (37, 12), (24, 8), radius_x=24, sweep=False)
        self.add_arc('sym-e19-1', (24, 8), (11, 12), radius_x=24, sweep=False)
        self.add_arc('sym-e19-2', (11, 12), (4, 21), radius_x=15, sweep=False)
        self.add_arc('sym-e20', (4, 21), (4, 23), radius_x=11)
        self.add_line('sym-e21', (4, 23), (4, 24))
        self.add_arc('sym-e22', (4, 24), (6, 26), radius_x=2, sweep=False)
        self.add_line('sym-e23', (6, 26), (7, 27))
        self.add_line('sym-e24', (7, 27), (14, 25))
        self.add_line('sym-e25', (14, 25), (18, 25))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16-1', 'sym-e16-2', 'sym-e19-1', 'sym-e19-2', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
