"""Flag shape (design), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '741ea6f6-af2d-5573-98b8-3bfff729de4a'
SOURCE_PATH = 'icons-json/design/flag shape_741ea6f6-af2d-5573-98b8-3bfff729de4a.json'
AUTHOR = 'json_to_solo'

class FlagShape(Solo48):
    icon_id = 'flag-shape'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('flag', 'shape', 'design')

    def build(self):
        self.add_line('e0', (8, 8), (40, 8))
        self.add_line('e1', (40, 8), (34, 18))
        self.add_line('e2', (34, 18), (40, 27))
        self.add_line('e3', (40, 27), (8, 27))
        self.add_line('e4', (8, 4), (8, 44))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3')
        self.add_contour('c1', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
