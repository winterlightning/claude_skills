"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3057870d-1409-44b0-8369-04ad03f65bba'
SOURCE_PATH = 'icons-json/smileys/drop_3057870d-1409-44b0-8369-04ad03f65bba.json'
AUTHOR = 'json_to_solo'

class Drop3057870d(Solo48):
    icon_id = 'drop-3057870d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('drop', 'smileys')

    def build(self):
        self.add_line('e0', (26, 6), (24, 4))
        self.add_arc('e1-1', (24, 4), (8, 28), radius_x=46, sweep=False)
        self.add_arc('e1-2', (8, 28), (24, 44), radius_x=16, sweep=False)
        self.add_line('e1-3', (24, 44), (32, 42))
        self.add_arc('e1-4', (32, 42), (40, 29), radius_x=15, sweep=False)
        self.add_arc('e1-5', (40, 29), (26, 6), radius_x=40, sweep=False)
        self.add_contour('c0', 'e0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', closed=True)
