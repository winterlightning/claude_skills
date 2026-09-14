"""Warp arc upper (design), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '41afe867-f59f-5952-985b-78e3355127ff'
SOURCE_PATH = 'icons-json/design/warp arc upper_41afe867-f59f-5952-985b-78e3355127ff.json'
AUTHOR = 'json_to_solo'

class WarpArcUpperDesign(Solo48):
    icon_id = 'warp-arc-upper-design'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arc', 'upper', 'design')

    def build(self):
        self.add_bezier('sym-e0', (24, 4), ((23.98, 4), (24.02, 4), (24, 4)))
        self.add_bezier('sym-e1', (24, 4), ((23.731, 4), (23.269, 4), (23, 4)))
        self.add_bezier('sym-e2', (23, 4), ((15.084, 4), (8, 12.573), (8, 21)))
        self.add_bezier('sym-e3', (8, 21), ((8, 21.3), (8, 21.7), (8, 22)))
        self.add_bezier('sym-e4', (8, 22), ((8, 22.145), (8, 21.855), (8, 22)))
        self.add_line('sym-e5', (8, 22), (8, 44))
        self.add_line('sym-e6', (8, 44), (24, 44))
        self.add_line('sym-e7', (24, 44), (40, 44))
        self.add_line('sym-e8', (40, 44), (40, 22))
        self.add_bezier('sym-e9', (40, 22), ((40, 21.855), (40, 22.145), (40, 22)))
        self.add_bezier('sym-e10', (40, 22), ((40, 21.7), (40, 21.3), (40, 21)))
        self.add_bezier('sym-e11', (40, 21), ((40, 12.573), (32.916, 4), (25, 4)))
        self.add_bezier('sym-e12', (25, 4), ((24.731, 4), (24.269, 4), (24, 4)))
        self.add_bezier('sym-e13', (24, 4), ((23.98, 4), (24.02, 4), (24, 4)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', closed=True)
