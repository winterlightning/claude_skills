'An ear is drawn in profile with a curled inner fold and a rounded lower lobe. Two nested sound arcs sit beyond the upper-right edge of the ear.\n\nConstruction: Ear with two detached sound waves at its upper-right. Inner-ear detail omitted to keep the waves separated. Bounds (6,6)-(42,42).\nLucide: ear: continuous ear bowl and lobule.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2002b214-1c74-402f-b75c-79645c2d7522'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability hearing_2002b214-1c74-402f-b75c-79645c2d7522.svg'
AUTHOR = 'gpt-6'

class EarWithSoundWaves(Solo48):
    icon_id = 'ear-with-sound-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'audio', 'listening', 'accessibility')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('ear-top', (6, 26), (22, 26), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('ear-down', (22, 26), (18, 36), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('ear-lobe', (18, 36), (6, 36), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wave-inner', (29, 15), (33, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('wave-outer', (29, 6), (42, 19), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('ear', 'ear-top', 'ear-down', 'ear-lobe', closed=False)
