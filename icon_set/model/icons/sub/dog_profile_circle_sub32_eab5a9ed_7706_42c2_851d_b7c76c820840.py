"""Dog Profile Circle: user-requested grid-fitted 32px version of dog-profile-circle-solo.
Plan: retain source primitive/contour topology and fit CIRCLE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='eab5a9ed-7706-42c2-851d-b7c76c820840'
SOURCE_PATH='pictographic-primitives/pets/dog head_eab5a9ed-7706-42c2-851d-b7c76c820840.svg'
SOLO_SOURCE_ICON_ID='dog-profile-circle-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='dog-profile-circle-sub32'
    keyshape=Keyshape.CIRCLE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'dog profile circle')
    def build(self):
        self.add_arc('outline-top', (2, 16), (30, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_arc('outline-bottom', (30, 16), (2, 16), radius_x=14, radius_y=14, large_arc=False, sweep=True)
        self.add_line('dog-1', (15, 29), (15, 20))
        self.add_line('dog-2', (15, 20), (10, 20))
        self.add_line('dog-3', (10, 20), (8, 15))
        self.add_line('dog-4', (8, 15), (15, 12))
        self.add_line('dog-5', (15, 12), (15, 6))
        self.add_line('dog-6', (15, 6), (26, 20))
        self.add_contour('outline', 'outline-top', 'outline-bottom', closed=True)
        self.add_contour('dog', 'dog-1', 'dog-2', 'dog-3', 'dog-4', 'dog-5', 'dog-6', closed=False)
        self.relate('connect', 'outline', 'dog')
        self.add_anchor('center',(16, 16))
