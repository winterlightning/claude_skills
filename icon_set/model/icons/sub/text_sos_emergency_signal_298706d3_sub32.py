"""Independent 32px profile of text-sos-emergency-signal-298706d3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '298706d3-05c2-49c9-816c-461ebbb76674'
SOURCE_PATH = 'icon_set/dist/text32/text-sos-emergency-signal-298706d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('298706d3-05c2-49c9-816c-461ebbb76674', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sos (text)_298706d3-05c2-49c9-816c-461ebbb76674.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sos-emergency-signal-298706d3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-o-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '948a59abb33d5b60e0761043edd7300e201a5d6411904fe24907887bb8910931'

class Drawing(TextSub32):
    icon_id = 'text-sos-emergency-signal-298706d3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 77
    text_ink_bounds = (0.0, 0.0, 77.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (74, 6), ((73, 3), (70, 2), (66, 2)))
        self.add_bezier('p1-r1-2', (66, 2), ((62, 2), (58, 4), (57, 9)))
        self.add_bezier('p1-r1-3', (57, 9), ((57, 9), (57, 9), (57, 10)))
        self.add_bezier('p1-r1-4', (57, 10), ((57, 17), (74, 13), (75, 22)))
        self.add_bezier('p1-r1-5', (75, 22), ((75, 22), (75, 22), (75, 23)))
        self.add_bezier('p1-r1-6', (75, 23), ((75, 28), (70, 30), (65, 30)))
        self.add_bezier('p1-r1-7', (65, 30), ((62, 30), (58, 29), (56, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_arc('p2-r1-1', (28, 16), (48, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (48, 16), (28, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p3-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p3-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p3-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p3-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p3-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p3-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
