"""End point triangle arrow 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
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
        self.add_arc('sym-e2', (29, 11), (31, 8), radius_x=3)
        self.add_line('sym-e5', (31, 8), (43, 21))
        self.add_line('sym-e6', (43, 21), (44, 24))
        self.add_line('sym-e11', (44, 24), (43, 27))
        self.add_line('sym-e12', (43, 27), (31, 40))
        self.add_arc('sym-e15', (31, 40), (29, 37), radius_x=3)
        self.add_line('sym-e16', (29, 37), (29, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e11', 'sym-e12', 'sym-e15', 'sym-e16')
