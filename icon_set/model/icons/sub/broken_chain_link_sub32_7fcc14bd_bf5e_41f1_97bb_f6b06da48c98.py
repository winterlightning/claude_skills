"""Broken Chain Link: user-requested grid-fitted 32px version of broken-chain-link-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7fcc14bd-bf5e-41f1-97bb-f6b06da48c98'
SOURCE_PATH='pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'
SOLO_SOURCE_ICON_ID='broken-chain-link-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='broken-chain-link-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'broken chain link')
    def build(self):
        self.add_bezier('link-left', (14, 23), ((9, 28), (7, 30), (5, 30)), ((2, 30), (2, 25), (2, 23)), ((2, 20), (4, 18), (8, 14)))
        self.add_bezier('link-right', (18, 9), ((23, 4), (25, 2), (27, 2)), ((30, 2), (30, 7), (30, 9)), ((30, 12), (28, 14), (24, 18)))
        self.add_line('burst-a', (2, 9), (4, 9))
        self.add_line('burst-b', (11, 2), (11, 4))
        self.add_anchor('center',(16, 16))
