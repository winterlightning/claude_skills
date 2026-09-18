"""Three Acupuncture Needles: user-requested grid-fitted 32px version of three-acupuncture-needles-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='c8865933-bab1-445f-94ab-65d5649059df'
SOURCE_PATH='pictographic-primitives/other/needles three_c8865933-bab1-445f-94ab-65d5649059df.svg'
SOLO_SOURCE_ICON_ID='three-acupuncture-needles-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='three-acupuncture-needles-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'three acupuncture needles')
    def build(self):
        self.add_line('needle-0', (2, 7), (24, 7))
        self.add_arc('handle-0-top', (24, 7), (30, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('handle-0-bottom', (30, 7), (24, 7), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('needle-1', (2, 16), (12, 16))
        self.add_arc('handle-1-top', (12, 16), (17, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('handle-1-bottom', (17, 16), (12, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('needle-2', (2, 25), (24, 25))
        self.add_arc('handle-2-top', (24, 25), (30, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('handle-2-bottom', (30, 25), (24, 25), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('handle-0', 'handle-0-top', 'handle-0-bottom', closed=True)
        self.add_contour('handle-1', 'handle-1-top', 'handle-1-bottom', closed=True)
        self.add_contour('handle-2', 'handle-2-top', 'handle-2-bottom', closed=True)
        self.relate('connect', 'needle-0', 'handle-0')
        self.relate('connect', 'needle-1', 'handle-1')
        self.relate('connect', 'needle-2', 'handle-2')
        self.add_anchor('center',(16, 16))
