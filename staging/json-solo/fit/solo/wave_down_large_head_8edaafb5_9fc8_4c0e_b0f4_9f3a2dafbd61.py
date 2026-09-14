"""Wave down large head (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8edaafb5-9fc8-4c0e-b0f4-9f3a2dafbd61'
SOURCE_PATH = 'icons-json/arrows/wave down large head_8edaafb5-9fc8-4c0e-b0f4-9f3a2dafbd61.json'
AUTHOR = 'json_to_solo'

class WaveDownLargeHeadArrows(Solo48):
    icon_id = 'wave-down-large-head-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('wave', 'down', 'large', 'head', 'arrows')

    def build(self):
        self.add_line('e0', (13, 13), (13, 34))
        self.add_line('e1', (27, 34), (27, 14))
        self.add_line('e2', (39, 14), (39, 26))
        self.add_line('e3', (34, 21), (39, 26))
        self.add_line('e4', (44, 21), (39, 26))
        self.add_arc('e5-1', (4, 8), (8, 8), radius_x=33, sweep=False)
        self.add_arc('e5-2', (8, 8), (13, 13), radius_x=6)
        self.add_arc('e6-1', (13, 34), (15, 38), radius_x=9, sweep=False)
        self.add_line('e6-2', (15, 38), (20, 40))
        self.add_line('e6-3', (20, 40), (25, 38))
        self.add_line('e6-4', (25, 38), (27, 34))
        self.add_arc('e7-1', (27, 14), (33, 8), radius_x=7)
        self.add_arc('e7-2', (33, 8), (39, 14), radius_x=7)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e1', 'e7-1', 'e7-2', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
