"""0 (text) (other), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e070fae7-149d-4c33-a2d6-4734b2d75e94'
SOURCE_PATH = 'icons-json/other/0 (text)_e070fae7-149d-4c33-a2d6-4734b2d75e94.json'
AUTHOR = 'json_to_solo'

class Icon0TextOther(Solo48):
    icon_id = 'icon-0-text-other'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('text', 'other')

    def build(self):
        self.add_line('sym-e0', (8, 24), (8, 24))
        self.add_bezier('sym-e1', (8, 24), ((8, 23.555), (8, 23.436), (8, 23)))
        self.add_bezier('sym-e2', (8, 23), ((8, 18.127), (9.258, 12.045), (13, 8)))
        self.add_bezier('sym-e3', (13, 8), ((15.117, 5.7), (19.037, 4), (23, 4)))
        self.add_bezier('sym-e4', (23, 4), ((23.234, 4), (23.766, 4), (24, 4)))
        self.add_bezier('sym-e5', (24, 4), ((24.099, 4), (23.902, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((24.049, 4), (23.951, 4), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.049, 4), (23.951, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.098, 4), (23.901, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.234, 4), (24.766, 4), (25, 4)))
        self.add_bezier('sym-e10', (25, 4), ((28.963, 4), (32.883, 5.7), (35, 8)))
        self.add_bezier('sym-e11', (35, 8), ((38.742, 12.045), (40, 18.127), (40, 23)))
        self.add_bezier('sym-e12', (40, 23), ((40, 23.436), (40, 23.555), (40, 24)))
        self.add_line('sym-e13', (40, 24), (40, 24))
        self.add_bezier('sym-e14', (40, 24), ((40, 24.445), (40, 24.564), (40, 25)))
        self.add_bezier('sym-e15', (40, 25), ((40, 29.873), (38.742, 35.955), (35, 40)))
        self.add_bezier('sym-e16', (35, 40), ((32.883, 42.3), (28.963, 44), (25, 44)))
        self.add_bezier('sym-e17', (25, 44), ((24.766, 44), (24.234, 44), (24, 44)))
        self.add_bezier('sym-e18', (24, 44), ((23.901, 44), (24.098, 44), (24, 44)))
        self.add_bezier('sym-e19', (24, 44), ((23.951, 44), (24.049, 44), (24, 44)))
        self.add_bezier('sym-e20', (24, 44), ((23.951, 44), (24.049, 44), (24, 44)))
        self.add_bezier('sym-e21', (24, 44), ((23.902, 44), (24.099, 44), (24, 44)))
        self.add_bezier('sym-e22', (24, 44), ((23.766, 44), (23.234, 44), (23, 44)))
        self.add_bezier('sym-e23', (23, 44), ((19.037, 44), (15.117, 42.3), (13, 40)))
        self.add_bezier('sym-e24', (13, 40), ((9.258, 35.955), (8, 29.873), (8, 25)))
        self.add_bezier('sym-e25', (8, 25), ((8, 24.564), (8, 24.445), (8, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', closed=True)
