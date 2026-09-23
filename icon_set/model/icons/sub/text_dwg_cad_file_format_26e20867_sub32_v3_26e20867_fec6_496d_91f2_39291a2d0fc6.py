"""Independent 32px profile of text-dwg-cad-file-format-26e20867.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '26e20867-fec6-496d-91f2-39291a2d0fc6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dwg (text)_26e20867-fec6-496d-91f2-39291a2d0fc6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('26e20867-fec6-496d-91f2-39291a2d0fc6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dwg (text)_26e20867-fec6-496d-91f2-39291a2d0fc6.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dwg-cad-file-format-26e20867',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '04e95afdc2e5b7af22d65df1e2229ad17bda8bb5cdb8fa98a77ae6b3f6ae7130'

TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-w-uppercase', 'letter-g-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant3(TextSub32):
    icon_id = 'text-dwg-cad-file-format-26e20867-sub32-v3'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 68.00000000000009, 20.0005)

    def build(self):
        """Source-native uppercase composition for 'DWG'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (8.88681, 2))
        self.add_bezier('p1-r1-2', (8.88681, 2), ((12.8153, 2), (16, 5.58172), (16, 10)))
        self.add_bezier('p1-r1-3', (16, 10), ((16, 14.4183), (12.8153, 18), (8.88681, 18)))
        self.add_line('p1-r1-4', (8.88681, 18), (4, 18))
        self.add_line('p1-r1-5', (4, 18), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (42.0005, 2.00052), (37.603300000000004, 18.0005))
        self.add_line('p2-r1-2', (37.603300000000004, 18.0005), (34.5005, 8.28623))
        self.add_line('p2-r1-3', (34.5005, 8.28623), (30.83221, 18.0005))
        self.add_line('p2-r1-4', (30.83221, 18.0005), (26.00049, 2.00052))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (62.8699, 3.51954), ((61.5334, 2.56364), (59.8896, 2), (58.1123, 2)))
        self.add_bezier('p3-r1-2', (58.1123, 2), ((53.63199, 2), (50, 5.58172), (50, 10)))
        self.add_bezier('p3-r1-3', (50, 10), ((50, 14.4183), (53.63199, 18), (58.1123, 18)))
        self.add_bezier('p3-r1-4', (58.1123, 18), ((62.373599999999996, 18), (65.6686, 14.5166), (66, 10.3983)))
        self.add_line('p3-r1-5', (66, 10.3983), (59.9716, 10.3983))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
