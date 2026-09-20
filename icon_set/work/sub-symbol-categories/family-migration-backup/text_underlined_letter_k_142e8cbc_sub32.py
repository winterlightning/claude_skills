"""Independent 32px profile of text-underlined-letter-k-142e8cbc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '142e8cbc-226e-43cc-ba88-44eae89e8efa'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-k-142e8cbc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('142e8cbc-226e-43cc-ba88-44eae89e8efa', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/k (text u)_142e8cbc-226e-43cc-ba88-44eae89e8efa.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-k-142e8cbc',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase',)
REFERENCE_EXPORT_SHA256 = '1dc4a755c6ec9a4f85c9c223b5847f9b3c85e7cba731dfafc1a4b8e820eda5bd'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-k-142e8cbc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 17
    text_ink_bounds = (0.0, 0.0, 17.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (15, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (15, 2), (2, 12))
        self.add_line('p3-r1-2', (2, 12), (15, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
