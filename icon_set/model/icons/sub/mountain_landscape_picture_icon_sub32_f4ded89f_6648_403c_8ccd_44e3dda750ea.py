"""Mountain Landscape Picture Icon: user-requested grid-fitted 32px version of mountain-landscape-picture-icon-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='f4ded89f-6648-403c-8ccd-44e3dda750ea'
SOURCE_PATH='pictographic-primitives/images/image_f4ded89f-6648-403c-8ccd-44e3dda750ea.svg'
SOLO_SOURCE_ICON_ID='mountain-landscape-picture-icon-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='mountain-landscape-picture-icon-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'mountain landscape picture icon')
    def build(self):
        self.add_line('frame-0', (6, 2), (26, 2))
        self.add_arc('frame-1', (26, 2), (30, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('frame-2', (30, 6), (30, 26))
        self.add_arc('frame-3', (30, 26), (26, 30), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('frame-4', (26, 30), (6, 30))
        self.add_arc('frame-5', (6, 30), (2, 26), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('frame-6', (2, 26), (2, 6))
        self.add_arc('frame-7', (2, 6), (6, 2), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('sun-top', (9, 11), (14, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('sun-bottom', (14, 11), (9, 11), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('mountains-1', (2, 26), (11, 21))
        self.add_line('mountains-2', (11, 21), (15, 25))
        self.add_line('mountains-3', (15, 25), (22, 17))
        self.add_line('mountains-4', (22, 17), (30, 26))
        self.add_contour('frame', 'frame-0', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6', 'frame-7', closed=True)
        self.add_contour('sun', 'sun-top', 'sun-bottom', closed=True)
        self.add_contour('mountains', 'mountains-1', 'mountains-2', 'mountains-3', 'mountains-4', closed=False)
        self.relate('connect', 'frame', 'mountains')
        self.add_anchor('center',(16, 16))
