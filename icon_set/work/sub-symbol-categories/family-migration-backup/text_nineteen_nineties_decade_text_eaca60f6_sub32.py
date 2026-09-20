"""Independent 32px profile of text-nineteen-nineties-decade-text-eaca60f6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'eaca60f6-1764-4315-b59f-730ecf0e7458'
SOURCE_PATH = 'icon_set/dist/text32/text-nineteen-nineties-decade-text-eaca60f6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('eaca60f6-1764-4315-b59f-730ecf0e7458', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/90s_eaca60f6-1764-4315-b59f-730ecf0e7458.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-nineteen-nineties-decade-text-eaca60f6',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-9', 'digit-0', 'letter-s')
REFERENCE_EXPORT_SHA256 = '45e3918608c8d2c9272343b551a72c503e480c53adb0217c59e9765631d5055a'

class Drawing(TextSub32):
    icon_id = 'text-nineteen-nineties-decade-text-eaca60f6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 72
    text_ink_bounds = (0.0, 0.0, 72.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (69, 13), ((69, 13), (69, 11), (63, 11)))
        self.add_bezier('p1-r1-2', (63, 11), ((60, 11), (57, 13), (57, 16)))
        self.add_bezier('p1-r1-3', (57, 16), ((57, 17), (58, 19), (60, 19)))
        self.add_bezier('p1-r1-4', (60, 19), ((65, 21), (64, 21), (68, 22)))
        self.add_bezier('p1-r1-5', (68, 22), ((69, 23), (70, 24), (70, 25)))
        self.add_bezier('p1-r1-6', (70, 25), ((70, 27), (68, 30), (63, 30)))
        self.add_bezier('p1-r1-7', (63, 30), ((57, 30), (57, 26), (57, 26)))
        self.add_bezier('p1-r1-8', (57, 26), ((57, 26), (57, 26), (57, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (29, 10), (49, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (49, 10), (49, 22))
        self.add_arc('p2-r1-3', (49, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (29, 22), (29, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_arc('p3-r1-1', (2, 10), (22, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (22, 10), (2, 10), radius_x=10, radius_y=8, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (22, 10), (22, 20))
        self.add_bezier('p4-r1-2', (22, 20), ((22, 26), (17, 30), (12, 30)))
        self.add_line('p4-r1-3', (12, 30), (5, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p3-r1-1', 'p4-r1-1')
        self.relate("connect", 'p3-r1-2', 'p4-r1-1')
