"""Classical piano (music), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a53bd27a-5806-5a97-81ac-1e6b26e8a953'
SOURCE_PATH = 'icons-json/music/classical piano_a53bd27a-5806-5a97-81ac-1e6b26e8a953.json'
AUTHOR = 'json_to_solo'

class ClassicalPiano(Solo48):
    icon_id = 'classical-piano'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'music'
    aliases = ()
    keywords = ('classical', 'piano', 'music')

    def build(self):
        self.add_line('e0', (42, 23), (10, 23))
        self.add_line('e1', (6, 32), (6, 35))
        self.add_line('e2', (6, 35), (42, 35))
        self.add_line('e3', (42, 35), (42, 24))
        self.add_line('e4', (20, 6), (15, 6))
        self.add_line('e5', (12, 9), (12, 23))
        self.add_line('e6', (12, 42), (12, 35))
        self.add_line('e7', (36, 35), (36, 42))
        self.add_arc('e8-1', (10, 23), (9, 27), radius_x=4, sweep=False)
        self.add_line('e8-2', (9, 27), (6, 32))
        self.add_line('e9-1', (42, 24), (42, 20))
        self.add_arc('e9-2', (42, 20), (39, 16), radius_x=6, sweep=False)
        self.add_line('e9-3', (39, 16), (31, 15))
        self.add_arc('e9-4', (31, 15), (23, 7), radius_x=15)
        self.add_arc('e9-5', (23, 7), (20, 6), radius_x=8, sweep=False)
        self.add_arc('e10', (15, 6), (12, 9), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1', 'e2', 'e3', 'e9-1', 'e9-2', 'e9-3', 'e9-4', 'e9-5', 'e4', 'e10', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
