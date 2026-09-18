"""Virtual Reality Headset: user-requested grid-fitted 32px version of virtual-reality-headset-solo.
Plan: retain source primitive/contour topology and fit HRECT_XL ink (0, 2, 32, 30).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='8a515529-35b3-4547-9b35-3ae486711582'
SOURCE_PATH='pictographic-primitives/other/device wearable vr goggles_8a515529-35b3-4547-9b35-3ae486711582.svg'
SOLO_SOURCE_ICON_ID='virtual-reality-headset-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='virtual-reality-headset-sub32'
    keyshape=Keyshape.HRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'virtual reality headset')
    def build(self):
        self.add_line('outline-1', (2, 11), (5, 11))
        self.add_line('outline-2', (5, 11), (5, 7))
        self.add_line('outline-3', (5, 7), (9, 4))
        self.add_line('outline-4', (9, 4), (23, 4))
        self.add_line('outline-5', (23, 4), (27, 7))
        self.add_line('outline-6', (27, 7), (27, 11))
        self.add_line('outline-7', (27, 11), (30, 11))
        self.add_line('outline-8', (30, 11), (30, 21))
        self.add_line('outline-9', (30, 21), (27, 21))
        self.add_line('outline-10', (27, 21), (27, 25))
        self.add_line('outline-11', (27, 25), (23, 28))
        self.add_line('outline-12', (23, 28), (19, 28))
        self.add_line('outline-13', (19, 28), (16, 24))
        self.add_line('outline-14', (16, 24), (13, 28))
        self.add_line('outline-15', (13, 28), (9, 28))
        self.add_line('outline-16', (9, 28), (5, 25))
        self.add_line('outline-17', (5, 25), (5, 21))
        self.add_line('outline-18', (5, 21), (2, 21))
        self.add_line('outline-19', (2, 21), (2, 11))
        self.add_contour('outline', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', 'outline-12', 'outline-13', 'outline-14', 'outline-15', 'outline-16', 'outline-17', 'outline-18', 'outline-19', closed=True)
        self.add_anchor('center',(16, 16))
