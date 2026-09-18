"""Independent 32px profile of text-flv-video-file-format-e3a73450.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'e3a73450-19cc-4412-8089-8b72325dc6cb'
SOURCE_PATH = 'icon_set/dist/text32/text-flv-video-file-format-e3a73450.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3a73450-19cc-4412-8089-8b72325dc6cb', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/flv (text)_e3a73450-19cc-4412-8089-8b72325dc6cb.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-flv-video-file-format-e3a73450',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-l-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = '8b329b99f5d5c777967a665dca5e754da1c8060940178d80f98888d6170bbf61'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-flv-video-file-format-e3a73450-sub32-symbol'
    related_origin_icon_id = 'text-flv-video-file-format-e3a73450-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-flv-video-file-format-e3a73450-sub32'
    counterpart_icon_id = 'text-flv-video-file-format-e3a73450-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 74
    text_ink_bounds = (0.0, 0.0, 74.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (51, 2), (60, 28))
        self.add_bezier('p1-r1-2', (60, 28), ((60.666666666666664, 29.333333333333332), (61.333333333333336, 30), (62, 30)))
        self.add_bezier('p1-r1-3', (62, 30), ((62, 30), (62.333333333333336, 29.333333333333332), (63, 28)))
        self.add_line('p1-r1-4', (63, 28), (72, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (27, 2), (27, 30))
        self.add_line('p2-r1-2', (27, 30), (43, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (19, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 16), (16, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
