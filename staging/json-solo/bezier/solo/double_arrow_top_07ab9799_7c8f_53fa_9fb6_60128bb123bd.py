"""Double arrow top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07ab9799-7c8f-53fa-9fb6-60128bb123bd'
SOURCE_PATH = 'icons-json/arrows/double arrow top_07ab9799-7c8f-53fa-9fb6-60128bb123bd.json'
AUTHOR = 'json_to_solo'

class DoubleArrowTopArrows(Solo48):
    icon_id = 'double-arrow-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_bezier('sym-e0', (11, 28), ((9.998, 28), (8, 27.291), (8, 26)))
        self.add_bezier('sym-e1', (8, 26), ((8, 25.845), (8, 25.164), (8, 25)))
        self.add_bezier('sym-e2', (8, 25), ((8, 24.773), (8, 24.227), (8, 24)))
        self.add_bezier('sym-e3', (8, 24), ((8, 23.855), (8, 24.145), (8, 24)))
        self.add_line('sym-e4', (8, 24), (21, 6))
        self.add_bezier('sym-e5', (21, 6), ((21.337, 5.545), (22.427, 4), (23, 4)))
        self.add_bezier('sym-e6', (23, 4), ((23.051, 4), (23.949, 4.009), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.059, 4), (23.949, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.095, 4), (23.899, 4), (24, 4)))
        self.add_bezier('sym-e9', (24, 4), ((24.101, 4), (23.905, 4), (24, 4)))
        self.add_bezier('sym-e10', (24, 4), ((24.051, 4), (23.941, 4), (24, 4)))
        self.add_bezier('sym-e11', (24, 4), ((24.051, 4.009), (24.949, 4), (25, 4)))
        self.add_bezier('sym-e12', (25, 4), ((25.573, 4), (26.663, 5.545), (27, 6)))
        self.add_line('sym-e13', (27, 6), (40, 24))
        self.add_bezier('sym-e14', (40, 24), ((40, 24.145), (40, 23.855), (40, 24)))
        self.add_bezier('sym-e15', (40, 24), ((40, 24.227), (40, 24.773), (40, 25)))
        self.add_bezier('sym-e16', (40, 25), ((40, 25.164), (40, 25.845), (40, 26)))
        self.add_bezier('sym-e17', (40, 26), ((40, 27.291), (38.002, 28), (37, 28)))
        self.add_line('sym-e18', (37, 28), (30, 28))
        self.add_line('sym-e19', (30, 28), (40, 41))
        self.add_bezier('sym-e20', (40, 41), ((40, 41.136), (40, 41.864), (40, 42)))
        self.add_bezier('sym-e21', (40, 42), ((40, 42.245), (40, 41.755), (40, 42)))
        self.add_bezier('sym-e22', (40, 42), ((40, 42.055), (40, 42.945), (40, 43)))
        self.add_bezier('sym-e23', (40, 43), ((40, 44), (38.733, 44), (38, 44)))
        self.add_bezier('sym-e24', (38, 44), ((37.857, 44), (37.143, 44), (37, 44)))
        self.add_line('sym-e25', (37, 44), (24, 44))
        self.add_line('sym-e26', (24, 44), (11, 44))
        self.add_bezier('sym-e27', (11, 44), ((10.857, 44), (10.143, 44), (10, 44)))
        self.add_bezier('sym-e28', (10, 44), ((9.267, 44), (8, 44), (8, 43)))
        self.add_bezier('sym-e29', (8, 43), ((8, 42.945), (8, 42.055), (8, 42)))
        self.add_bezier('sym-e30', (8, 42), ((8, 41.755), (8, 42.245), (8, 42)))
        self.add_bezier('sym-e31', (8, 42), ((8, 41.864), (8, 41.136), (8, 41)))
        self.add_line('sym-e32', (8, 41), (18, 28))
        self.add_line('sym-e33', (18, 28), (11, 28))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', closed=True)
