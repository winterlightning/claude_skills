"""Navigation top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e2', (28, 4), ((27.717, 4), (27.114, 4.009), (26.831, 4.009)), ((26.006, 4.009), (25.455, 4.591), (25, 5)))
        self.add_bezier('e3', (26, 13), ((26.8, 17.473), (27.975, 22.109), (28.062, 26.627)), ((28.209, 34.391), (27.286, 40.409), (15.766, 43.055)), ((14.252, 43.4), (12.702, 43.573), (11.151, 43.764)), ((10.658, 43.827), (10.129, 44), (9.625, 44)), ((9.083, 44), (8.542, 44), (8, 44)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3')
