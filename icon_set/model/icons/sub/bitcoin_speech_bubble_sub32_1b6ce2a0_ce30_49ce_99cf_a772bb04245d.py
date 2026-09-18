"""Bitcoin Speech Bubble: user-requested grid-fitted 32px version of bitcoin-speech-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='1b6ce2a0-ce30-49ce-99cf-a772bb04245d'
SOURCE_PATH='pictographic-primitives/symbol/messages bubble round bitcoin_1b6ce2a0-ce30-49ce-99cf-a772bb04245d.svg'
SOLO_SOURCE_ICON_ID='bitcoin-speech-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='bitcoin-speech-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'bitcoin speech bubble')
    def build(self):
        self.add_line('top', (8, 2), (24, 2))
        self.add_arc('tr', (24, 2), (28, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 23))
        self.add_arc('br', (28, 23), (24, 27), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('bottom', (24, 27), (12, 27))
        self.add_line('tail', (12, 27), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (8, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('coin-top', (11, 9), (17, 9))
        self.add_arc('upper', (17, 9), (17, 15), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('lower', (17, 15), (17, 20), radius_x=4, radius_y=3, large_arc=False, sweep=True)
        self.add_line('coin-bottom', (17, 20), (11, 20))
        self.add_line('spine', (11, 20), (11, 9))
        self.add_line('middle', (11, 15), (17, 15))
        self.add_line('tick--6--1', (11, 9), (11, 8))
        self.add_line('tick--6-1', (11, 20), (11, 21))
        self.add_line('tick-2--1', (17, 9), (17, 8))
        self.add_line('tick-2-1', (17, 20), (17, 21))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.add_contour('currency', 'coin-top', 'upper', 'lower', 'coin-bottom', 'spine', closed=True)
        self.relate('connect', 'currency', 'middle')
        self.relate('connect', 'currency', 'tick--6--1')
        self.relate('connect', 'currency', 'tick--6-1')
        self.relate('connect', 'currency', 'tick-2--1')
        self.relate('connect', 'currency', 'tick-2-1')
        self.add_anchor('center',(16, 16))
