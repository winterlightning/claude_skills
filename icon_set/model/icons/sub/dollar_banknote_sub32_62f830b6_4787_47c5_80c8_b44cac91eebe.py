"""Dollar Banknote: user-requested grid-fitted 32px version of dollar-banknote-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='62f830b6-4787-47c5-80c8-b44cac91eebe'
SOURCE_PATH='pictographic-primitives/other/bill with dollar_62f830b6-4787-47c5-80c8-b44cac91eebe.svg'
SOLO_SOURCE_ICON_ID='dollar-banknote-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='dollar-banknote-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'dollar banknote')
    def build(self):
        self.add_line('outline-0', (5, 4), (27, 4))
        self.add_arc('outline-1', (27, 4), (30, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('outline-2', (30, 7), (30, 25))
        self.add_arc('outline-3', (30, 25), (27, 28), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('outline-4', (27, 28), (5, 28))
        self.add_arc('outline-5', (5, 28), (2, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('outline-6', (2, 25), (2, 7))
        self.add_arc('outline-7', (2, 7), (5, 4), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('top', (23, 15), (20, 12))
        self.add_bezier('upper', (20, 12), ((17, 8), (12, 12), (16, 16)))
        self.add_bezier('lower', (16, 16), ((20, 20), (15, 24), (12, 20)))
        self.add_line('foot', (12, 20), (9, 17))
        self.add_line('stem-top', (21, 11), (20, 12))
        self.add_line('stem-bottom', (12, 20), (11, 21))
        self.add_contour('outline', 'outline-0', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', closed=True)
        self.add_contour('currency', 'top', 'upper', 'lower', 'foot', closed=False)
        self.relate('connect', 'currency', 'stem-top')
        self.relate('connect', 'currency', 'stem-bottom')
        self.add_anchor('center',(16, 16))
