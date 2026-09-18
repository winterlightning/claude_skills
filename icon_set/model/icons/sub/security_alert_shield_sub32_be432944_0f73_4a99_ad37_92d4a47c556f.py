"""Security Alert Shield: user-requested grid-fitted 32px version of security-alert-shield-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='be432944-0f73-4a99-ad37-92d4a47c556f'
SOURCE_PATH='pictographic-primitives/state/shield with exclamation_be432944-0f73-4a99-ad37-92d4a47c556f.svg'
SOLO_SOURCE_ICON_ID='security-alert-shield-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='security-alert-shield-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'security alert shield')
    def build(self):
        self.add_bezier('shield', (16, 2), ((12, 4), (8, 5), (4, 6)), ((4, 17), (4, 24), (16, 30)), ((28, 24), (28, 17), (28, 6)), ((24, 5), (20, 4), (16, 2)))
        self.add_line('stem', (16, 10), (16, 13))
        self.add_line('dot', (16, 20), (16, 20))
        self.add_contour('outline', 'shield', closed=True)
        self.add_anchor('center',(16, 16))
