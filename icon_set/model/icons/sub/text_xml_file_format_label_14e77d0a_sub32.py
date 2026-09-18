"""Independent 32px profile of text-xml-file-format-label-14e77d0a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '14e77d0a-f38d-4468-8003-3403c3e8269c'
SOURCE_PATH = 'icon_set/dist/text32/text-xml-file-format-label-14e77d0a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14e77d0a-f38d-4468-8003-3403c3e8269c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/xml (text)_14e77d0a-f38d-4468-8003-3403c3e8269c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-xml-file-format-label-14e77d0a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-m-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = '9069c9a0be00054f0eae3c807f669f6e29eedd81e819a84d97e9dfaed5418e5e'

class Drawing(TextSub32):
    icon_id = 'text-xml-file-format-label-14e77d0a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 83
    text_ink_bounds = (0.0, 0.0, 83.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (64, 2), (64, 30))
        self.add_line('p1-r1-2', (64, 30), (81, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (30, 30), (30, 2))
        self.add_line('p2-r1-2', (30, 2), (43, 20))
        self.add_line('p2-r1-3', (43, 20), (57, 2))
        self.add_line('p2-r1-4', (57, 2), (57, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 2), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
