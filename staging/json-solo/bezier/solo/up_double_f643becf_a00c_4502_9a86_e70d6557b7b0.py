"""Up double (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f643becf-a00c-4502-9a86-e70d6557b7b0'
SOURCE_PATH = 'icons-json/arrows/up double_f643becf-a00c-4502-9a86-e70d6557b7b0.json'
AUTHOR = 'json_to_solo'

class UpDoubleArrows(Solo48):
    icon_id = 'up-double-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('up', 'double', 'arrows')

    def build(self):
        self.add_line('sym-e0', (6, 10), (10, 6))
        self.add_line('sym-e1', (10, 6), (15, 11))
        self.add_line('sym-e2', (10, 6), (10, 29))
        self.add_bezier('sym-e3', (10, 29), ((10, 29.965), (10.722, 31.084), (11, 32)))
        self.add_bezier('sym-e4', (11, 32), ((12.645, 37.367), (17.183, 42), (23, 42)))
        self.add_bezier('sym-e5', (23, 42), ((23.123, 42), (23.877, 42), (24, 42)))
        self.add_bezier('sym-e6', (24, 42), ((24.094, 42), (23.904, 42), (24, 42)))
        self.add_bezier('sym-e7', (24, 42), ((24.096, 42), (23.906, 42), (24, 42)))
        self.add_bezier('sym-e8', (24, 42), ((24.123, 42), (24.877, 42), (25, 42)))
        self.add_bezier('sym-e9', (25, 42), ((30.817, 42), (35.355, 37.367), (37, 32)))
        self.add_bezier('sym-e10', (37, 32), ((37.278, 31.084), (38, 29.965), (38, 29)))
        self.add_line('sym-e11', (38, 29), (38, 6))
        self.add_line('sym-e12', (38, 6), (42, 10))
        self.add_line('sym-e13', (33, 11), (38, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12')
        self.add_contour('sym-c2', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
