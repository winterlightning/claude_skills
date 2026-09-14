"""Trash (state), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e0c6d19-547e-46f0-8ec6-c837972fb3f0'
SOURCE_PATH = 'icons-json/state/trash_5e0c6d19-547e-46f0-8ec6-c837972fb3f0.json'
AUTHOR = 'json_to_solo'

class Trash5e0c6d19(Solo48):
    icon_id = 'trash-5e0c6d19'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('trash', 'state')

    def build(self):
        self.add_line('sym-e0', (17, 13), (31, 13))
        self.add_bezier('sym-e1', (31, 13), ((30.995, 12.867), (31, 13.135), (31, 13)))
        self.add_bezier('sym-e2', (31, 13), ((31, 10.783), (32.028, 8.504), (30, 7)))
        self.add_bezier('sym-e3', (30, 7), ((29.575, 6.681), (28.556, 6), (28, 6)))
        self.add_bezier('sym-e4', (28, 6), ((27.959, 6), (28.041, 6.008), (28, 6)))
        self.add_line('sym-e5', (28, 6), (24, 6))
        self.add_line('sym-e6', (24, 6), (20, 6))
        self.add_bezier('sym-e7', (20, 6), ((19.959, 6.008), (20.041, 6), (20, 6)))
        self.add_bezier('sym-e8', (20, 6), ((19.444, 6), (18.425, 6.681), (18, 7)))
        self.add_bezier('sym-e9', (18, 7), ((15.972, 8.504), (17, 10.783), (17, 13)))
        self.add_bezier('sym-e10', (17, 13), ((17, 13.135), (17.005, 12.867), (17, 13)))
        self.add_line('sym-e11', (17, 13), (8, 13))
        self.add_line('sym-e12', (8, 13), (6, 13))
        self.add_line('sym-e13', (42, 13), (40, 13))
        self.add_line('sym-e14', (40, 13), (36, 40))
        self.add_bezier('sym-e15', (36, 40), ((35.877, 40.957), (34.974, 42), (34, 42)))
        self.add_line('sym-e16', (34, 42), (24, 42))
        self.add_line('sym-e17', (24, 42), (14, 42))
        self.add_bezier('sym-e18', (14, 42), ((13.026, 42), (12.123, 40.957), (12, 40)))
        self.add_line('sym-e19', (12, 40), (8, 13))
        self.add_line('sym-e20', (31, 13), (40, 13))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c1', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c2', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
