"""Independent 32px profile of text-advertisement-text-symbol-46927056.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '46927056-6b93-47f9-8be7-c7d7312f7f7a'
SOURCE_PATH = 'icon_set/dist/text32/text-advertisement-text-symbol-46927056.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('46927056-6b93-47f9-8be7-c7d7312f7f7a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/AD (text)_46927056-6b93-47f9-8be7-c7d7312f7f7a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-advertisement-text-symbol-46927056',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '1b6b1fd0ba09ac106f8177f9df2ba5ee86a07b4063ad3cca943dd72f93c0a8ab'

class Drawing(TextSub32):
    icon_id = 'text-advertisement-text-symbol-46927056-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 52
    text_ink_bounds = (0.0, 0.0, 52.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (31, 2), (39, 2))
        self.add_bezier('p1-r1-2', (39, 2), ((46, 2), (50, 9), (50, 16)))
        self.add_bezier('p1-r1-3', (50, 16), ((50, 23), (46, 30), (39, 30)))
        self.add_line('p1-r1-4', (39, 30), (31, 30))
        self.add_line('p1-r1-5', (31, 30), (31, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 30), (11, 3))
        self.add_bezier('p2-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p2-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p2-r1-4', (14, 3), (23, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (6, 18), (19, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
