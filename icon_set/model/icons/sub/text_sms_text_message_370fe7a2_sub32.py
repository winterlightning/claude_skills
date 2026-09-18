"""Independent 32px profile of text-sms-text-message-370fe7a2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '370fe7a2-da11-4788-b651-2af6aeacb600'
SOURCE_PATH = 'icon_set/dist/text32/text-sms-text-message-370fe7a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('370fe7a2-da11-4788-b651-2af6aeacb600', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/sms (text)_370fe7a2-da11-4788-b651-2af6aeacb600.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sms-text-message-370fe7a2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-m-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '33d957ee96382b47aaecb1149fd27a8fe0e28eea9c806f037283809e29570b1b'

class Drawing(TextSub32):
    icon_id = 'text-sms-text-message-370fe7a2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 83
    text_ink_bounds = (0.0, 0.0, 83.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (80, 6), ((79, 3), (76, 2), (72, 2)))
        self.add_bezier('p1-r1-2', (72, 2), ((68, 2), (64, 4), (63, 9)))
        self.add_bezier('p1-r1-3', (63, 9), ((63, 9), (63, 9), (63, 10)))
        self.add_bezier('p1-r1-4', (63, 10), ((63, 17), (80, 13), (81, 22)))
        self.add_bezier('p1-r1-5', (81, 22), ((81, 22), (81, 22), (81, 23)))
        self.add_bezier('p1-r1-6', (81, 23), ((81, 28), (76, 30), (72, 30)))
        self.add_bezier('p1-r1-7', (72, 30), ((68, 30), (64, 29), (63, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (28, 30), (28, 2))
        self.add_line('p2-r1-2', (28, 2), (41, 20))
        self.add_line('p2-r1-3', (41, 20), (55, 2))
        self.add_line('p2-r1-4', (55, 2), (55, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p3-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p3-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p3-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p3-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p3-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p3-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
