"""Mindmap organize (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cef74fe-690b-40bd-a920-baf04f6a2eb0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/mindmap organize_3cef74fe-690b-40bd-a920-baf04f6a2eb0.svg'
AUTHOR = 'gpt-6'

class MindmapOrganize(Solo48):
    icon_id = 'mindmap-organize'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('mindmap', 'organize', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (4, 24), (44, 24))
        self.add_line('sym-e4', (4, 8), (15, 8))
        self.add_arc('sym-e6', (15, 8), (20, 15), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e7', (20, 15), (20, 33))
        self.add_arc('sym-e9', (20, 33), (15, 40), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('sym-e10', (15, 40), (4, 40))
        self.add_line('sym-e12', (44, 8), (33, 8))
        self.add_arc('sym-e14', (33, 8), (28, 15), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e15', (28, 15), (28, 33))
        self.add_arc('sym-e17', (28, 33), (33, 40), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e18', (33, 40), (44, 40))
        self.add_contour('sym-c0', 'sym-e0', closed=False)
        self.add_contour('sym-c1', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', closed=False)
        self.add_contour('sym-c2', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', closed=False)
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
