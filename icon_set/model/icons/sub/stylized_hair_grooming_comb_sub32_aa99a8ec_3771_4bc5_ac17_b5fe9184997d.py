"""Stylized Hair Grooming Comb: user-requested grid-fitted 32px version of stylized-hair-grooming-comb-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='aa99a8ec-3771-4bc5-ac17-b5fe9184997d'
SOURCE_PATH='pictographic-primitives/other/comb_aa99a8ec-3771-4bc5-ac17-b5fe9184997d.svg'
SOLO_SOURCE_ICON_ID='stylized-hair-grooming-comb-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='stylized-hair-grooming-comb-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'stylized hair grooming comb')
    def build(self):
        self.add_bezier('back', (2, 28), ((11, 20), (20, 13), (27, 7)), ((30, 5), (30, 4), (27, 4)))
        self.add_line('tip', (27, 4), (30, 4))
        self.add_line('tooth-a', (5, 26), (2, 21))
        self.add_line('tooth-b', (13, 19), (10, 14))
        self.add_line('tooth-c', (22, 12), (19, 8))
        self.relate('connect', 'back', 'tip')
        self.relate('connect', 'back', 'tooth-a')
        self.relate('connect', 'back', 'tooth-b')
        self.relate('connect', 'back', 'tooth-c')
        self.add_anchor('center',(16, 16))
