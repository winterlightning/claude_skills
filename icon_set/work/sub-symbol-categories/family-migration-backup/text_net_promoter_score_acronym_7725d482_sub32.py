"""Independent 32px profile of text-net-promoter-score-acronym-7725d482.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '7725d482-4bd3-49b7-87ad-c65a70f09057'
SOURCE_PATH = 'icon_set/dist/text32/text-net-promoter-score-acronym-7725d482.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7725d482-4bd3-49b7-87ad-c65a70f09057', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/nps (text)_7725d482-4bd3-49b7-87ad-c65a70f09057.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-net-promoter-score-acronym-7725d482',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-p-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '91bd9814adf3077b2b8f16d4f5d5ffd062994f47cd4fb2199b5b9879d287b4fd'

class Drawing(TextSub32):
    icon_id = 'text-net-promoter-score-acronym-7725d482-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 78
    text_ink_bounds = (0.0, 0.0, 78.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (75, 6), ((74, 3), (71, 2), (67, 2)))
        self.add_bezier('p1-r1-2', (67, 2), ((63, 2), (59, 4), (58, 9)))
        self.add_bezier('p1-r1-3', (58, 9), ((58, 9), (58, 9), (58, 10)))
        self.add_bezier('p1-r1-4', (58, 10), ((58, 17), (75, 13), (76, 22)))
        self.add_bezier('p1-r1-5', (76, 22), ((76, 22), (76, 22), (76, 23)))
        self.add_bezier('p1-r1-6', (76, 23), ((76, 28), (71, 30), (66, 30)))
        self.add_bezier('p1-r1-7', (66, 30), ((63, 30), (59, 29), (57, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (30, 30), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (40, 2))
        self.add_bezier('p2-r1-3', (40, 2), ((46, 2), (50, 6), (50, 9)))
        self.add_bezier('p2-r1-4', (50, 9), ((50, 13), (46, 17), (40, 17)))
        self.add_line('p2-r1-5', (40, 17), (30, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (22, 30))
        self.add_line('p3-r1-3', (22, 30), (22, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
