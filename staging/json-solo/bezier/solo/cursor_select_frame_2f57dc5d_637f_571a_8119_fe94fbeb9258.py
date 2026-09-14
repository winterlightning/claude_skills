"""Cursor select frame (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2f57dc5d-637f-571a-8119-fe94fbeb9258'
SOURCE_PATH = 'icons-json/interface-essential/cursor select frame_2f57dc5d-637f-571a-8119-fe94fbeb9258.json'
AUTHOR = 'json_to_solo'

class CursorSelectFrame2f57dc5d(Solo48):
    icon_id = 'cursor-select-frame-2f57dc5d'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'select', 'frame', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 16), (6, 8))
        self.add_bezier('sym-e1', (6, 8), ((6, 7.812), (6, 8.196), (6, 8)))
        self.add_bezier('sym-e2', (6, 8), ((6, 7.01), (7.043, 6), (8, 6)))
        self.add_bezier('sym-e3', (8, 6), ((8.057, 6), (7.935, 6), (8, 6)))
        self.add_bezier('sym-e4', (8, 6), ((8.115, 6), (7.885, 6), (8, 6)))
        self.add_line('sym-e5', (8, 6), (17, 6))
        self.add_line('sym-e6', (31, 6), (40, 6))
        self.add_bezier('sym-e7', (40, 6), ((40.188, 6), (39.82, 6), (40, 6)))
        self.add_bezier('sym-e8', (40, 6), ((41.006, 6), (42, 7.018), (42, 8)))
        self.add_bezier('sym-e9', (42, 8), ((42, 8.065), (42, 7.935), (42, 8)))
        self.add_bezier('sym-e10', (42, 8), ((42, 8.123), (42, 7.877), (42, 8)))
        self.add_line('sym-e11', (42, 8), (42, 16))
        self.add_line('sym-e12', (6, 32), (6, 40))
        self.add_bezier('sym-e13', (6, 40), ((6, 40.188), (6, 39.804), (6, 40)))
        self.add_bezier('sym-e14', (6, 40), ((6, 40.99), (7.043, 42), (8, 42)))
        self.add_bezier('sym-e15', (8, 42), ((8.057, 42), (7.935, 42), (8, 42)))
        self.add_bezier('sym-e16', (8, 42), ((8.115, 42), (7.885, 42), (8, 42)))
        self.add_line('sym-e17', (8, 42), (17, 42))
        self.add_line('sym-e18', (31, 42), (40, 42))
        self.add_bezier('sym-e19', (40, 42), ((40.188, 42), (39.82, 42), (40, 42)))
        self.add_bezier('sym-e20', (40, 42), ((41.006, 42), (42, 40.982), (42, 40)))
        self.add_bezier('sym-e21', (42, 40), ((42, 39.935), (42, 40.065), (42, 40)))
        self.add_bezier('sym-e22', (42, 40), ((42, 39.877), (42, 40.123), (42, 40)))
        self.add_line('sym-e23', (42, 40), (42, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c1', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17')
        self.add_contour('sym-c3', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23')
