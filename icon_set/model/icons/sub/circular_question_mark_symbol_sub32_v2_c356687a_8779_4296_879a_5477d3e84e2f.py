"""Circular Question Mark Symbol: user-requested grid-fitted 32px version of circular-question-mark-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c356687a-8779-4296-879a-5477d3e84e2f'
SOURCE_PATH='pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'
SOLO_SOURCE_ICON_ID='circular-question-mark-symbol-solo'
AUTHOR = 'gpt-6'
SOURCE_PARTS = ('enclosing circle', 'curved question hook', 'dot')
REPAIR_PLAN = {'concept': 'Circular Question Mark Symbol', 'core_parts': ('enclosing circle', 'curved question hook', 'dot'), 'flexible_parts': 'hook curve and gap', 'ladder': 'Widened question hook and separated the dot; circle, hook, and dot remain'}

class DrawingVariant2(Sub32):
    icon_id='circular-question-mark-symbol-sub32-v2'
    variant_label = 'Widened question hook and separated the dot; circle, hook, and dot remain'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circular question mark symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('hook', (11, 15), (21, 15), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_bezier('turn', (21, 15), ((21, 16), (16, 16), (16, 16)))
        self.add_line('dot', (16, 23), (16, 23))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('question', 'hook', 'turn', closed=False)
        self.add_anchor('center',(16, 16))
