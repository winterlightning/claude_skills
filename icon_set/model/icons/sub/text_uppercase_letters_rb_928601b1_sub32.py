"""Independent 32px profile of text-uppercase-letters-rb-928601b1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '928601b1-cc6f-4c81-b977-ad0ce69dd337'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-letters-rb-928601b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('928601b1-cc6f-4c81-b977-ad0ce69dd337', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rb (text)_928601b1-cc6f-4c81-b977-ad0ce69dd337.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-letters-rb-928601b1',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-b-uppercase')
REFERENCE_EXPORT_SHA256 = 'bfdfcc93900607f5f78706c9664db1b4a12c987e757377af6e6ed60a5e9854d7'

class Drawing(TextSub32):
    icon_id = 'text-uppercase-letters-rb-928601b1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (30, 30), (30, 2))
        self.add_line('p1-r1-2', (30, 2), (39, 2))
        self.add_bezier('p1-r1-3', (39, 2), ((45, 2), (48, 6), (48, 9)))
        self.add_bezier('p1-r1-4', (48, 9), ((48, 13), (45, 16), (39, 16)))
        self.add_line('p1-r1-5', (39, 16), (30, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (39, 16), ((46, 16), (49, 20), (49, 23)))
        self.add_bezier('p2-r1-2', (49, 23), ((49, 26), (46, 30), (39, 30)))
        self.add_line('p2-r1-3', (39, 30), (30, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 2))
        self.add_bezier('p3-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p3-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p3-r1-5', (12, 17), (2, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (12, 17), (22, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-3')
        self.relate("connect", 'p1-r1-4', 'p2-r1-1')
        self.relate("connect", 'p1-r1-5', 'p2-r1-1')
        self.relate("connect", 'p3-r1-4', 'p4-r1-1')
        self.relate("connect", 'p3-r1-5', 'p4-r1-1')
