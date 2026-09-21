"""T (typeface), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcbbdb66-24b8-46f2-a2b9-bc31ed68c218'
SOURCE_PATH = 'icons-json/typeface/t_fcbbdb66-24b8-46f2-a2b9-bc31ed68c218.json'
AUTHOR = 'json_to_solo'

class TFcbbdb66(Solo48):
    icon_id = 't-fcbbdb66'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'typeface'
    aliases = ()
    keywords = ('t', 'typeface')

    def build(self):
        self.add_line('e0', (21, 4), (21, 34))
        self.add_line('e1', (8, 16), (34, 16))
        self.add_arc('e2-1', (21, 34), (25, 42), radius_x=9, sweep=False)
        self.add_arc('e2-2', (25, 42), (30, 44), radius_x=15, sweep=False)
        self.add_line('e2-3', (30, 44), (34, 44))
        self.add_line('e2-4', (34, 44), (40, 44))
        self.add_contour('c0', 'e0', 'e2-1', 'e2-2', 'e2-3', 'e2-4')
        self.add_contour('c1', 'e1')
