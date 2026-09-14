"""End point triangle arrow 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50e2631e-8d3a-4df5-902e-0a6b04d1633d'
SOURCE_PATH = 'icons-json/arrows/end point triangle arrow 2_50e2631e-8d3a-4df5-902e-0a6b04d1633d.json'
AUTHOR = 'json_to_solo'

class EndPointTriangleArrow2Arrows(Solo48):
    icon_id = 'end-point-triangle-arrow-2-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('end', 'point', 'triangle', 'arrow', 'arrows')

    def build(self):
        self.add_line('sym-e0', (4, 24), (29, 24))
        self.add_line('sym-e1', (29, 24), (29, 11))
        self.add_bezier('sym-e2', (29, 11), ((29.118, 9.512), (29.918, 8), (31, 8)))
        self.add_bezier('sym-e3', (31, 8), ((31.036, 8), (30.964, 8), (31, 8)))
        self.add_bezier('sym-e4', (31, 8), ((31.091, 8), (30.909, 8), (31, 8)))
        self.add_line('sym-e5', (31, 8), (43, 21))
        self.add_bezier('sym-e6', (43, 21), ((43.436, 21.464), (44, 23.12), (44, 24)))
        self.add_bezier('sym-e7', (44, 24), ((44, 24.08), (44, 23.92), (44, 24)))
        self.add_bezier('sym-e8', (44, 24), ((44, 24.054), (44, 23.947), (44, 24)))
        self.add_bezier('sym-e9', (44, 24), ((44, 24.053), (44, 23.946), (44, 24)))
        self.add_bezier('sym-e10', (44, 24), ((44, 24.08), (44, 23.92), (44, 24)))
        self.add_bezier('sym-e11', (44, 24), ((44, 24.88), (43.436, 26.536), (43, 27)))
        self.add_line('sym-e12', (43, 27), (31, 40))
        self.add_bezier('sym-e13', (31, 40), ((30.909, 40), (31.091, 40), (31, 40)))
        self.add_bezier('sym-e14', (31, 40), ((30.964, 40), (31.036, 40), (31, 40)))
        self.add_bezier('sym-e15', (31, 40), ((29.918, 40), (29.118, 38.488), (29, 37)))
        self.add_line('sym-e16', (29, 37), (29, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
