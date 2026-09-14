"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6eeb8b64-353f-4d55-afc4-cee5edb7104e'
SOURCE_PATH = 'icons-json/smileys/drop_6eeb8b64-353f-4d55-afc4-cee5edb7104e.json'
AUTHOR = 'json_to_solo'

class Drop6eeb8b64(Solo48):
    icon_id = 'drop-6eeb8b64'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self):
        self.add_arc('e0', (24, 36), (31, 29), radius_x=8, sweep=False)
        self.add_arc('e1-1', (23, 5), (8, 29), radius_x=38, sweep=False)
        self.add_arc('e1-2', (8, 29), (16, 42), radius_x=15, sweep=False)
        self.add_line('e1-3', (16, 42), (24, 44))
        self.add_line('e1-4', (24, 44), (32, 42))
        self.add_arc('e1-5', (32, 42), (40, 29), radius_x=15, sweep=False)
        self.add_arc('e1-6', (40, 29), (24, 4), radius_x=41, sweep=False)
        self.add_line('e1-7', (24, 4), (23, 5))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', closed=True)
