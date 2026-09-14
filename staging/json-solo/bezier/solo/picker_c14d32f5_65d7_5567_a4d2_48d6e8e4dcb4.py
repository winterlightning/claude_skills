"""Picker (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c14d32f5-65d7-5567-a4d2-48d6e8e4dcb4'
SOURCE_PATH = 'icons-json/design/picker_c14d32f5-65d7-5567-a4d2-48d6e8e4dcb4.json'
AUTHOR = 'json_to_solo'

class PickerC14d32f5(Solo48):
    icon_id = 'picker-c14d32f5'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('picker', 'design')

    def build(self):
        self.add_line('sym-e0', (40, 19), (8, 19))
        self.add_line('sym-e1', (24, 4), (24, 4))
        self.add_bezier('sym-e2', (24, 4), ((24.053, 4), (23.946, 4), (24, 4)))
        self.add_bezier('sym-e3', (24, 4), ((25.424, 4), (26.848, 4.573), (28, 5)))
        self.add_bezier('sym-e4', (28, 5), ((31.344, 6.236), (34, 7.682), (34, 10)))
        self.add_line('sym-e5', (34, 10), (34, 31))
        self.add_bezier('sym-e6', (34, 31), ((34, 32.682), (33.552, 34.509), (32, 36)))
        self.add_bezier('sym-e7', (32, 36), ((30.816, 37.127), (28.512, 37.682), (28, 39)))
        self.add_bezier('sym-e8', (28, 39), ((27.424, 40.491), (28.992, 43.218), (26, 44)))
        self.add_bezier('sym-e9', (26, 44), ((25.536, 44), (24.496, 44), (24, 44)))
        self.add_bezier('sym-e10', (24, 44), ((23.905, 44), (24.09, 44), (24, 44)))
        self.add_bezier('sym-e11', (24, 44), ((23.91, 44), (24.095, 44), (24, 44)))
        self.add_bezier('sym-e12', (24, 44), ((23.504, 44), (22.464, 44), (22, 44)))
        self.add_bezier('sym-e13', (22, 44), ((19.008, 43.218), (20.576, 40.491), (20, 39)))
        self.add_bezier('sym-e14', (20, 39), ((19.488, 37.682), (17.184, 37.127), (16, 36)))
        self.add_bezier('sym-e15', (16, 36), ((14.448, 34.509), (14, 32.682), (14, 31)))
        self.add_line('sym-e16', (14, 31), (14, 10))
        self.add_bezier('sym-e17', (14, 10), ((14, 7.682), (16.656, 6.236), (20, 5)))
        self.add_bezier('sym-e18', (20, 5), ((21.152, 4.573), (22.576, 4), (24, 4)))
        self.add_bezier('sym-e19', (24, 4), ((24.054, 4), (23.947, 4), (24, 4)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
