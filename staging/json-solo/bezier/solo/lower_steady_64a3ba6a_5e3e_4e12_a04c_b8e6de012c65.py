"""Lower steady (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64a3ba6a-5e3e-4e12-a04c-b8e6de012c65'
SOURCE_PATH = 'icons-json/arrows/lower steady_64a3ba6a-5e3e-4e12-a04c-b8e6de012c65.json'
AUTHOR = 'json_to_solo'

class LowerSteadyArrows(Solo48):
    icon_id = 'lower-steady-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('lower', 'steady', 'arrows')

    def build(self):
        self.add_line('e0', (6, 6), (6, 36))
        self.add_line('e1', (20, 36), (20, 26))
        self.add_line('e2', (25, 21), (42, 21))
        self.add_line('e3', (37, 26), (42, 21))
        self.add_line('e4', (37, 17), (42, 21))
        self.add_bezier('e5', (6, 36), ((6, 36.376), (6.18, 37.099), (6.311, 37.451)), ((7.219, 39.848), (9.805, 41.984), (12.48, 41.984)), ((12.611, 41.984), (12.734, 42), (12.865, 42)), ((12.867, 42), (12.87, 42), (12.872, 42)), ((13.033, 42), (13.186, 41.992), (13.347, 41.992)), ((16.105, 41.992), (18.747, 39.725), (19.606, 37.214)), ((19.664, 37.05), (20, 36.115), (20, 36)))
        self.add_bezier('e6', (20, 26), ((20, 25.763), (20.146, 24.884), (20.236, 24.622)), ((20.875, 22.707), (22.824, 21), (25, 21)))
        self.add_contour('c0', 'e0', 'e5', 'e1', 'e6', 'e2')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
