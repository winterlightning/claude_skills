"""Independent 32px profile of text-times-four-multiplier-2aa72adc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2aa72adc-73bd-4dc7-9a10-98093ab16af8'
SOURCE_PATH = 'icon_set/dist/text32/text-times-four-multiplier-2aa72adc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2aa72adc-73bd-4dc7-9a10-98093ab16af8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/x4 (text)_2aa72adc-73bd-4dc7-9a10-98093ab16af8.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-times-four-multiplier-2aa72adc',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'digit-4')
REFERENCE_EXPORT_SHA256 = 'a5139bab6eb6a2cbc8b1fbc9f783ec00cf6c324413571cb8aa0ba9181c98be5a'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-times-four-multiplier-2aa72adc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (1.0, 3.0000000000196536e-05, 42.0, 20.0001)

    def build(self):
        """Source-native uppercase composition for 'X4'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (3, 2.00003), (17, 17.9909))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (3.02295, 18), (16.9638, 2.04587))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (40, 12.8572), (28.40861, 12.8572))
        self.add_bezier('p3-r1-2', (28.40861, 12.8572), ((28.18045, 12.8572), (27.81423, 12.5715), (28.11142, 12.2858)))
        self.add_line('p3-r1-3', (28.11142, 12.2858), (37.622299999999996, 2.00009))
        self.add_line('p3-r1-4', (37.622299999999996, 2.00009), (37.622299999999996, 18.0001))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
