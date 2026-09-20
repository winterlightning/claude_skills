"""Independent 32px profile of text-kilocalorie-energy-unit-text-ffea3de8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'ffea3de8-601b-4157-a4fc-b03f13dd98ff'
SOURCE_PATH = 'icon_set/dist/text32/text-kilocalorie-energy-unit-text-ffea3de8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ffea3de8-601b-4157-a4fc-b03f13dd98ff', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/kcal (text)_ffea3de8-601b-4157-a4fc-b03f13dd98ff.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-kilocalorie-energy-unit-text-ffea3de8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase', 'letter-c-uppercase', 'letter-a-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = 'fe26f17ab6394132b155f2a72835fcabe9ad0b3c7deee2254f86109a2f3a94e2'

class Drawing(TextSub32):
    icon_id = 'text-kilocalorie-energy-unit-text-ffea3de8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 101
    text_ink_bounds = (0.0, 0.0, 101.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (83, 2), (83, 30))
        self.add_line('p1-r1-2', (83, 30), (99, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (54, 30), (64, 3))
        self.add_bezier('p2-r1-2', (64, 3), ((64, 2.3333333333333335), (64.33333333333333, 2), (65, 2)))
        self.add_bezier('p2-r1-3', (65, 2), ((65, 2), (65.33333333333333, 2.3333333333333335), (66, 3)))
        self.add_line('p2-r1-4', (66, 3), (75, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (59, 18), (71, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_arc('p4-r1-1', (47, 6), (47, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (2, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (21, 2), (2, 17))
        self.add_line('p6-r1-2', (2, 17), (21, 30))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', closed=False)
