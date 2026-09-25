"""Diagonal Expansion Arrow: user-requested grid-fitted 32px version of diagonal-expansion-arrow-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c84b5b94-cfc2-4c80-bb44-468cd2bc0cf6'
SOURCE_PATH='pictographic-primitives/interface-essential/expand_c84b5b94-cfc2-4c80-bb44-468cd2bc0cf6.svg'
SOLO_SOURCE_ICON_ID='diagonal-expansion-arrow-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='diagonal-expansion-arrow-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'diagonal expansion arrow')
    def build(self):
        self.add_line('stand-1', (2, 30), (2, 25))
        self.add_line('stand-2', (2, 25), (13, 25))
        self.add_line('stand-3', (13, 25), (13, 30))
        self.add_line('arrow', (14, 18), (30, 2))
        self.add_line('head-1', (21, 2), (30, 2))
        self.add_line('head-2', (30, 2), (30, 11))
        self.add_contour('stand', 'stand-1', 'stand-2', 'stand-3', closed=False)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate('connect', 'head', 'arrow')
        self.add_anchor('center',(16, 16))
