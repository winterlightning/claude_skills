"""Bitcoin Cryptocurrency Symbol: user-requested grid-fitted 32px version of bitcoin-cryptocurrency-symbol-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='056563c8-a6c4-4201-b355-6ff5f08795ea'
SOURCE_PATH='pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg'
SOLO_SOURCE_ICON_ID='bitcoin-cryptocurrency-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='bitcoin-cryptocurrency-symbol-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'bitcoin cryptocurrency symbol')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('coin-top', (10, 8), (18, 8))
        self.add_arc('upper', (18, 8), (18, 16), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('lower', (18, 16), (18, 24), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('coin-bottom', (18, 24), (10, 24))
        self.add_line('spine', (10, 24), (10, 8))
        self.add_line('middle', (10, 16), (18, 16))
        self.add_line('tick--6--1', (10, 8), (10, 7))
        self.add_line('tick--6-1', (10, 24), (10, 25))
        self.add_line('tick-2--1', (18, 8), (18, 7))
        self.add_line('tick-2-1', (18, 24), (18, 25))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('currency', 'coin-top', 'upper', 'lower', 'coin-bottom', 'spine', closed=True)
        self.relate('connect', 'currency', 'middle')
        self.relate('connect', 'currency', 'tick--6--1')
        self.relate('connect', 'currency', 'tick--6-1')
        self.relate('connect', 'currency', 'tick-2--1')
        self.relate('connect', 'currency', 'tick-2-1')
        self.add_anchor('center',(16, 16))

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'bitcoin-cryptocurrency-symbol-sub32': {'status': 'cannot-fix',
                                         'date': '2026-09-23',
                                         'author': 'gpt-6',
                                         'source_icon_id': '056563c8-a6c4-4201-b355-6ff5f08795ea',
                                         'failures_at_review': ['mic [outline]: outline and '
                                                                'tick--6-1 are 3.18322 apart on '
                                                                'centerlines nearest (8.24777, '
                                                                '27.6576)<->(10, 25); SUB32 '
                                                                'requires at least 6 (ink '
                                                                'clearance 2) unless the contact '
                                                                'is declared with a scoped '
                                                                '`connect` relationship'],
                                         'blocker': 'The circle, two B bowls, middle bar, and '
                                                    'paired stem tips cannot maintain 8px parallel '
                                                    'stroke spacing and 6px frame clearance '
                                                    'together',
                                         'attempts': ['Original 32px B: frame-to-terminal MIC 3.18',
                                                      'Compact 32px B: parallel stem and bowl gaps '
                                                      '6 (<8), frame-to-tip gap 5.94 (<6)'],
                                         'evidence': 'icon_set/work/side-sub-repairs-2026-09-23/strict32-evidence'}}
