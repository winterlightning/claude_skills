"""Independent 32px profile of text-sftp-protocol-text-958df5e6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '958df5e6-16e8-40f7-a1fd-1eaf93108784'
SOURCE_PATH = 'icon_set/dist/text32/text-sftp-protocol-text-958df5e6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('958df5e6-16e8-40f7-a1fd-1eaf93108784', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/sftp (text)_958df5e6-16e8-40f7-a1fd-1eaf93108784.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sftp-protocol-text-958df5e6',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-f-uppercase', 'letter-t-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '0f63afb6b11426688489083f8b2efe14b644ede380bcb406e03e87fd5bce337e'

class Drawing(TextSub32):
    icon_id = 'text-sftp-protocol-text-958df5e6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 104
    text_ink_bounds = (0.0, 0.0, 104.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (83, 30), (83, 2))
        self.add_line('p1-r1-2', (83, 2), (93, 2))
        self.add_bezier('p1-r1-3', (93, 2), ((99, 2), (102, 6), (102, 9)))
        self.add_bezier('p1-r1-4', (102, 9), ((102, 13), (99, 17), (93, 17)))
        self.add_line('p1-r1-5', (93, 17), (83, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (53, 2), (75, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (64, 2), (64, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (45, 2), (28, 2))
        self.add_line('p4-r1-2', (28, 2), (28, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (28, 16), (42, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p6-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p6-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p6-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p6-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p6-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p6-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', 'p6-r1-7', closed=False)
