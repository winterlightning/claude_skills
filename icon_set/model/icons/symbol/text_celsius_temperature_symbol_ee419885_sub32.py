"""Independent 32px profile of text-celsius-temperature-symbol-ee419885.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'ee419885-8649-4759-9a58-8b2f5faaccd2'
SOURCE_PATH = 'icon_set/dist/text32/text-celsius-temperature-symbol-ee419885.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee419885-8649-4759-9a58-8b2f5faaccd2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/celsius_ee419885-8649-4759-9a58-8b2f5faaccd2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-celsius-temperature-symbol-ee419885', 'text/text-uppercase-alphabet-letter-c-f64636e2')
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase',)
REFERENCE_EXPORT_SHA256 = 'd8d10689706f84cd7231fe4eb72c251e5c40f106424e2cb5842eb20a9fc849b5'

class Drawing(TextSub32):
    icon_id = 'text-celsius-temperature-symbol-ee419885-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 21
    text_ink_bounds = (0.001457877762348403, 0.0, 21.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
