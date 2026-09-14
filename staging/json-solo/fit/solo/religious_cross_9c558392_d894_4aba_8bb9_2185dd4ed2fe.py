"""Religious cross (religion), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c558392-d894-4aba-8bb9-2185dd4ed2fe'
SOURCE_PATH = 'icons-json/religion/religious cross_9c558392-d894-4aba-8bb9-2185dd4ed2fe.json'
AUTHOR = 'json_to_solo'

class ReligiousCrossReligion(Solo48):
    icon_id = 'religious-cross-religion'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'religion'
    aliases = ()
    keywords = ('religious', 'cross', 'religion')

    def build(self):
        self.add_line('e0', (29, 4), (19, 4))
        self.add_line('e1', (19, 4), (19, 15))
        self.add_line('e2', (19, 15), (8, 15))
        self.add_line('e3', (8, 15), (8, 25))
        self.add_line('e4', (8, 25), (19, 25))
        self.add_line('e5', (19, 25), (19, 44))
        self.add_line('e6', (19, 44), (29, 44))
        self.add_line('e7', (29, 44), (29, 25))
        self.add_line('e8', (29, 25), (40, 25))
        self.add_line('e9', (40, 25), (40, 15))
        self.add_line('e10', (40, 15), (29, 15))
        self.add_line('e11', (29, 15), (29, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', closed=True)
