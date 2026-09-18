"""Independent 32px profile of text-capital-letter-a-37012d29.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '37012d29-357d-4e7a-9788-4fe102b86097'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letter-a-37012d29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('37012d29-357d-4e7a-9788-4fe102b86097', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/a (text)_37012d29-357d-4e7a-9788-4fe102b86097.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-a-37012d29',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase',)
REFERENCE_EXPORT_SHA256 = '25cf18d5525249db4d9a534bc3a4c2b9ea361a1f824dc3d4b7245e14ba7d9ab6'

class Drawing(TextSub32):
    icon_id = 'text-capital-letter-a-37012d29-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 25
    text_ink_bounds = (0.0, 0.0, 25.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (11, 3))
        self.add_bezier('p1-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p1-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p1-r1-4', (14, 3), (23, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (6, 18), (19, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
