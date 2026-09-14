"""Mindmap organize (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3cef74fe-690b-40bd-a920-baf04f6a2eb0'
SOURCE_PATH = 'icons-json/interface-essential/mindmap organize_3cef74fe-690b-40bd-a920-baf04f6a2eb0.json'
AUTHOR = 'json_to_solo'

class MindmapOrganize(Solo48):
    icon_id = 'mindmap-organize'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('mindmap', 'organize', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (4, 24), (20, 24))
        self.add_line('sym-e1', (20, 24), (24, 24))
        self.add_line('sym-e2', (24, 24), (28, 24))
        self.add_line('sym-e3', (28, 24), (44, 24))
        self.add_line('sym-e4', (4, 8), (14, 8))
        self.add_line('sym-e5', (14, 8), (15, 8))
        self.add_arc('sym-e6', (15, 8), (20, 15), radius_x=7)
        self.add_line('sym-e7', (20, 15), (20, 24))
        self.add_line('sym-e8', (20, 24), (20, 33))
        self.add_arc('sym-e9', (20, 33), (15, 40), radius_x=7)
        self.add_line('sym-e10', (15, 40), (14, 40))
        self.add_line('sym-e11', (14, 40), (4, 40))
        self.add_line('sym-e12', (44, 8), (34, 8))
        self.add_line('sym-e13', (34, 8), (33, 8))
        self.add_arc('sym-e14', (33, 8), (28, 15), radius_x=7, sweep=False)
        self.add_line('sym-e15', (28, 15), (28, 24))
        self.add_line('sym-e16', (28, 24), (28, 33))
        self.add_arc('sym-e17', (28, 33), (33, 40), radius_x=7, sweep=False)
        self.add_line('sym-e18', (33, 40), (34, 40))
        self.add_line('sym-e19', (34, 40), (44, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
