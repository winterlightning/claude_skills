"""Independent 32px profile of circular-question-mark-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c356687a-8779-4296-879a-5477d3e84e2f'
SOURCE_PATH = 'pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c356687a-8779-4296-879a-5477d3e84e2f', 'pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circular-question-mark-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('circular-question-mark-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '649c1cb2e5085a00f0d0f65ad90be035bff07303f8385f5838e5310aeba585c9'

class Drawing(Sub32):
    icon_id = 'circular-question-mark-symbol-solo-profile32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_arc('p1-r1-1', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('p1-r1-2', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_arc('p2-r1-1', (13, 14), (20, 14), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_bezier('p2-r1-2', (20, 14), ((20, 16), (16, 16), (16, 17)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (16, 23), (16, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
