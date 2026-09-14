"""T (typeface), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcbbdb66-24b8-46f2-a2b9-bc31ed68c218'
SOURCE_PATH = 'icons-json/typeface/t_fcbbdb66-24b8-46f2-a2b9-bc31ed68c218.json'
AUTHOR = 'json_to_solo'

class T(Solo48):
    icon_id = 't'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('t', 'typeface')

    def build(self):
        self.add_line('e0', (21, 4), (21, 34))
        self.add_line('e1', (8, 16), (34, 16))
        self.add_bezier('e2', (21, 34), ((21, 37.364), (22.24, 41.4), (27.744, 43.282)), ((28.704, 43.618), (30.08, 44), (31.248, 44)), ((33.168, 44), (35.088, 44), (37.008, 44)), ((37.728, 44), (38.448, 44), (39.168, 44)), ((39.44, 44), (39.984, 43.845), (39.984, 44)), ((39.984, 44), (40, 44), (40, 44)))
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e1')
