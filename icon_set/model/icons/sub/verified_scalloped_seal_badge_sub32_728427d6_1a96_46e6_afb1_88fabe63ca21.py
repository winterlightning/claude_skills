"""Verified Scalloped Seal Badge: user-requested grid-fitted 32px version of verified-scalloped-seal-badge-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='728427d6-1a96-46e6-afb1-88fabe63ca21'
SOURCE_PATH='pictographic-primitives/interface-essential/check badge_728427d6-1a96-46e6-afb1-88fabe63ca21.svg'
SOLO_SOURCE_ICON_ID='verified-scalloped-seal-badge-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='verified-scalloped-seal-badge-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category = 'interface-essential'
    categories = ('interface-essential', 'state')
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'verified scalloped seal badge')
    def build(self):
        self.add_bezier('seal', (16, 2), ((19, 2), (19, 6), (23, 6)), ((26, 6), (26, 11), (29, 13)), ((30, 16), (27, 18), (26, 22)), ((26, 26), (22, 26), (19, 29)), ((16, 30), (14, 27), (10, 26)), ((6, 26), (6, 22), (3, 19)), ((2, 16), (5, 14), (6, 10)), ((6, 6), (10, 6), (13, 3)), ((14, 3), (15, 2), (16, 2)))
        self.add_line('check-1', (10, 16), (15, 19))
        self.add_line('check-2', (15, 19), (21, 13))
        self.add_contour('outline', 'seal', closed=True)
        self.add_contour('check', 'check-1', 'check-2', closed=False)
        self.add_anchor('center',(16, 16))
