"""Independent 32px profile of text-tiff-image-file-format-02af3840.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '02af3840-b8eb-40f6-b3ef-54661616285b'
SOURCE_PATH = 'icon_set/dist/text32/text-tiff-image-file-format-02af3840.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('02af3840-b8eb-40f6-b3ef-54661616285b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/TIFF (text)_02af3840-b8eb-40f6-b3ef-54661616285b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-tiff-image-file-format-02af3840',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-i-uppercase', 'letter-f-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'af0ba5f9d79256b8c42f88164cd6e0a4b9830640bc31955095a1c6aefae94b49'

class Drawing(TextSub32):
    icon_id = 'text-tiff-image-file-format-02af3840-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 93
    text_ink_bounds = (0.0, 0.0, 93.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (91, 2), (74, 2))
        self.add_line('p1-r1-2', (74, 2), (74, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (74, 16), (88, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (66, 2), (49, 2))
        self.add_line('p3-r1-2', (49, 2), (49, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (49, 16), (63, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (32, 2), (41, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (36, 2), (36, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (32, 30), (41, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.add_line('p8-r1-1', (2, 2), (24, 2))
        self.add_contour('path-8-1', 'p8-r1-1', closed=False)
        self.add_line('p9-r1-1', (13, 2), (13, 30))
        self.add_contour('path-9-1', 'p9-r1-1', closed=False)
