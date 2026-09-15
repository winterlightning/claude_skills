"""Rounded rectangle shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '787addf8-2230-543a-ba7e-a43cf42d887d'
SOURCE_PATH = 'pictographic-primitives/design/rounded rectangle shape_787addf8-2230-543a-ba7e-a43cf42d887d.svg'
AUTHOR = 'gpt-6'

class RoundedRectangleShapeDesign(Solo48):
    icon_id = 'rounded-rectangle-shape-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rounded', 'rectangle', 'shape', 'design')

    def build(self):
        self.add_line('sym-e1', (4, 24), (4, 23))
        self.add_arc('sym-e2', (4, 23), (13, 8), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('sym-e3', (13, 8), (33, 8))
        self.add_arc('sym-e6', (33, 8), (44, 23), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('sym-e7', (44, 23), (44, 25))
        self.add_arc('sym-e9', (44, 25), (33, 40), radius_x=16, radius_y=16, large_arc=False, sweep=True)
        self.add_line('sym-e11', (33, 40), (13, 40))
        self.add_arc('sym-e13', (13, 40), (4, 25), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('sym-e14', (4, 25), (4, 24))
        self.add_contour('sym-c0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e11', 'sym-e13', 'sym-e14', closed=True)
