"""Rectangle dots (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a85ee0a-25fe-413a-b15f-b957051e288b'
SOURCE_PATH = 'icons-json/state/rectangle dots_1a85ee0a-25fe-413a-b15f-b957051e288b.json'
AUTHOR = 'json_to_solo'

class RectangleDotsState(Solo48):
    icon_id = 'rectangle-dots-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('rectangle', 'dots', 'state')

    def build(self):
        self.add_bezier('sym-e0', (24, 14), ((24, 14.3), (24, 14.7), (24, 15)))
        self.add_bezier('sym-e1', (24, 32), ((24, 32.3), (24, 32.7), (24, 33)))
        self.add_line('sym-e2', (40, 10), (40, 6))
        self.add_bezier('sym-e3', (40, 6), ((39.988, 5.927), (40, 6.073), (40, 6)))
        self.add_bezier('sym-e4', (40, 6), ((40, 5.245), (39.022, 4), (38, 4)))
        self.add_bezier('sym-e5', (38, 4), ((37.902, 4), (38.098, 4), (38, 4)))
        self.add_line('sym-e6', (38, 4), (30, 4))
        self.add_line('sym-e7', (40, 38), (40, 42))
        self.add_bezier('sym-e8', (40, 42), ((39.988, 42.073), (40, 41.927), (40, 42)))
        self.add_bezier('sym-e9', (40, 42), ((40, 42.755), (39.022, 44), (38, 44)))
        self.add_bezier('sym-e10', (38, 44), ((37.902, 44), (38.098, 44), (38, 44)))
        self.add_line('sym-e11', (38, 44), (30, 44))
        self.add_line('sym-e12', (39, 18), (39, 29))
        self.add_line('sym-e13', (8, 10), (8, 6))
        self.add_bezier('sym-e14', (8, 6), ((8.012, 5.927), (8, 6.073), (8, 6)))
        self.add_bezier('sym-e15', (8, 6), ((8, 5.245), (8.978, 4), (10, 4)))
        self.add_bezier('sym-e16', (10, 4), ((10.098, 4), (9.902, 4), (10, 4)))
        self.add_line('sym-e17', (10, 4), (18, 4))
        self.add_line('sym-e18', (8, 38), (8, 42))
        self.add_bezier('sym-e19', (8, 42), ((8.012, 42.073), (8, 41.927), (8, 42)))
        self.add_bezier('sym-e20', (8, 42), ((8, 42.755), (8.978, 44), (10, 44)))
        self.add_bezier('sym-e21', (10, 44), ((10.098, 44), (9.902, 44), (10, 44)))
        self.add_line('sym-e22', (10, 44), (18, 44))
        self.add_line('sym-e23', (9, 18), (9, 29))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1')
        self.add_contour('sym-c2', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c3', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c4', 'sym-e12')
        self.add_contour('sym-c5', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c6', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22')
        self.add_contour('sym-c7', 'sym-e23')
