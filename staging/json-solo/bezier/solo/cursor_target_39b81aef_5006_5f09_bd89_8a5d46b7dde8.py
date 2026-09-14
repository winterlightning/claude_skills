"""Cursor target (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39b81aef-5006-5f09-bd89-8a5d46b7dde8'
SOURCE_PATH = 'icons-json/interface-essential/cursor target_39b81aef-5006-5f09-bd89-8a5d46b7dde8.json'
AUTHOR = 'json_to_solo'

class CursorTargetInterfaceEssential(Solo48):
    icon_id = 'cursor-target-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cursor', 'target', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 31), (24, 36))
        self.add_line('sym-e1', (24, 36), (24, 42))
        self.add_line('sym-e2', (24, 17), (24, 12))
        self.add_line('sym-e3', (24, 12), (24, 6))
        self.add_line('sym-e4', (17, 24), (6, 24))
        self.add_bezier('sym-e5', (24, 12), ((21.513, 12.147), (19.078, 12.511), (17, 14)))
        self.add_bezier('sym-e6', (17, 14), ((13.596, 16.43), (12.27, 19.909), (12, 24)))
        self.add_bezier('sym-e7', (12, 24), ((11.959, 24.679), (11.885, 25.321), (12, 26)))
        self.add_bezier('sym-e8', (12, 26), ((12.968, 31.76), (18.252, 35.904), (24, 36)))
        self.add_bezier('sym-e9', (24, 36), ((29.748, 35.904), (35.032, 31.76), (36, 26)))
        self.add_bezier('sym-e10', (36, 26), ((36.115, 25.321), (36.041, 24.679), (36, 24)))
        self.add_bezier('sym-e11', (36, 24), ((35.73, 19.909), (34.404, 16.43), (31, 14)))
        self.add_bezier('sym-e12', (31, 14), ((28.922, 12.511), (26.487, 12.147), (24, 12)))
        self.add_line('sym-e13', (31, 24), (42, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
        self.add_contour('sym-c4', 'sym-e13')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
