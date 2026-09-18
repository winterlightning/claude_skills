"""Independent 32px profile of text-gif-file-format-icon-3d3b075e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '3d3b075e-c8d1-4ff5-82d7-2b5904b06c7d'
SOURCE_PATH = 'icon_set/dist/text32/text-gif-file-format-icon-3d3b075e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d3b075e-c8d1-4ff5-82d7-2b5904b06c7d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/gif (text)_3d3b075e-c8d1-4ff5-82d7-2b5904b06c7d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-gif-file-format-icon-3d3b075e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-i-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'eccc894f9f66c7b38cbdad8993491e94f30ca4890b1cb0183a63f7070b56c38f'

class Drawing(TextSub32):
    icon_id = 'text-gif-file-format-icon-3d3b075e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 66
    text_ink_bounds = (0.0, 0.0, 66.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (64, 2), (47, 2))
        self.add_line('p1-r1-2', (47, 2), (47, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (47, 16), (61, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (30, 2), (39, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (35, 2), (35, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (30, 30), (39, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (19, 6), ((17, 4), (15, 2), (13, 2)))
        self.add_bezier('p6-r1-2', (13, 2), ((7, 2), (2, 9), (2, 17)))
        self.add_bezier('p6-r1-3', (2, 17), ((2, 18), (2, 20), (3, 21)))
        self.add_bezier('p6-r1-4', (3, 21), ((4, 27), (8, 29), (12, 29)))
        self.add_bezier('p6-r1-5', (12, 29), ((17, 29), (22, 24), (22, 16)))
        self.add_line('p6-r1-6', (22, 16), (14, 16))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', closed=False)
