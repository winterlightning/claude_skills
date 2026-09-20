"""Independent 32px profile of text-lb-weight-symbol-44b2a4ad.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '44b2a4ad-3075-45bc-ae41-282c60bd7d93'
SOURCE_PATH = 'icon_set/dist/text32/text-lb-weight-symbol-44b2a4ad.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('44b2a4ad-3075-45bc-ae41-282c60bd7d93', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/LB (text)_44b2a4ad-3075-45bc-ae41-282c60bd7d93.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-lb-weight-symbol-44b2a4ad',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-b-uppercase')
REFERENCE_EXPORT_SHA256 = '4d5df57b3411cf5aa5d0b1525649edaf48f43f0b4c5c2ef0e98f75576c9e501a'

class Drawing(TextSub32):
    icon_id = 'text-lb-weight-symbol-44b2a4ad-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 47
    text_ink_bounds = (0.0, 0.0, 47.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (26, 30), (26, 2))
        self.add_line('p1-r1-2', (26, 2), (36, 2))
        self.add_bezier('p1-r1-3', (36, 2), ((41, 2), (44, 6), (44, 9)))
        self.add_bezier('p1-r1-4', (44, 9), ((44, 13), (41, 16), (36, 16)))
        self.add_line('p1-r1-5', (36, 16), (26, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (36, 16), ((42, 16), (45, 20), (45, 23)))
        self.add_bezier('p2-r1-2', (45, 23), ((45, 26), (42, 30), (36, 30)))
        self.add_line('p2-r1-3', (36, 30), (26, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (2, 2), (2, 30))
        self.add_line('p3-r1-2', (2, 30), (18, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
