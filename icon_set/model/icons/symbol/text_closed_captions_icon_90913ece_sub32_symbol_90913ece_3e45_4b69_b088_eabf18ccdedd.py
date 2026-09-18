"""Independent 32px profile of text-closed-captions-icon-90913ece.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '90913ece-3e45-4b69-b088-eabf18ccdedd'
SOURCE_PATH = 'icon_set/dist/text32/text-closed-captions-icon-90913ece.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('90913ece-3e45-4b69-b088-eabf18ccdedd', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/CC (text)_90913ece-3e45-4b69-b088-eabf18ccdedd.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-closed-captions-icon-90913ece',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-c-uppercase')
REFERENCE_EXPORT_SHA256 = 'd5c06a774548f8e70b46e2a2c7ff4919f2a93cfb8ff8f020c692bb5da22fc2ae'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-closed-captions-icon-90913ece-sub32-symbol'
    related_origin_icon_id = 'text-closed-captions-icon-90913ece-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-closed-captions-icon-90913ece-sub32'
    counterpart_icon_id = 'text-closed-captions-icon-90913ece-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 46
    text_ink_bounds = (0.001457877762348403, 0.0, 46.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (44, 6), (44, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
