"""Security Protection Shield: user-requested grid-fitted 32px version of security-protection-shield-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='948619df-4023-4222-a169-4dace0131ae9'
SOURCE_PATH='pictographic-primitives/other/shield 1_948619df-4023-4222-a169-4dace0131ae9.svg'
SOLO_SOURCE_ICON_ID='security-protection-shield-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='security-protection-shield-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'security protection shield')
    def build(self):
        self.add_bezier('shield', (16, 2), ((12, 4), (8, 6), (4, 6)), ((4, 17), (4, 24), (16, 30)), ((28, 24), (28, 17), (28, 6)), ((24, 6), (20, 4), (16, 2)))
        self.add_line('divider', (16, 2), (16, 30))
        self.add_contour('outline', 'shield', closed=True)
        self.relate('connect', 'outline', 'divider')
        self.add_anchor('center',(16, 16))
