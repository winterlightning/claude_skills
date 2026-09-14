"""Double arrow bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5f5f6da-8db6-57b5-9fbb-9c29c2944a84'
SOURCE_PATH = 'icons-json/arrows/double arrow bottom_e5f5f6da-8db6-57b5-9fbb-9c29c2944a84.json'
AUTHOR = 'json_to_solo'

class DoubleArrowBottomArrows(Solo48):
    icon_id = 'double-arrow-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'bottom', 'arrows')

    def build(self):
        self.add_line('sym-e0', (24, 4), (37, 4))
        self.add_bezier('sym-e1', (37, 4), ((37.143, 4), (37.857, 4), (38, 4)))
        self.add_bezier('sym-e2', (38, 4), ((38.733, 4), (40, 4), (40, 5)))
        self.add_bezier('sym-e3', (40, 5), ((40, 5.055), (40, 5.945), (40, 6)))
        self.add_bezier('sym-e4', (40, 6), ((40, 6.245), (40, 5.755), (40, 6)))
        self.add_bezier('sym-e5', (40, 6), ((40, 6.136), (40, 6.864), (40, 7)))
        self.add_line('sym-e6', (40, 7), (30, 20))
        self.add_line('sym-e7', (30, 20), (37, 20))
        self.add_bezier('sym-e8', (37, 20), ((38.002, 20), (40, 20.709), (40, 22)))
        self.add_bezier('sym-e9', (40, 22), ((40, 22.155), (40, 22.836), (40, 23)))
        self.add_bezier('sym-e10', (40, 23), ((40, 23.227), (40, 23.773), (40, 24)))
        self.add_bezier('sym-e11', (40, 24), ((40, 24.145), (40, 23.855), (40, 24)))
        self.add_line('sym-e12', (40, 24), (27, 42))
        self.add_bezier('sym-e13', (27, 42), ((26.663, 42.455), (25.573, 44), (25, 44)))
        self.add_bezier('sym-e14', (25, 44), ((24.949, 44), (24.051, 43.991), (24, 44)))
        self.add_bezier('sym-e15', (24, 44), ((23.941, 44), (24.051, 44), (24, 44)))
        self.add_bezier('sym-e16', (24, 44), ((23.905, 44), (24.101, 44), (24, 44)))
        self.add_bezier('sym-e17', (24, 44), ((23.899, 44), (24.095, 44), (24, 44)))
        self.add_bezier('sym-e18', (24, 44), ((23.949, 44), (24.059, 44), (24, 44)))
        self.add_bezier('sym-e19', (24, 44), ((23.949, 43.991), (23.051, 44), (23, 44)))
        self.add_bezier('sym-e20', (23, 44), ((22.427, 44), (21.337, 42.455), (21, 42)))
        self.add_line('sym-e21', (21, 42), (8, 24))
        self.add_bezier('sym-e22', (8, 24), ((8, 23.855), (8, 24.145), (8, 24)))
        self.add_bezier('sym-e23', (8, 24), ((8, 23.773), (8, 23.227), (8, 23)))
        self.add_bezier('sym-e24', (8, 23), ((8, 22.836), (8, 22.155), (8, 22)))
        self.add_bezier('sym-e25', (8, 22), ((8, 20.709), (9.998, 20), (11, 20)))
        self.add_line('sym-e26', (11, 20), (18, 20))
        self.add_line('sym-e27', (18, 20), (8, 7))
        self.add_bezier('sym-e28', (8, 7), ((8, 6.864), (8, 6.136), (8, 6)))
        self.add_bezier('sym-e29', (8, 6), ((8, 5.755), (8, 6.245), (8, 6)))
        self.add_bezier('sym-e30', (8, 6), ((8, 5.945), (8, 5.055), (8, 5)))
        self.add_bezier('sym-e31', (8, 5), ((8, 4), (9.267, 4), (10, 4)))
        self.add_bezier('sym-e32', (10, 4), ((10.143, 4), (10.857, 4), (11, 4)))
        self.add_line('sym-e33', (11, 4), (24, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
