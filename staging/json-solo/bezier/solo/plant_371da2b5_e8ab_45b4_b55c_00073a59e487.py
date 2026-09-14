"""Plant (nature), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '371da2b5-e8ab-45b4-b55c-00073a59e487'
SOURCE_PATH = 'icons-json/nature/plant_371da2b5-e8ab-45b4-b55c-00073a59e487.json'
AUTHOR = 'json_to_solo'

class Plant371da2b5(Solo48):
    icon_id = 'plant-371da2b5'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature'
    aliases = ()
    keywords = ('plant', 'nature')

    def build(self):
        self.add_line('sym-e0', (24, 42), (24, 36))
        self.add_bezier('sym-e1', (24, 36), ((16.62, 36), (9.414, 32.094), (7, 25)))
        self.add_bezier('sym-e2', (7, 25), ((6.534, 23.634), (6, 21.456), (6, 20)))
        self.add_bezier('sym-e3', (6, 20), ((6, 19.869), (6, 20.131), (6, 20)))
        self.add_bezier('sym-e4', (6, 20), ((9.387, 20.205), (12.087, 21.216), (15, 23)))
        self.add_bezier('sym-e5', (15, 23), ((16.342, 23.818), (17.781, 25.018), (19, 26)))
        self.add_bezier('sym-e6', (19, 26), ((17.495, 20.134), (17.735, 15.326), (21, 10)))
        self.add_bezier('sym-e7', (21, 10), ((21.695, 8.863), (22.1, 7.974), (23, 7)))
        self.add_bezier('sym-e8', (23, 7), ((23.065, 6.929), (23.803, 6.205), (24, 6)))
        self.add_bezier('sym-e9', (24, 6), ((24.197, 6.205), (24.935, 6.929), (25, 7)))
        self.add_bezier('sym-e10', (25, 7), ((25.9, 7.974), (26.305, 8.863), (27, 10)))
        self.add_bezier('sym-e11', (27, 10), ((30.265, 15.326), (30.505, 20.134), (29, 26)))
        self.add_bezier('sym-e12', (29, 26), ((30.219, 25.018), (31.658, 23.818), (33, 23)))
        self.add_bezier('sym-e13', (33, 23), ((35.913, 21.216), (38.613, 20.205), (42, 20)))
        self.add_bezier('sym-e14', (42, 20), ((42, 20.131), (42, 19.869), (42, 20)))
        self.add_bezier('sym-e15', (42, 20), ((42, 21.456), (41.466, 23.634), (41, 25)))
        self.add_bezier('sym-e16', (41, 25), ((38.586, 32.094), (31.38, 36), (24, 36)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
