"""Oval 1 (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fb3135a9-0f07-4fe3-96c8-fd473915e0c0'
SOURCE_PATH = 'icons-json/symbol/oval 1_fb3135a9-0f07-4fe3-96c8-fd473915e0c0.json'
AUTHOR = 'json_to_solo'

class Oval1Symbol(Solo48):
    icon_id = 'oval-1-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('oval', 'symbol')

    def build(self):
        self.add_bezier('sym-e0', (8, 24), ((8.004, 23.793), (8, 23.205), (8, 23)))
        self.add_bezier('sym-e1', (8, 23), ((8, 16.191), (11.22, 8.509), (18, 5)))
        self.add_bezier('sym-e2', (18, 5), ((19.58, 4.182), (21.16, 4), (23, 4)))
        self.add_bezier('sym-e3', (23, 4), ((23.16, 4), (23.84, 4), (24, 4)))
        self.add_bezier('sym-e4', (24, 4), ((24.053, 4), (23.947, 4), (24, 4)))
        self.add_bezier('sym-e5', (24, 4), ((24.027, 4), (23.973, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((24.027, 4), (23.973, 4), (24, 4)))
        self.add_bezier('sym-e7', (24, 4), ((24.053, 4), (23.947, 4), (24, 4)))
        self.add_bezier('sym-e8', (24, 4), ((24.16, 4), (24.84, 4), (25, 4)))
        self.add_bezier('sym-e9', (25, 4), ((26.84, 4), (28.42, 4.182), (30, 5)))
        self.add_bezier('sym-e10', (30, 5), ((36.78, 8.509), (40, 16.191), (40, 23)))
        self.add_bezier('sym-e11', (40, 23), ((40, 23.205), (39.996, 23.793), (40, 24)))
        self.add_bezier('sym-e12', (40, 24), ((39.996, 24.207), (40, 24.795), (40, 25)))
        self.add_bezier('sym-e13', (40, 25), ((40, 31.809), (36.78, 39.491), (30, 43)))
        self.add_bezier('sym-e14', (30, 43), ((28.42, 43.818), (26.84, 44), (25, 44)))
        self.add_bezier('sym-e15', (25, 44), ((24.84, 44), (24.16, 44), (24, 44)))
        self.add_bezier('sym-e16', (24, 44), ((23.947, 44), (24.053, 44), (24, 44)))
        self.add_bezier('sym-e17', (24, 44), ((23.973, 44), (24.027, 44), (24, 44)))
        self.add_bezier('sym-e18', (24, 44), ((23.973, 44), (24.027, 44), (24, 44)))
        self.add_bezier('sym-e19', (24, 44), ((23.947, 44), (24.053, 44), (24, 44)))
        self.add_bezier('sym-e20', (24, 44), ((23.84, 44), (23.16, 44), (23, 44)))
        self.add_bezier('sym-e21', (23, 44), ((21.16, 44), (19.58, 43.818), (18, 43)))
        self.add_bezier('sym-e22', (18, 43), ((11.22, 39.491), (8, 31.809), (8, 25)))
        self.add_bezier('sym-e23', (8, 25), ((8, 24.795), (8.004, 24.207), (8, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', closed=True)
