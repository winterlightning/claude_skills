"""Independent 32px profile of text-adobe-xd-logo-745c0a55.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '745c0a55-b6f3-45b5-8923-20698c6b86de'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-xd-logo-745c0a55.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('745c0a55-b6f3-45b5-8923-20698c6b86de', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/Xd_745c0a55-b6f3-45b5-8923-20698c6b86de.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-xd-logo-745c0a55',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = '765eb9bd6b54ea94f62323083c3396f408998cf98570bb4d857979b02ced9558'

class Drawing(TextSub32):
    icon_id = 'text-adobe-xd-logo-745c0a55-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 50
    text_ink_bounds = (0.0, 0.0, 50.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (48, 25), ((46, 28), (43, 30), (40, 30)))
        self.add_bezier('p1-r1-2', (40, 30), ((34, 30), (30, 26), (30, 20)))
        self.add_bezier('p1-r1-3', (30, 20), ((30, 15), (34, 11), (40, 11)))
        self.add_bezier('p1-r1-4', (40, 11), ((43, 11), (46, 12), (48, 15)))
        self.add_bezier('p1-r1-5', (48, 15), ((48, 15), (48, 16), (48, 16)))
        self.add_line('p1-r1-6', (48, 16), (48, 25))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (48, 16), (48, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 2), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 2), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p1-r1-5', 'p2-r1-1')
        self.relate('connect', 'p1-r1-6', 'p2-r1-1')
