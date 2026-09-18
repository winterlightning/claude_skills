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
TYPEFACE_GLYPH_IDS = ('letter-x', 'digit-4')
REFERENCE_EXPORT_SHA256 = 'a5139bab6eb6a2cbc8b1fbc9f783ec00cf6c324413571cb8aa0ba9181c98be5a'

class Drawing(TextSub32):
    icon_id = 'text-times-four-multiplier-2aa72adc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 53
    text_ink_bounds = (0.0, 0.0, 53.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (27, 20))
        self.add_bezier('p1-r1-2', (27, 20), ((27, 20), (27, 20), (28, 20)))
        self.add_line('p1-r1-3', (28, 20), (51, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (46, 2), (46, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 11), (19, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (19, 11))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
