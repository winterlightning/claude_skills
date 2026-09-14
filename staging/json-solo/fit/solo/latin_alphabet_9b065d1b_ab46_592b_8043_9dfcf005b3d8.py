"""Latin alphabet (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b065d1b-ab46-592b-8043-9dfcf005b3d8'
SOURCE_PATH = 'icons-json/interface-essential/latin alphabet_9b065d1b-ab46-592b-8043-9dfcf005b3d8.json'
AUTHOR = 'json_to_solo'

class LatinAlphabetInterfaceEssential(Solo48):
    icon_id = 'latin-alphabet-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('latin', 'alphabet', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 39), (40, 24))
        self.add_line('e1', (40, 24), (30, 24))
        self.add_arc('e2-1', (36, 7), (26, 4), radius_x=19, sweep=False)
        self.add_line('e2-2', (26, 4), (20, 5))
        self.add_arc('e2-3', (20, 5), (10, 14), radius_x=19, sweep=False)
        self.add_line('e2-4', (10, 14), (8, 24))
        self.add_line('e2-5', (8, 24), (10, 34))
        self.add_arc('e2-6', (10, 34), (26, 44), radius_x=18, sweep=False)
        self.add_arc('e2-7', (26, 44), (36, 42), radius_x=27, sweep=False)
        self.add_arc('e2-8', (36, 42), (40, 39), radius_x=4, sweep=False)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e0', 'e1')
