"""Independent 32px profile of text-radon-chemical-symbol-65550daf.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '65550daf-4dd0-4b5a-999f-640ed02a8414'
SOURCE_PATH = 'icon_set/dist/text32/text-radon-chemical-symbol-65550daf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('65550daf-4dd0-4b5a-999f-640ed02a8414', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/rn (text u)_65550daf-4dd0-4b5a-999f-640ed02a8414.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-radon-chemical-symbol-65550daf',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = 'bb1e35c67468b15f0fa93626f6e4c36214e863db46dfe844e51d27c0d4d8c675'

class Drawing(TextSub32):
    icon_id = 'text-radon-chemical-symbol-65550daf-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 35
    text_ink_bounds = (0.0, 0.0, 35.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (33, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (33, 21), (33, 13))
        self.add_bezier('p2-r1-2', (33, 13), ((33, 10), (31, 8), (28, 8)))
        self.add_bezier('p2-r1-3', (28, 8), ((25, 8), (22, 10), (22, 13)))
        self.add_line('p2-r1-4', (22, 13), (22, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 2))
        self.add_bezier('p3-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p3-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p3-r1-5', (9, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (9, 12), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
