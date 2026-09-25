"""British Pound Sterling Message Bubble: user-requested grid-fitted 32px version of british-pound-sterling-message-bubble-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c6889dfd-e645-43b6-bcaf-969ba67629d7'
SOURCE_PATH='pictographic-primitives/other/message pound sign lines_c6889dfd-e645-43b6-bcaf-969ba67629d7.svg'
SOLO_SOURCE_ICON_ID='british-pound-sterling-message-bubble-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='british-pound-sterling-message-bubble-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'british pound sterling message bubble')
    def build(self):
        self.add_line('top', (9, 2), (23, 2))
        self.add_arc('tr', (23, 2), (28, 6), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_line('right', (28, 6), (28, 23))
        self.add_arc('br', (28, 23), (23, 28), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_line('bottom', (23, 28), (11, 28))
        self.add_line('tail', (11, 28), (4, 30))
        self.add_line('left', (4, 30), (4, 6))
        self.add_arc('tl', (4, 6), (9, 2), radius_x=5, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('hook', (20, 11), (14, 11), radius_x=3, radius_y=2, large_arc=False, sweep=False)
        self.add_line('stem', (14, 11), (14, 20))
        self.add_line('foot', (11, 20), (21, 20))
        self.add_line('bar', (11, 12), (15, 12))
        self.add_contour('outline', 'top', 'tr', 'right', 'br', 'bottom', 'tail', 'left', 'tl', closed=True)
        self.add_contour('currency', 'hook', 'stem', closed=False)
        self.relate('connect', 'currency', 'bar')
        self.relate('connect', 'currency', 'foot')
        self.add_anchor('center',(16, 16))
