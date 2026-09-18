"""Independent 32px profile of text-capital-letter-e-cd794274.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'cd794274-bcc6-4483-b634-63126d777dd2'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letter-e-cd794274.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cd794274-bcc6-4483-b634-63126d777dd2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/E (text)_cd794274-bcc6-4483-b634-63126d777dd2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-e-cd794274',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase',)
REFERENCE_EXPORT_SHA256 = '03b188ab64e75904ee727f235c88fb4620c8c1c17a29ecb105278e0c7e39d427'

class Drawing(TextSub32):
    icon_id = 'text-capital-letter-e-cd794274-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 21
    text_ink_bounds = (0.0, 0.0, 21.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (19, 2), (2, 2))
        self.add_line('p1-r1-2', (2, 2), (2, 30))
        self.add_line('p1-r1-3', (2, 30), (19, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (2, 16), (16, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
