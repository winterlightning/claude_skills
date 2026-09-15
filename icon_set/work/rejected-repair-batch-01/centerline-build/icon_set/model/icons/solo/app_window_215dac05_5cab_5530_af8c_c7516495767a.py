"""App window (apps), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '215dac05-5cab-5530-af8c-c7516495767a'
SOURCE_PATH = 'pictographic-primitives/apps/app window_215dac05-5cab-5530-af8c-c7516495767a.svg'
AUTHOR = 'gpt-6'

class AppWindow(Solo48):
    icon_id = 'app-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('app', 'window', 'apps')

    def build(self):
        self.add_line('sym-e0', (42, 16), (6, 16))
        self.add_line('sym-e1', (6, 16), (6, 39))
        self.add_arc('sym-e2', (6, 39), (9, 42), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e4', (9, 42), (39, 42))
        self.add_arc('sym-e7', (39, 42), (42, 39), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e8', (42, 39), (42, 9))
        self.add_arc('sym-e11', (42, 9), (39, 6), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e13', (39, 6), (9, 6))
        self.add_arc('sym-e16', (9, 6), (6, 9), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('sym-e18', (6, 9), (6, 16))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e7', 'sym-e8', 'sym-e11', 'sym-e13', 'sym-e16', 'sym-e18', closed=False)
