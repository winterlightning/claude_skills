"""Batch-01/monitor (computers), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '181755f1-a8ab-4d25-8475-ebcf6885f0c8'
SOURCE_PATH = 'icons-json/computers/batch-01/monitor_181755f1-a8ab-4d25-8475-ebcf6885f0c8.json'
AUTHOR = 'gpt-6'

class Batch01Monitor(Solo48):
    icon_id = 'batch-01-monitor'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'monitor', 'computers')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 32))
        self.add_line('sym-e1', (24, 32), (7, 32))
        self.add_arc('sym-e2', (7, 32), (4, 30), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e4', (4, 30), (4, 10))
        self.add_arc('sym-e6', (4, 10), (7, 8), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('sym-e7', (7, 8), (41, 8))
        self.add_arc('sym-e11', (41, 8), (44, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sym-e12', (44, 10), (44, 11), radius_x=1, radius_y=1, large_arc=False, sweep=False)
        self.add_line('sym-e13', (44, 11), (44, 30))
        self.add_arc('sym-e15', (44, 30), (41, 32), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e16', (41, 32), (24, 32))
        self.add_line('sym-e17', (17, 40), (31, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', closed=False)
        self.add_contour('sym-c1', 'sym-e17', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
