"""Classical piano (music), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a53bd27a-5806-5a97-81ac-1e6b26e8a953'
SOURCE_PATH = 'icons-json/music/classical piano_a53bd27a-5806-5a97-81ac-1e6b26e8a953.json'
AUTHOR = 'json_to_solo'

class ClassicalPianoMusic(Solo48):
    icon_id = 'classical-piano-music'
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
        self.add_bezier('e8', (10, 23), ((9.755, 23.205), (9.494, 23.591), (9.305, 23.861)), ((8.315, 25.293), (9.248, 27.592), (8.397, 29.056)), ((7.743, 30.185), (6.008, 30.455), (6.008, 31.945)), ((6.008, 32.026), (6, 31.918), (6, 32)))
        self.add_bezier('e9', (42, 24), ((42, 23.73), (42, 23.452), (42, 23.182)), ((42, 22.945), (41.992, 22.715), (41.992, 22.478)), ((41.992, 21.496), (42, 20.343), (41.779, 19.377)), ((41.509, 18.461), (40.961, 17.675), (40.29, 17.013)), ((37.025, 13.781), (32.133, 16.743), (28.664, 13.985)), ((25.808, 11.711), (24.941, 7.219), (21.087, 6.237)), ((20.703, 6.139), (20.401, 6), (20, 6)))
        self.add_bezier('e10', (15, 6), ((14.91, 6), (14.828, 6), (14.738, 6)), ((13.069, 6), (12, 7.413), (12, 9)))
        self.add_contour('c0', 'e0', 'e8', 'e1', 'e2', 'e3', 'e9', 'e4', 'e10', 'e5')
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c0')
