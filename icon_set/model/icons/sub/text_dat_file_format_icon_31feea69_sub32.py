"""Independent 32px profile of text-dat-file-format-icon-31feea69.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '31feea69-61c1-4251-bf45-f3338a7ae5c0'
SOURCE_PATH = 'icon_set/dist/text32/text-dat-file-format-icon-31feea69.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('31feea69-61c1-4251-bf45-f3338a7ae5c0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dat (text)_31feea69-61c1-4251-bf45-f3338a7ae5c0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dat-file-format-icon-31feea69',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-a-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = 'd2c41fc36be82571c98ce3d364b9a9e1656ae0a6bfe993c92b7b3d6c833278ae'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-dat-file-format-icon-31feea69-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 66.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'DAT'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (8.88681, 2))
        self.add_bezier('p1-r1-2', (8.88681, 2), ((12.8153, 2), (16, 5.58172), (16, 10)))
        self.add_bezier('p1-r1-3', (16, 10), ((16, 14.4183), (12.8153, 18), (8.88681, 18)))
        self.add_line('p1-r1-4', (8.88681, 18), (4, 18))
        self.add_line('p1-r1-5', (4, 18), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (28, 18), ((28, 18), (29.26667, 2), (34.1333, 2)))
        self.add_bezier('p2-r1-2', (34.1333, 2), ((39, 2), (40, 18), (40, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p2-r2-1', (28.49782, 13.9921), (39.5709, 14.0032))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_line('p3-r1-1', (52, 2), (64, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (58, 18), (58.0064, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'path-3-1', 'path-4-1')
