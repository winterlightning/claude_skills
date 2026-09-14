"""Double arrow right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed70003a-c057-54c5-881a-b3ad2feedaf5'
SOURCE_PATH = 'icons-json/arrows/double arrow right_ed70003a-c057-54c5-881a-b3ad2feedaf5.json'
AUTHOR = 'json_to_solo'

class DoubleArrowRightArrows(Solo48):
    icon_id = 'double-arrow-right-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'right', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 24), (4, 11))
        self.add_bezier('sym-e1', (4, 11), ((4, 10.857), (4, 10.143), (4, 10)))
        self.add_bezier('sym-e2', (4, 10), ((4, 9.267), (4, 8), (5, 8)))
        self.add_bezier('sym-e3', (5, 8), ((5.055, 8), (5.945, 8), (6, 8)))
        self.add_bezier('sym-e4', (6, 8), ((6.245, 8), (5.755, 8), (6, 8)))
        self.add_bezier('sym-e5', (6, 8), ((6.136, 8), (6.864, 8), (7, 8)))
        self.add_line('sym-e6', (7, 8), (20, 18))
        self.add_line('sym-e7', (20, 18), (20, 11))
        self.add_bezier('sym-e8', (20, 11), ((20, 9.998), (20.709, 8), (22, 8)))
        self.add_bezier('sym-e9', (22, 8), ((22.155, 8), (22.836, 8), (23, 8)))
        self.add_bezier('sym-e10', (23, 8), ((23.227, 8), (23.773, 8), (24, 8)))
        self.add_bezier('sym-e11', (24, 8), ((24.145, 8), (23.855, 8), (24, 8)))
        self.add_line('sym-e12', (24, 8), (42, 21))
        self.add_bezier('sym-e13', (42, 21), ((42.455, 21.337), (44, 22.427), (44, 23)))
        self.add_bezier('sym-e14', (44, 23), ((44, 23.051), (43.991, 23.949), (44, 24)))
        self.add_bezier('sym-e15', (44, 24), ((44, 24.059), (44, 23.949), (44, 24)))
        self.add_bezier('sym-e16', (44, 24), ((44, 24.095), (44, 23.899), (44, 24)))
        self.add_bezier('sym-e17', (44, 24), ((44, 24.101), (44, 23.905), (44, 24)))
        self.add_bezier('sym-e18', (44, 24), ((44, 24.051), (44, 23.941), (44, 24)))
        self.add_bezier('sym-e19', (44, 24), ((43.991, 24.051), (44, 24.949), (44, 25)))
        self.add_bezier('sym-e20', (44, 25), ((44, 25.573), (42.455, 26.663), (42, 27)))
        self.add_line('sym-e21', (42, 27), (24, 40))
        self.add_bezier('sym-e22', (24, 40), ((23.855, 40), (24.145, 40), (24, 40)))
        self.add_bezier('sym-e23', (24, 40), ((23.773, 40), (23.227, 40), (23, 40)))
        self.add_bezier('sym-e24', (23, 40), ((22.836, 40), (22.155, 40), (22, 40)))
        self.add_bezier('sym-e25', (22, 40), ((20.709, 40), (20, 38.002), (20, 37)))
        self.add_line('sym-e26', (20, 37), (20, 30))
        self.add_line('sym-e27', (20, 30), (7, 40))
        self.add_bezier('sym-e28', (7, 40), ((6.864, 40), (6.136, 40), (6, 40)))
        self.add_bezier('sym-e29', (6, 40), ((5.755, 40), (6.245, 40), (6, 40)))
        self.add_bezier('sym-e30', (6, 40), ((5.945, 40), (5.055, 40), (5, 40)))
        self.add_bezier('sym-e31', (5, 40), ((4, 40), (4, 38.733), (4, 38)))
        self.add_bezier('sym-e32', (4, 38), ((4, 37.857), (4, 37.143), (4, 37)))
        self.add_line('sym-e33', (4, 37), (4, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
