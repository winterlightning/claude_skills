"""Independent 32px profile of text-promethium-chemical-element-symbol-a08b93a3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a08b93a3-444d-4398-ae9a-caa1969b7b40'
SOURCE_PATH = 'icon_set/dist/text32/text-promethium-chemical-element-symbol-a08b93a3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a08b93a3-444d-4398-ae9a-caa1969b7b40', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/pm (text u)_a08b93a3-444d-4398-ae9a-caa1969b7b40.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-promethium-chemical-element-symbol-a08b93a3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = '84afd80c2fd93542d3a1826cfbdf4faacf492dc1b9cce3a8f99cbc93e9241c2a'

class Drawing(TextSub32):
    icon_id = 'text-promethium-chemical-element-symbol-a08b93a3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 43
    text_ink_bounds = (0.0, 0.0, 43.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (41, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (31, 13), (31, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 21), (22, 13))
        self.add_bezier('p3-r1-2', (22, 13), ((22, 10), (24, 8), (27, 8)))
        self.add_bezier('p3-r1-3', (27, 8), ((29, 8), (31, 10), (31, 13)))
        self.add_bezier('p3-r1-4', (31, 13), ((31, 10), (34, 8), (36, 8)))
        self.add_bezier('p3-r1-5', (36, 8), ((39, 8), (41, 10), (41, 13)))
        self.add_line('p3-r1-6', (41, 13), (41, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-1', 'p3-r1-4')
