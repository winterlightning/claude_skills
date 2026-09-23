"""Independent 32px profile of text-xls-spreadsheet-file-format-537c3e64.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '537c3e64-2125-4115-80ac-862f539aecc8'
SOURCE_PATH = 'icon_set/dist/text32/text-xls-spreadsheet-file-format-537c3e64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('537c3e64-2125-4115-80ac-862f539aecc8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/xls (text)_537c3e64-2125-4115-80ac-862f539aecc8.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-xls-spreadsheet-file-format-537c3e64',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-l-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '6c33c74233526c8f6e9b72d866a79817b3966836a1816d79632e6f2f1effe7ad'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-xls-spreadsheet-file-format-537c3e64-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (1.0, 0.0, 66.0000075398524, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'XLS'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (3, 2.00003), (17, 17.9909))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (3.02295, 18), (16.9638, 2.04587))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_bezier('p3-r1-1', (39, 18), ((35.9428, 18), (28.23973, 18), (28, 18)))
        self.add_line('p3-r1-2', (28, 18), (28, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (63.9314, 2), (56.77906, 2))
        self.add_bezier('p4-r1-2', (56.77906, 2), ((51.70172, 2), (50.21029, 7.42857), (54.98284, 9.42857)))
        self.add_line('p4-r1-3', (54.98284, 9.42857), (61.4623, 11.608))
        self.add_bezier('p4-r1-4', (61.4623, 11.608), ((65.7211, 13.4286), (64.2526, 18), (59.7787, 18)))
        self.add_line('p4-r1-5', (59.7787, 18), (52, 18))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
