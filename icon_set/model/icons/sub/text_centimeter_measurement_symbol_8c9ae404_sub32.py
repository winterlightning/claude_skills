"""Independent 32px profile of text-centimeter-measurement-symbol-8c9ae404.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '8c9ae404-2f38-4d2f-996b-7c8e6495bc2b'
SOURCE_PATH = 'icon_set/dist/text32/text-centimeter-measurement-symbol-8c9ae404.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8c9ae404-2f38-4d2f-996b-7c8e6495bc2b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cm (text u)_8c9ae404-2f38-4d2f-996b-7c8e6495bc2b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-centimeter-measurement-symbol-8c9ae404',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = '684bfa901e4ece1d4263b5627d1386cb6a5131c223e2b58d42c5e93c1d4a152f'

class Drawing(TextSub32):
    icon_id = 'text-centimeter-measurement-symbol-8c9ae404-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 57
    text_ink_bounds = (0.001457877762348403, 0.0, 57.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (41, 18), (41, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (27, 30), (27, 18))
        self.add_bezier('p2-r1-2', (27, 18), ((27, 14), (30, 11), (34, 11)))
        self.add_bezier('p2-r1-3', (34, 11), ((38, 11), (41, 14), (41, 18)))
        self.add_bezier('p2-r1-4', (41, 18), ((41, 14), (44, 11), (48, 11)))
        self.add_bezier('p2-r1-5', (48, 11), ((52, 11), (55, 14), (55, 18)))
        self.add_line('p2-r1-6', (55, 18), (55, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_arc('p3-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-1', 'p2-r1-4')
