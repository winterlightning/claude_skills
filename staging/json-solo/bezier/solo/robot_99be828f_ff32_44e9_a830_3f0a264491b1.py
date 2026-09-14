"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '99be828f-ff32-44e9-a830-3f0a264491b1'
SOURCE_PATH = 'icons-json/artificial-intelligence/robot_99be828f-ff32-44e9-a830-3f0a264491b1.json'
AUTHOR = 'json_to_solo'

class Robot(Solo48):
    icon_id = 'robot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 17))
        self.add_line('sym-e1', (24, 17), (11, 17))
        self.add_bezier('sym-e2', (11, 17), ((8.644, 17), (6, 19.832), (6, 22)))
        self.add_line('sym-e3', (6, 22), (6, 36))
        self.add_bezier('sym-e4', (6, 36), ((6, 36.09), (6, 36.91), (6, 37)))
        self.add_bezier('sym-e5', (6, 37), ((6, 39.201), (8.693, 42), (11, 42)))
        self.add_line('sym-e6', (11, 42), (24, 42))
        self.add_line('sym-e7', (24, 42), (37, 42))
        self.add_bezier('sym-e8', (37, 42), ((39.307, 42), (42, 39.201), (42, 37)))
        self.add_bezier('sym-e9', (42, 37), ((42, 36.91), (42, 36.09), (42, 36)))
        self.add_line('sym-e10', (42, 36), (42, 22))
        self.add_bezier('sym-e11', (42, 22), ((42, 19.832), (39.356, 17), (37, 17)))
        self.add_line('sym-e12', (37, 17), (24, 17))
        self.add_line('sym-e13', (17, 27), (17, 32))
        self.add_line('sym-e14', (31, 27), (31, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13')
        self.add_contour('sym-c2', 'sym-e14')
