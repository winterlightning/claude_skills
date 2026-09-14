"""Double arrow left 2 (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '717cf8c7-9070-593d-91fb-e8cbbfd22322'
SOURCE_PATH = 'icons-json/arrows/double arrow left 2_717cf8c7-9070-593d-91fb-e8cbbfd22322.json'
AUTHOR = 'json_to_solo'

class DoubleArrowLeft2Arrows(Solo48):
    icon_id = 'double-arrow-left-2-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('double', 'arrow', 'left', 'arrows')

    def build(self):
        self.add_bezier('sym-e0', (22, 24), ((22, 24.993), (23.269, 26.211), (24, 27)))
        self.add_line('sym-e1', (24, 27), (40, 44))
        self.add_line('sym-e2', (25, 44), (9, 26))
        self.add_bezier('sym-e3', (9, 26), ((8.621, 25.564), (8, 24.664), (8, 24)))
        self.add_bezier('sym-e4', (8, 24), ((8, 23.936), (8, 24.055), (8, 24)))
        self.add_bezier('sym-e5', (8, 24), ((8, 23.965), (8, 24.033), (8, 24)))
        self.add_bezier('sym-e6', (8, 24), ((8, 23.967), (8, 24.035), (8, 24)))
        self.add_bezier('sym-e7', (8, 24), ((8, 23.945), (8, 24.064), (8, 24)))
        self.add_bezier('sym-e8', (8, 24), ((8, 23.336), (8.621, 22.436), (9, 22)))
        self.add_line('sym-e9', (9, 22), (25, 4))
        self.add_bezier('sym-e10', (22, 24), ((22, 23.007), (23.269, 21.789), (24, 21)))
        self.add_line('sym-e11', (24, 21), (40, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c2', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c2')
