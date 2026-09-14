"""Drop (smileys), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b'
SOURCE_PATH = 'icons-json/smileys/drop_a1bd3645-c186-44d1-a3a2-2ec8e3d10a1b.json'
AUTHOR = 'json_to_solo'

class DropA1bd3645(Solo48):
    icon_id = 'drop-a1bd3645'
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
