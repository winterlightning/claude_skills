"""Vertical DNA Double Helix: user-requested grid-fitted 32px version of vertical-dna-double-helix-solo.
Plan: retain source primitive/contour topology and fit VRECT_L ink (4, 0, 28, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='3c216074-a57a-436c-81d8-30276fe1614e'
SOURCE_PATH='pictographic-primitives/other/dna vertical_3c216074-a57a-436c-81d8-30276fe1614e.svg'
SOLO_SOURCE_ICON_ID='vertical-dna-double-helix-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='vertical-dna-double-helix-sub32'
    keyshape=Keyshape.VRECT_L
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'vertical dna double helix')
    def build(self):
        self.add_bezier('strand-a', (6, 2), ((6, 11), (26, 21), (26, 30)))
        self.add_bezier('strand-b', (26, 2), ((26, 11), (6, 21), (6, 30)))
        self.add_line('rung-top', (6, 2), (26, 2))
        self.add_line('rung-bottom', (6, 30), (26, 30))
        self.relate('connect', 'strand-a', 'strand-b')
        self.relate('connect', 'strand-a', 'rung-top', 'rung-bottom')
        self.relate('connect', 'strand-b', 'rung-top', 'rung-bottom')
        self.add_anchor('center',(16, 16))
