"""Thai Baht Currency Symbol: user-requested grid-fitted 32px version of thai-baht-currency-symbol-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7c740c03-3323-47d7-93fa-89d191da2b7a'
SOURCE_PATH='pictographic-primitives/other/baht sign_7c740c03-3323-47d7-93fa-89d191da2b7a.svg'
SOLO_SOURCE_ICON_ID='thai-baht-currency-symbol-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='thai-baht-currency-symbol-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/finance'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'thai baht currency symbol')
    def build(self):
        self.add_line('top', (4, 4), (19, 4))
        self.add_arc('upper', (19, 4), (19, 16), radius_x=9, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('lower', (19, 16), (19, 28), radius_x=9, radius_y=6, large_arc=False, sweep=True)
        self.add_line('bottom', (19, 28), (4, 28))
        self.add_line('spine', (4, 28), (4, 4))
        self.add_line('middle', (4, 16), (19, 16))
        self.add_line('stem', (13, 2), (13, 30))
        self.add_contour('outline', 'top', 'upper', 'lower', 'bottom', 'spine', closed=True)
        self.relate('connect', 'outline', 'middle', 'stem')
        self.add_anchor('center',(16, 16))
