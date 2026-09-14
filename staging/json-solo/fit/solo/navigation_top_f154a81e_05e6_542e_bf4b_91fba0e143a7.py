"""Navigation top (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f154a81e-05e6-542e-bf4b-91fba0e143a7'
SOURCE_PATH = 'icons-json/arrows/navigation top_f154a81e-05e6-542e-bf4b-91fba0e143a7.json'
AUTHOR = 'json_to_solo'

class NavigationTopArrows(Solo48):
    icon_id = 'navigation-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('navigation', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (40, 14), (28, 4))
        self.add_line('e1', (25, 5), (14, 14))
        self.add_line('e2', (28, 4), (25, 5))
        self.add_arc('e3-1', (26, 13), (28, 30), radius_x=74)
        self.add_arc('e3-2', (28, 30), (23, 40), radius_x=11)
        self.add_arc('e3-3', (23, 40), (9, 44), radius_x=33)
        self.add_arc('e3-4', (9, 44), (8, 44), radius_x=23, sweep=False)
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4')
