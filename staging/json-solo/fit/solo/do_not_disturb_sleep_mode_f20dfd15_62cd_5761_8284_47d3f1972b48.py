"""Do not disturb sleep mode (mobile), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f20dfd15-62cd-5761-8284-47d3f1972b48'
SOURCE_PATH = 'icons-json/mobile/do not disturb sleep mode_f20dfd15-62cd-5761-8284-47d3f1972b48.json'
AUTHOR = 'json_to_solo'

class DoNotDisturbSleepModeMobile(Solo48):
    icon_id = 'do-not-disturb-sleep-mode-mobile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('do', 'not', 'disturb', 'sleep', 'mode', 'mobile')

    def build(self):
        self.add_arc('e0-1', (21, 6), (42, 30), radius_x=16, sweep=False)
        self.add_arc('e0-2', (42, 30), (36, 38), radius_x=24)
        self.add_arc('e0-3', (36, 38), (30, 41), radius_x=18)
        self.add_line('e0-4', (30, 41), (24, 42))
        self.add_arc('e0-5', (24, 42), (6, 24), radius_x=18)
        self.add_arc('e0-6', (6, 24), (7, 18), radius_x=19)
        self.add_arc('e0-7', (7, 18), (9, 14), radius_x=18)
        self.add_arc('e0-8', (9, 14), (21, 6), radius_x=18)
        self.add_contour('c0', 'e0-1', 'e0-2', 'e0-3', 'e0-4', 'e0-5', 'e0-6', 'e0-7', 'e0-8', closed=True)
