"""House (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f2c3cd65-0c37-5f94-b1b9-40450b3afc1a'
SOURCE_PATH = 'icons-json/interface-essential/house_f2c3cd65-0c37-5f94-b1b9-40450b3afc1a.json'
AUTHOR = 'json_to_solo'

class House(Solo48):
    icon_id = 'house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('house', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (42, 24), (37, 19))
        self.add_line('sym-e1', (37, 19), (24, 6))
        self.add_line('sym-e2', (24, 6), (11, 19))
        self.add_line('sym-e3', (11, 19), (6, 24))
        self.add_line('sym-e4', (37, 19), (37, 42))
        self.add_line('sym-e5', (37, 42), (29, 42))
        self.add_line('sym-e6', (29, 42), (19, 42))
        self.add_line('sym-e7', (19, 42), (11, 42))
        self.add_line('sym-e8', (11, 42), (11, 19))
        self.add_line('sym-e9', (29, 42), (29, 34))
        self.add_bezier('sym-e10', (29, 34), ((29, 31.464), (27.577, 28.581), (25, 28)))
        self.add_bezier('sym-e11', (25, 28), ((24.695, 27.93), (24.31, 28), (24, 28)))
        self.add_bezier('sym-e12', (24, 28), ((23.69, 28), (23.305, 27.93), (23, 28)))
        self.add_bezier('sym-e13', (23, 28), ((20.423, 28.581), (19, 31.464), (19, 34)))
        self.add_line('sym-e14', (19, 34), (19, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
