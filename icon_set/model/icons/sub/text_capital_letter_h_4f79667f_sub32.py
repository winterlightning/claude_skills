"""Independent 32px profile of text-capital-letter-h-4f79667f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '4f79667f-2c08-4b1a-9ba6-926c5e637a31'
SOURCE_PATH = 'icon_set/dist/text32/text-capital-letter-h-4f79667f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4f79667f-2c08-4b1a-9ba6-926c5e637a31', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/typeface/h_4f79667f-2c08-4b1a-9ba6-926c5e637a31.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-h-4f79667f', 'text/text-capital-letter-h-e84d2b2f')
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase',)
REFERENCE_EXPORT_SHA256 = '0e3d747e0de62aee4e60b049674c985caef8e9156ace28f561ad711b19451796'

class Drawing(TextSub32):
    icon_id = 'text-capital-letter-h-4f79667f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (2, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 2), (22, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 16), (22, 16))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
