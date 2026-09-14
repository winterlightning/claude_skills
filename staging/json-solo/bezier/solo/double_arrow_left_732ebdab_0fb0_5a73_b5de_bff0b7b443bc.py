"""Double arrow left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '732ebdab-0fb0-5a73-b5de-bff0b7b443bc'
SOURCE_PATH = 'icons-json/arrows/double arrow left_732ebdab-0fb0-5a73-b5de-bff0b7b443bc.json'
AUTHOR = 'json_to_solo'

class DoubleArrowLeftArrows(Solo48):
    icon_id = 'double-arrow-left-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'left', 'arrows')

    def build(self):
        self.add_line('sym-e0', (44, 24), (44, 37))
        self.add_bezier('sym-e1', (44, 37), ((44, 37.143), (44, 37.857), (44, 38)))
        self.add_bezier('sym-e2', (44, 38), ((44, 38.733), (44, 40), (43, 40)))
        self.add_bezier('sym-e3', (43, 40), ((42.945, 40), (42.055, 40), (42, 40)))
        self.add_bezier('sym-e4', (42, 40), ((41.755, 40), (42.245, 40), (42, 40)))
        self.add_bezier('sym-e5', (42, 40), ((41.864, 40), (41.136, 40), (41, 40)))
        self.add_line('sym-e6', (41, 40), (28, 30))
        self.add_line('sym-e7', (28, 30), (28, 37))
        self.add_bezier('sym-e8', (28, 37), ((28, 38.002), (27.291, 40), (26, 40)))
        self.add_bezier('sym-e9', (26, 40), ((25.845, 40), (25.164, 40), (25, 40)))
        self.add_bezier('sym-e10', (25, 40), ((24.773, 40), (24.227, 40), (24, 40)))
        self.add_bezier('sym-e11', (24, 40), ((23.855, 40), (24.145, 40), (24, 40)))
        self.add_line('sym-e12', (24, 40), (6, 27))
        self.add_bezier('sym-e13', (6, 27), ((5.545, 26.663), (4, 25.573), (4, 25)))
        self.add_bezier('sym-e14', (4, 25), ((4, 24.949), (4.009, 24.051), (4, 24)))
        self.add_bezier('sym-e15', (4, 24), ((4, 23.941), (4, 24.051), (4, 24)))
        self.add_bezier('sym-e16', (4, 24), ((4, 23.905), (4, 24.101), (4, 24)))
        self.add_bezier('sym-e17', (4, 24), ((4, 23.899), (4, 24.095), (4, 24)))
        self.add_bezier('sym-e18', (4, 24), ((4, 23.949), (4, 24.059), (4, 24)))
        self.add_bezier('sym-e19', (4, 24), ((4.009, 23.949), (4, 23.051), (4, 23)))
        self.add_bezier('sym-e20', (4, 23), ((4, 22.427), (5.545, 21.337), (6, 21)))
        self.add_line('sym-e21', (6, 21), (24, 8))
        self.add_bezier('sym-e22', (24, 8), ((24.145, 8), (23.855, 8), (24, 8)))
        self.add_bezier('sym-e23', (24, 8), ((24.227, 8), (24.773, 8), (25, 8)))
        self.add_bezier('sym-e24', (25, 8), ((25.164, 8), (25.845, 8), (26, 8)))
        self.add_bezier('sym-e25', (26, 8), ((27.291, 8), (28, 9.998), (28, 11)))
        self.add_line('sym-e26', (28, 11), (28, 18))
        self.add_line('sym-e27', (28, 18), (41, 8))
        self.add_bezier('sym-e28', (41, 8), ((41.136, 8), (41.864, 8), (42, 8)))
        self.add_bezier('sym-e29', (42, 8), ((42.245, 8), (41.755, 8), (42, 8)))
        self.add_bezier('sym-e30', (42, 8), ((42.055, 8), (42.945, 8), (43, 8)))
        self.add_bezier('sym-e31', (43, 8), ((44, 8), (44, 9.267), (44, 10)))
        self.add_bezier('sym-e32', (44, 10), ((44, 10.143), (44, 10.857), (44, 11)))
        self.add_line('sym-e33', (44, 11), (44, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
