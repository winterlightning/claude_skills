"""Circular Question Mark Symbol: user-requested grid-fitted 32px version of circular-question-mark-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ._tall_base import SourceFaithfulSideSub
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'c356687a-8779-4296-879a-5477d3e84e2f'
SOURCE_PATH = 'pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'
SOLO_SOURCE_ICON_ID = 'circular-question-mark-symbol-solo'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'curved question hook', 'dot')

class DrawingVariant2(SourceFaithfulSideSub):
    canvas_width = 60
    canvas_height = 60
    icon_id = 'circular-question-mark-symbol-sub32-v2'
    variant_of = 'circular-question-mark-symbol-sub32'
    variant_label = 'Complete source on a proportionate canvas'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    tags = ('sub icon',)
    keywords = ('sub icon', 'grid fitted', 'circular question mark symbol')

    def build(self):
        self.add_arc('outline-top', (2, 30), (58, 30), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (58, 30), (2, 30), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_arc('hook', (24, 26), (36, 26), radius_x=6, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('turn', (36, 26), ((36, 30), (30, 30), (30, 30)))
        self.add_line('dot', (30, 44), (30, 44))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('question', 'hook', 'turn', closed=False)
        self.add_anchor('center', (30, 30))
