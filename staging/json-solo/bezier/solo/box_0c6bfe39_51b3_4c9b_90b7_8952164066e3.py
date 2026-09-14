"""Box (shipping), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c6bfe39-51b3-4c9b-90b7-8952164066e3'
SOURCE_PATH = 'icons-json/shipping/box_0c6bfe39-51b3-4c9b-90b7-8952164066e3.json'
AUTHOR = 'json_to_solo'

class Box0c6bfe39(Solo48):
    icon_id = 'box-0c6bfe39'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'shipping'
    aliases = ()
    keywords = ('box', 'shipping')

    def build(self):
        self.add_line('sym-e0', (42, 15), (24, 15))
        self.add_line('sym-e1', (24, 15), (6, 15))
        self.add_line('sym-e2', (6, 15), (6, 42))
        self.add_line('sym-e3', (6, 42), (42, 42))
        self.add_line('sym-e4', (42, 42), (42, 15))
        self.add_bezier('sym-e5', (42, 15), ((41.624, 14.435), (42, 15.54), (42, 15)))
        self.add_bezier('sym-e6', (42, 15), ((41.812, 14.665), (41.262, 13.368), (41, 13)))
        self.add_bezier('sym-e7', (41, 13), ((39.748, 11.208), (38.317, 9.743), (37, 8)))
        self.add_bezier('sym-e8', (37, 8), ((36.55, 7.411), (35.892, 6), (35, 6)))
        self.add_bezier('sym-e9', (35, 6), ((34.918, 6), (35.082, 6), (35, 6)))
        self.add_line('sym-e10', (35, 6), (24, 6))
        self.add_line('sym-e11', (24, 6), (24, 15))
        self.add_bezier('sym-e12', (6, 15), ((6.376, 14.435), (6, 15.54), (6, 15)))
        self.add_bezier('sym-e13', (6, 15), ((6.188, 14.665), (6.738, 13.368), (7, 13)))
        self.add_bezier('sym-e14', (7, 13), ((8.252, 11.208), (9.683, 9.743), (11, 8)))
        self.add_bezier('sym-e15', (11, 8), ((11.45, 7.411), (12.108, 6), (13, 6)))
        self.add_bezier('sym-e16', (13, 6), ((13.082, 6), (12.918, 6), (13, 6)))
        self.add_line('sym-e17', (13, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c1', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
