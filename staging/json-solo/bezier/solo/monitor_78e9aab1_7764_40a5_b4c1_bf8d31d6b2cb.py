"""Batch-01/monitor (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb'
SOURCE_PATH = 'icons-json/computers/batch-01/monitor_78e9aab1-7764-40a5-b4c1-bf8d31d6b2cb.json'
AUTHOR = 'json_to_solo'

class Batch01Monitor78e9aab1(Solo48):
    icon_id = 'batch-01-monitor-78e9aab1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'monitor', 'computers')

    def build(self):
        self.add_line('sym-e0', (24, 40), (24, 32))
        self.add_line('sym-e1', (24, 32), (7, 32))
        self.add_bezier('sym-e2', (7, 32), ((5.973, 32), (4, 31.019), (4, 30)))
        self.add_bezier('sym-e3', (4, 30), ((4, 29.916), (4.009, 30.084), (4, 30)))
        self.add_line('sym-e4', (4, 30), (4, 11))
        self.add_bezier('sym-e5', (4, 11), ((4.182, 10.503), (4, 10.505), (4, 10)))
        self.add_bezier('sym-e6', (4, 10), ((4.536, 8.88), (5.7, 8), (7, 8)))
        self.add_bezier('sym-e7', (7, 8), ((7.109, 8), (7.891, 8.008), (8, 8)))
        self.add_line('sym-e8', (8, 8), (24, 8))
        self.add_line('sym-e9', (24, 8), (40, 8))
        self.add_bezier('sym-e10', (40, 8), ((40.109, 8.008), (40.891, 8), (41, 8)))
        self.add_bezier('sym-e11', (41, 8), ((42.3, 8), (43.464, 8.88), (44, 10)))
        self.add_bezier('sym-e12', (44, 10), ((44, 10.505), (43.818, 10.503), (44, 11)))
        self.add_line('sym-e13', (44, 11), (44, 30))
        self.add_bezier('sym-e14', (44, 30), ((43.991, 30.084), (44, 29.916), (44, 30)))
        self.add_bezier('sym-e15', (44, 30), ((44, 31.019), (42.027, 32), (41, 32)))
        self.add_line('sym-e16', (41, 32), (24, 32))
        self.add_line('sym-e17', (17, 40), (24, 40))
        self.add_line('sym-e18', (24, 40), (31, 40))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c1', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
