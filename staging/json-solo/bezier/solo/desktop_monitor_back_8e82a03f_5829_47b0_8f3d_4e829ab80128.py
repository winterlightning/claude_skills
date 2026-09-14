"""Batch-01/desktop monitor back (computers), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e82a03f-5829-47b0-8f3d-4e829ab80128'
SOURCE_PATH = 'icons-json/computers/batch-01/desktop monitor back_8e82a03f-5829-47b0-8f3d-4e829ab80128.json'
AUTHOR = 'json_to_solo'

class Batch01DesktopMonitorBack(Solo48):
    icon_id = 'batch-01-desktop-monitor-back'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    aliases = ()
    keywords = ('batch', 'desktop', 'monitor', 'back', 'computers')

    def build(self):
        self.add_line('sym-e0', (17, 40), (24, 40))
        self.add_line('sym-e1', (24, 40), (31, 40))
        self.add_line('sym-e2', (24, 40), (24, 32))
        self.add_line('sym-e3', (24, 32), (39, 32))
        self.add_bezier('sym-e4', (39, 32), ((40.855, 32), (43.291, 31.676), (44, 30)))
        self.add_bezier('sym-e5', (44, 30), ((44, 29.705), (44, 29.328), (44, 29)))
        self.add_line('sym-e6', (44, 29), (44, 12))
        self.add_bezier('sym-e7', (44, 12), ((44, 11.857), (44, 12.143), (44, 12)))
        self.add_bezier('sym-e8', (44, 12), ((44, 10.189), (41.791, 8.404), (40, 8)))
        self.add_bezier('sym-e9', (40, 8), ((39.482, 8), (39.527, 8), (39, 8)))
        self.add_bezier('sym-e10', (39, 8), ((38.627, 8), (38.373, 8), (38, 8)))
        self.add_line('sym-e11', (38, 8), (24, 8))
        self.add_line('sym-e12', (24, 8), (10, 8))
        self.add_bezier('sym-e13', (10, 8), ((9.627, 8), (9.373, 8), (9, 8)))
        self.add_bezier('sym-e14', (9, 8), ((8.473, 8), (8.518, 8), (8, 8)))
        self.add_bezier('sym-e15', (8, 8), ((6.209, 8.404), (4, 10.189), (4, 12)))
        self.add_bezier('sym-e16', (4, 12), ((4, 12.143), (4, 11.857), (4, 12)))
        self.add_line('sym-e17', (4, 12), (4, 29))
        self.add_bezier('sym-e18', (4, 29), ((4, 29.328), (4, 29.705), (4, 30)))
        self.add_bezier('sym-e19', (4, 30), ((4.709, 31.676), (7.145, 32), (9, 32)))
        self.add_line('sym-e20', (9, 32), (24, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
