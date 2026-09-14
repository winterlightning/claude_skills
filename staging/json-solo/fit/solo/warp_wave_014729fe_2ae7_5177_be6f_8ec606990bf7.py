"""Warp wave (design), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '014729fe-2ae7-5177-be6f-8ec606990bf7'
SOURCE_PATH = 'icons-json/design/warp wave_014729fe-2ae7-5177-be6f-8ec606990bf7.json'
AUTHOR = 'json_to_solo'

class WarpWaveDesign(Solo48):
    icon_id = 'warp-wave-design'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'wave', 'design')

    def build(self):
        self.add_line('e0', (27, 38), (22, 34))
        self.add_arc('e1-1', (4, 12), (14, 8), radius_x=16)
        self.add_arc('e1-2', (14, 8), (16, 8), radius_x=33, sweep=False)
        self.add_line('e1-3', (16, 8), (32, 16))
        self.add_arc('e1-4', (32, 16), (44, 10), radius_x=13, sweep=False)
        self.add_arc('e2-1', (4, 24), (16, 20), radius_x=16)
        self.add_arc('e2-2', (16, 20), (28, 27), radius_x=26)
        self.add_arc('e2-3', (28, 27), (35, 28), radius_x=13, sweep=False)
        self.add_arc('e2-4', (35, 28), (44, 22), radius_x=15, sweep=False)
        self.add_arc('e3-1', (44, 34), (34, 40), radius_x=14)
        self.add_line('e3-2', (34, 40), (27, 38))
        self.add_arc('e4', (22, 34), (4, 36), radius_x=14, sweep=False)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
        self.add_contour('c2', 'e3-1', 'e3-2', 'e0', 'e4')
