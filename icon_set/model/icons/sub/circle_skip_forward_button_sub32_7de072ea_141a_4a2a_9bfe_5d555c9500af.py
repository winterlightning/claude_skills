"""Circle Skip Forward Button: user-requested grid-fitted 32px version of circle-skip-forward-button-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='7de072ea-141a-4a2a-9bfe-5d555c9500af'
SOURCE_PATH='pictographic-primitives/other/circle button next_7de072ea-141a-4a2a-9bfe-5d555c9500af.svg'
SOLO_SOURCE_ICON_ID='circle-skip-forward-button-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='circle-skip-forward-button-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'circle skip forward button')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('play-1', (10, 11), (16, 16))
        self.add_line('play-2', (16, 16), (10, 21))
        self.add_line('play-3', (10, 21), (10, 11))
        self.add_line('stop', (22, 12), (22, 20))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('play', 'play-1', 'play-2', 'play-3', closed=True)
        self.add_anchor('center',(16, 16))
