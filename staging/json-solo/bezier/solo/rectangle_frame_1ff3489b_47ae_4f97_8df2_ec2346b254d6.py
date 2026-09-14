"""Rectangle frame (design), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ff3489b-47ae-4f97-8df2-ec2346b254d6'
SOURCE_PATH = 'icons-json/design/rectangle frame_1ff3489b-47ae-4f97-8df2-ec2346b254d6.json'
AUTHOR = 'json_to_solo'

class RectangleFrameDesign(Solo48):
    icon_id = 'rectangle-frame-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('rectangle', 'frame', 'design')

    def build(self):
        self.add_line('sym-e0', (5, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (43, 8))
        self.add_bezier('sym-e2', (43, 8), ((43.245, 8.21), (43.8, 8.69), (44, 9)))
        self.add_bezier('sym-e3', (44, 9), ((44, 9.16), (43.882, 8.83), (44, 9)))
        self.add_line('sym-e4', (44, 9), (44, 24))
        self.add_line('sym-e5', (44, 24), (44, 39))
        self.add_bezier('sym-e6', (44, 39), ((43.882, 39.17), (44, 38.84), (44, 39)))
        self.add_bezier('sym-e7', (44, 39), ((43.8, 39.31), (43.245, 39.79), (43, 40)))
        self.add_line('sym-e8', (43, 40), (24, 40))
        self.add_line('sym-e9', (24, 40), (5, 40))
        self.add_bezier('sym-e10', (5, 40), ((4.755, 39.79), (4.2, 39.31), (4, 39)))
        self.add_bezier('sym-e11', (4, 39), ((4, 38.84), (4.118, 39.17), (4, 39)))
        self.add_line('sym-e12', (4, 39), (4, 24))
        self.add_line('sym-e13', (4, 24), (4, 9))
        self.add_bezier('sym-e14', (4, 9), ((4.118, 8.83), (4, 9.16), (4, 9)))
        self.add_bezier('sym-e15', (4, 9), ((4.2, 8.69), (4.755, 8.21), (5, 8)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', closed=True)
