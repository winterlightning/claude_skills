"""Medical Health Protection Shield: user-requested grid-fitted 32px version of medical-health-protection-shield-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='378dbc4a-8e49-4c92-8de6-23be0bf1d811'
SOURCE_PATH='pictographic-primitives/other/shield with plus_378dbc4a-8e49-4c92-8de6-23be0bf1d811.svg'
SOLO_SOURCE_ICON_ID='medical-health-protection-shield-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='medical-health-protection-shield-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'medical health protection shield')
    def build(self):
        self.add_bezier('shield', (16, 2), ((12, 4), (8, 6), (4, 6)), ((4, 17), (4, 24), (16, 30)), ((28, 24), (28, 17), (28, 6)), ((24, 6), (20, 4), (16, 2)))
        self.add_line('cross-h-1', (11, 15), (16, 15))
        self.add_line('cross-h-2', (16, 15), (21, 15))
        self.add_line('cross-v-1', (16, 10), (16, 15))
        self.add_line('cross-v-2', (16, 15), (16, 20))
        self.add_contour('outline', 'shield', closed=True)
        self.add_contour('cross-h', 'cross-h-1', 'cross-h-2', closed=False)
        self.add_contour('cross-v', 'cross-v-1', 'cross-v-2', closed=False)
        self.relate('connect', 'cross-h', 'cross-v')
        self.add_anchor('center',(16, 16))
