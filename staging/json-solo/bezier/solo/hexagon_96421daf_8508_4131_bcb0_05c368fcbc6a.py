"""Hexagon (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96421daf-8508-4131-bcb0-05c368fcbc6a'
SOURCE_PATH = 'icons-json/design/hexagon_96421daf-8508-4131-bcb0-05c368fcbc6a.json'
AUTHOR = 'json_to_solo'

class Hexagon96421daf(Solo48):
    icon_id = 'hexagon-96421daf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('hexagon', 'design')

    def build(self):
        self.add_line('sym-e0', (8, 24), (8, 15))
        self.add_bezier('sym-e1', (8, 15), ((8.16, 14.427), (8.461, 13.345), (9, 13)))
        self.add_line('sym-e2', (9, 13), (23, 4))
        self.add_bezier('sym-e3', (23, 4), ((23.202, 4), (23.798, 4), (24, 4)))
        self.add_bezier('sym-e4', (24, 4), ((24.081, 4), (23.919, 4), (24, 4)))
        self.add_bezier('sym-e5', (24, 4), ((24.081, 4), (23.919, 4), (24, 4)))
        self.add_bezier('sym-e6', (24, 4), ((24.202, 4), (24.798, 4), (25, 4)))
        self.add_line('sym-e7', (25, 4), (39, 13))
        self.add_bezier('sym-e8', (39, 13), ((39.539, 13.345), (39.84, 14.427), (40, 15)))
        self.add_line('sym-e9', (40, 15), (40, 24))
        self.add_line('sym-e10', (40, 24), (40, 33))
        self.add_bezier('sym-e11', (40, 33), ((39.84, 33.573), (39.539, 34.655), (39, 35)))
        self.add_line('sym-e12', (39, 35), (25, 44))
        self.add_bezier('sym-e13', (25, 44), ((24.798, 44), (24.202, 44), (24, 44)))
        self.add_bezier('sym-e14', (24, 44), ((23.919, 44), (24.081, 44), (24, 44)))
        self.add_bezier('sym-e15', (24, 44), ((23.919, 44), (24.081, 44), (24, 44)))
        self.add_bezier('sym-e16', (24, 44), ((23.798, 44), (23.202, 44), (23, 44)))
        self.add_line('sym-e17', (23, 44), (9, 35))
        self.add_bezier('sym-e18', (9, 35), ((8.461, 34.655), (8.16, 33.573), (8, 33)))
        self.add_line('sym-e19', (8, 33), (8, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
